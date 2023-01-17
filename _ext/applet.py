import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.images import Figure


DEFAULT_BASE_URL = 'https://openla.ewi.tudelft.nl/applet/'


class AppletDirective(Figure):
	option_spec = Figure.option_spec.copy()
	option_spec.update({
		'url': directives.unchanged,
		'fig_url': directives.unchanged,
	})
	required_arguments = 0
	# has_content = True

	def run(self):
		# TODO: assert has content
		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		url = self.options['url']
		fig_url = self.options['fig_url']

		self.arguments = [fig_url]
		(figure,) = Figure.run(self)


		applet_html = f'''
			<div class="applet">
				<noscript class="loading-lazy">
					<iframe src="{base_url}{url}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>
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
