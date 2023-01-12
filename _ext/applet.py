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

		content = f'<h1>HELOOOO</h1> {base_url}{url} (description: {description})'

		return [nodes.raw(rawsource=content)]


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
