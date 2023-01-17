import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives


DEFAULT_BASE_URL = 'https://openla.ewi.tudelft.nl/applet/'


class AppletDirective(Directive):
	option_spec = {
		'url': directives.unchanged,
		'fig_url': directives.unchanged,
		'fig_name': directives.unchanged,
		'description': directives.unchanged
	}
	has_content = False

	def run(self):
		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		url = self.options['url']
		fig_url = self.options['fig_url']
		fig_name = self.options['fig_name']
		description = self.options['description']

		applet_html = f'''
			<div class="applet">
				<noscript class="loading-lazy">
					<iframe src="{base_url}{url}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>
				</noscript>
			</div>
		'''
		applet = nodes.raw(None, applet_html, format='html')

		figure = nodes.figure(None)

		img = nodes.image(uri=fig_url)

		figure += applet
		figure += img
		figure += nodes.label(None, fig_name)  # ????
		figure += nodes.caption(text=description)
		return [figure]


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
