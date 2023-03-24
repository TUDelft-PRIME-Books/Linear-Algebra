from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

class ParenthesizedEnumeratedListItem(nodes.list_item):
    pass

class ParenList(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {'start': directives.nonnegative_int}

    def run(self):

        node = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset,node)

        start = self.options.get('start', 1)
        list_node = nodes.enumerated_list(start=start, style='none')
        list_item_template = ParenthesizedEnumeratedListItem()

        for item in node.children[0]:
            list_item = list_item_template.deepcopy()
            list_item += item.children[0].children
            list_node += list_item

        return [list_node]

def visit_ParenthesizedEnumeratedListItem(self, node):
    self.body.append(self.starttag(node, 'li', '', CLASS='paren-list', style='list-style-type: none;'))
    prefix = '(' + str(node.parent.index(node) + node.parent['start']) + ') '
    self.body.append(prefix)

def depart_ParenthesizedEnumeratedListItem(self, node):
    self.body.append('</li>\n')

def setup(app):
    app.add_node(ParenthesizedEnumeratedListItem,
                 html=(visit_ParenthesizedEnumeratedListItem, depart_ParenthesizedEnumeratedListItem))
    app.add_directive('paren-list', ParenList)
