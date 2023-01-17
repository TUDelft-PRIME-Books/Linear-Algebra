import os
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
	}
	has_content = False

	def parseOption(self, key: str, params_dict: dict) -> dict:
		if key in self.options:
			params_dict[key] = str(self.options[key])
		
		return params_dict

	
	def parseOptions(self) -> dict:
		params_dict = dict()

		# Guard to check if options is None
		if self.options is None:
			return params_dict

		# Keys that are parsed as is
		parse_keys = ['title', 'background', 'autoPlay', 'position', 'isPerspectiveCamera', 'enablePan', 'distance', 'zoom']

		params_dict = {key: str(self.options[key]) for key in parse_keys if key in self.options}

		# for key in parse_keys:
		# 	params_dict = self.parseOption(key, params_dict)

		return params_dict


	def run(self):
		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		url = self.options['url']
		
		# TODO: parse width & height

		# title = self.options['title'] if 'title' in self.options else 'Applet'

		params_dict = self.parseOptions()

		# {a: '1', b: '2', c: '1,2,3'} -> 'a=1&b=2&c=1,2,3'
		params = '&'.join([f'{key}={value}' for key, value in params_dict.items()])

		content = f'<div class="applet">\n  <noscript class="loading-lazy">\n  <iframe src="{base_url}{url}?{params}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>\n  </noscript>\n</div>'

		return [nodes.raw('', content, format='html')]


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
