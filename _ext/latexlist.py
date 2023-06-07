from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.parsers.rst import roles
import roman
from docutils.statemachine import StringList



class LatexListItem(nodes.list_item):
    pass

class LatexList(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'enumerated': directives.flag,
        'type': directives.unchanged
    }

    def run(self):
        enumerated = 'enumerated' in self.options
        list_type = self.options.get('type', '')

        if enumerated:
            list_node = nodes.enumerated_list()
            if list_type == 'i':
                list_node['enumtype'] = 'lowerroman'
            elif list_type == 'a':
                list_node['enumtype'] = 'loweralpha'
            else:
                list_node['enumtype'] = 'arabic'
        else:
            list_node = nodes.bullet_list()

        item_node = None
        self.item_content = r""
        for line in self.content:
            if line.startswith('\\item'):

                if self.item_content != "":
                    para = nodes.paragraph()
                    self.state.nested_parse(StringList([self.item_content]), self.content_offset, para)
                    item_node += para
                    self.item_content = r""

                if item_node:
                    list_node += item_node
                item_node = LatexListItem()
                para = nodes.paragraph()
                self.item_content += line[5:].strip() + "\n"
            elif line.startswith('\\label{'):
                label_id = line[7:-1]
                item_node['ids'].append(label_id)
            else:
                self.item_content += line.strip() + "\n"

        # Add the last list item to the list as it is not covered with the current code.
        para = nodes.paragraph()
        self.state.nested_parse(StringList([self.item_content]), self.content_offset, para)
        item_node += para

        if item_node:
            list_node += item_node

        return [list_node]

    def visit_LatexListItem(self, node):
        if self.builder.format == 'latex':
            pass
        else:
            self.body.append(self.starttag(node, 'li', '', CLASS='latex-list'))

    def depart_LatexListItem(self, node):
        if self.builder.format == 'latex':
            pass
        else:
            self.body.append('</li>\n')

def find_list_item(doctree, label):
    for node in doctree.traverse(LatexListItem):
        if label in node['ids']:
            return node
    return None

import logging
logger = logging.getLogger(__name__)

def get_item_display_text(list_item):
    item_number = list_item.parent.index(list_item) + 1
    display_text = str(item_number)

    if list_item.parent.tagname == 'enumerated_list':
        enumtype = list_item.parent.get('enumtype', '')

        if enumtype == 'loweralpha':
            display_text = chr(ord('a') + item_number - 1) + '.'
        elif enumtype == 'lowerroman':
            display_text = roman.toRoman(item_number).lower() + '.'
        else:
            display_text = str(item_number) + '.'
    else:
        # If the parent is not an enumerated list, keep the display_text as is.
        pass

    return display_text


def itemref_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    list_item = find_list_item(inliner.document, text)
    if list_item is None:
        msg = f"Could not find list item with label '{text}'"
        inliner.reporter.error(msg, line=lineno)
        return [nodes.problematic(rawtext, rawtext, msg)], [msg]

    display_text = get_item_display_text(list_item)
    node = nodes.reference(rawtext, display_text, refuri="#" + text, **options)
    return [node], []

roles.register_local_role('itemref', itemref_role)

def setup(app):
    app.add_node(LatexListItem,
                 html=(LatexList.visit_LatexListItem, 
                       LatexList.depart_LatexListItem))
    app.add_directive('latexlist', LatexList)
