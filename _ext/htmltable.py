from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table
from docutils.parsers.rst import roles
from docutils.nodes import entry

from sphinx.locale import _
from bs4 import BeautifulSoup as bs

def align(argument):
    return directives.choice(argument, ('left', 'center', 'right'))

class centry(entry):

    basic_attributes = ('ids', 'classes', 'colspan', 'names', 'dupnames')
    local_attributes = ('backrefs',)
    list_attributes = basic_attributes + local_attributes
    known_attributes = list_attributes + ('source',)
    tagname = 'entry'
    child_text_separator = '\n\n'

class HTMLTableDirective(Table):

    option_spec = {'header-rows': directives.nonnegative_int,
                'stub-columns': directives.nonnegative_int,
                'width': directives.length_or_percentage_or_unitless,
                'widths': directives.value_or(('auto', ),
                                                directives.positive_int_list),
                'class': directives.class_option,
                'name': directives.unchanged,
                'title' : directives.unchanged,
                'align': align} 

    def run(self):

        col_widths = []

        title, messages = self.make_title()

        node = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, node)

        html_table_text = self.block_text.split('\n\n')[-1].strip(' ')
        
        table_soup = bs(html_table_text,"html.parser")
        table_head = table_soup.find('thead')

        total_rows = table_soup.find_all('tr')
        max = 0
        for row in total_rows:
            num_cols = len(row.find_all('td'))
            if num_cols >= max:
                max = num_cols

        table = nodes.table()

        tgroup = nodes.tgroup()
        table += tgroup

        for i in range(max):
            colspec = nodes.colspec(colwidth=1)
            tgroup += colspec

        num_head_rows = len(table_soup.find('thead').find_all('tr'))

        #table['classes'] += ['colwidths-auto']
        rows = []

        # parse the body of the table:
        body_rows = table_soup.find('tbody').find_all('tr')

        for row in body_rows:
            row_node = nodes.row()
            cell_list = row.find_all('td')
            for cell in cell_list:
                entry = nodes.entry()
                entry += nodes.raw(None,cell.text,format='html')
                row_node += entry
            rows.append(row_node)


        if table_head != None:
            th_rows = []
            table_head_rows = table_head.find_all('tr')

            for row in table_head_rows:
                row_node = nodes.row()
                cell_list = row.find_all('th')
                for cell in cell_list:
                    cell_text = nodes.raw(None,cell.text,format='html')
                    attrs = {}
                    if len(cell.attrs) > 0:
                        for key,value in cell.attrs.items():
                            if key == 'colspan':
                                attrs['morecols']=int(value)-1
                            if key == 'rowspan':
                                attrs['morerows']=int(value)-1
                            else:
                                attrs[key] = str(value)

                    node_entry = nodes.entry(**attrs)
                    node_entry.extend(cell_text)
                    row_node += node_entry

                th_rows.append(row_node)

            rows = th_rows + rows
            thead = nodes.thead()
            thead.extend(rows[:num_head_rows])
            tgroup += thead

        tbody = nodes.tbody()
        tbody.extend(rows[num_head_rows:])
        tgroup += tbody

        self.set_table_width(table)
        self.add_name(table)

        if title:
            table.insert(0,title)

        table_node = nodes.raw(None, html_table_text)
        return [table]
        #return [table]+messages

def visit_htmltable_node(self, node):
    pass

def depart_htmltable_node(self, node):
    pass


def setup(app):

    app.add_directive('htmltable',HTMLTableDirective)
    return {
        'version': '0.1.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
