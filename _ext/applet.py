import os
from typing import Optional
from urllib.parse import quote
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.directives.patches import Figure


DEFAULT_BASE_URL = 'https://openla.ewi.tudelft.nl/applet/'


def generate_style(height: Optional[str], width: Optional[str]):
	'''
	Given a height and width, generates an inline style that can be used in HTML.
	'''

	styles = ''

	if height:
		styles += f'height: {height};'

	if width:
		styles += f'width: {width};'

	return styles


def parse_value(val: str) -> str:
	'''
	Parses a string value to a string that can be used in a URL query parameter. This is a hacky way to use boolean in docutils.
	(For some reason docutils can't parse 'true' or 'True' strings??)
	'''

	if val == 'enabled':
		return 'true'
	elif val == 'disabled':
		return 'false'
	else:
		return str(val)


def parse_options(options: dict) -> dict:
	# if options is None:
	# 	return {}

	# Settings keys that are passed along to the applet iframe
	applet_keys = ['title', 'background', 'autoPlay', 'position', 'isPerspectiveCamera', 'enablePan', 'distance', 'zoom']

	return {key: parse_value(val) for key, val in options.items() if key in applet_keys and val != ''}


class AppletDirective(Figure):
	option_spec = Figure.option_spec.copy()
	option_spec.update({
		'url': directives.unchanged,
		'fig_url': directives.unchanged,
		'title': directives.unchanged,
		'background': directives.unchanged,
		'autoPlay': directives.unchanged,
		'position': directives.unchanged,
		'isPerspectiveCamera': directives.unchanged,
		'enablePan': directives.unchanged,
		'distance': directives.unchanged,
		'zoom': directives.unchanged,
		'height': directives.unchanged,
		'width': directives.unchanged,
	})
	required_arguments = 0


	def run(self):
		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		url = self.options['url']
		fig_url = self.options['fig_url']

		self.arguments = [fig_url]
		self.options['class'] = ['applet-print-figure']
		(figure,) = Figure.run(self)

		params_dict = parse_options(self.options)
		params = '&'.join([f'{key}={quote(value)}' for key, value in params_dict.items()])
		style = generate_style(self.options.get('width', None), self.options.get('height', None))

		applet_html = f'''
			<div class="applet" style={style}>
				<noscript class="loading-lazy">
					<iframe src="{base_url}{url}?{params}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>
				</noscript>
			</div>
		'''
		applet = nodes.raw(None, applet_html, format='html')

		return [applet, figure]


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
