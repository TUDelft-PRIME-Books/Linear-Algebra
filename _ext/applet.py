import os

from docutils import nodes
from docutils.parsers.rst import Directive, directives


DEFAULT_BASE_URL = 'https://openla.ewi.tudelft.nl/applet/'


class AppletDirective(Directive):
	option_spec = {
		'url': directives.unchanged,
		'description': directives.unchanged
	}
	has_content = False

	def run(self):
		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		url = self.options['url']
		description = self.options['description']

		content = f'<div class="applet">\n  <noscript class="loading-lazy">\n    <iframe src="{base_url}{url}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>\n  </noscript>\n</div>'

		return [nodes.raw('', content, format='html')]


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
