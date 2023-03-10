from docutils import nodes
from docutils.parsers.rst import Directive


class Review(Directive):

    def run(self):
        review_text="""
        <div style="text-align: center; font-size: 32px; color: red">
        This section is under review
        </div>
        """
        text = nodes.raw(None,review_text,format='html')
        paragraph_node = nodes.paragraph()
        paragraph_node += text
        return [paragraph_node]


def setup(app):
    app.add_directive("review", Review)

    return {
                'version': '0.1',
                'parallel_read_safe': True,
                'parallel_write_safe': True,
            }
