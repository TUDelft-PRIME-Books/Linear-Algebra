import os
import json
import urllib
from docutils import nodes
from docutils.parsers.rst import Directive, directives


DEFAULT_BASE_URL = 'https://openla.ewi.tudelft.nl/applet/'


class AppletDirective(Directive):
	option_spec = {
		'url': directives.unchanged_required,
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
		'debug': directives.unchanged,
	}
	has_content = False

	def parse_styles(self):
		'''
		Parses the styles from the options and returns a string that can be used in the HTML.
		'''

		styles = ''

		if 'width' in self.options:
			styles += f'width: {self.options["width"]};'

		if 'height' in self.options:
			styles += f'height: {self.options["height"]};'

		return styles


	def parse_param(self, val: str) -> str:
		'''
		Parses a string value to a string that can be used in a URL query parameter. This is a hacky way to use boolean in docutils.
		(For some reason docutils can't parse 'true' or 'True' strings??)
		'''

		match val:
			case 'enabled':
				return 'true'
			case 'disabled':
				return 'false'
			case _:
				return str(val)


	def parse_options(self) -> dict:
		params_dict = dict()

		# Guard to check if options is None
		if self.options is None:
			return params_dict

		# Keys that are parsed as is
		parse_keys = ['title', 'background', 'autoPlay', 'position', 'isPerspectiveCamera', 'enablePan', 'distance', 'zoom']

		params_dict = {key: self.parse_param(val) for key, val in self.options.items() if key in parse_keys and val != ''}

		return params_dict


	def run(self):
		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		url = self.options['url']

		styles = self.parse_styles()

		params_dict = self.parse_options()

		# Format dict as URL query parameters
		params = '&'.join([f'{key}={urllib.parse.quote(value)}' for key, value in params_dict.items()])

		content = f'<div class="applet">\n  <noscript class="loading-lazy">\n  <iframe styles="{styles}" src="{base_url}{url}?{params}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>\n  </noscript>\n</div>'

		output = [nodes.raw('', content, format='html')]

		if 'debug' in self.options:
			debug_node = nodes.paragraph(text=json.dumps(self.options))
			output.append(debug_node)

		return output


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
