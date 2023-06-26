# Author: Dani Balagué Guardia 
# Date: June 22, 2023
# Description: This code generates an admonition to include Grasple
#              exercises in a Jupyter Book

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils import nodes
from docutils.parsers.rst import roles
from docutils.statemachine import ViewList

import re

exercise_titles = {}

class Grasple(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'label': directives.unchanged, 
                   'dropdown': directives.flag, 
                   'description': directives.unchanged}
    has_content = True
    counter = {}

    RE_CHAPTER_NUMBER = re.compile(r"/Chapter(?P<chapter_num>[0-9]+)/")

    def run(self):
        try:
            current_source = self.state.document.current_source

            m = self.RE_CHAPTER_NUMBER.search(current_source)

            if m != None:
                section_number = m["chapter_num"]
            else:
                section_number = 0

            Grasple.counter[section_number] = Grasple.counter.get(section_number, 0) + 1

            exercise_number = Grasple.counter[section_number]

            title_text = f'Grasple Exercise {section_number}.{exercise_number}'
            title_node = nodes.title(title_text, title_text)

            iframe_src = self.arguments[0]
            iframe_html = f"""
            <iframe src="{iframe_src}" width="95%" height="560px">
            </iframe>
            """

            if 'dropdown' in self.options:
                # Create the admonition node (an admonition) and add the title
                exercise_node = nodes.admonition()
                exercise_node += title_node

                # Use nested_parse to parse the description as reStructuredText
                description = self.options.get('description', '')
                if description:
                    viewlist = ViewList()
                    viewlist.append(description, '<description>')
                    desc_node = nodes.Element()
                    self.state.nested_parse(viewlist, 0, desc_node)
                    # Add the parsed description to the admonition node
                    exercise_node.extend(desc_node.children)

                # Add the iframe inside a details tag, but outside the summary tag
                iframe_html = f"""
                <details>
                    <summary>Show/Hide Content</summary>
                    {iframe_html}
                </details>
                """
                content_node = nodes.raw('', iframe_html, format='html')
                exercise_node += content_node
            else:
                content_node = nodes.raw('', iframe_html, format='html')
                exercise_node = nodes.admonition()
                exercise_node += title_node
                exercise_node += content_node

            label = self.options.get('label', None)
            if label is not None:
                label = f"{label}"
                target_node = nodes.target('', '', ids=[label])
                exercise_node.insert(0, target_node)
                self.state.document.note_explicit_target(target_node)
                exercise_titles[label] = title_text

            return [exercise_node]
        except Exception as e:
            error_node = nodes.error('', nodes.paragraph(text=str(e)))
            return [error_node]

def grasple_ref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    try:
        display_text = exercise_titles[text]
    except KeyError:
        msg = inliner.reporter.error(
            f'Unknown Grasple exercise: "{text}".', line=lineno)
        prb = nodes.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    node = nodes.reference(rawtext, display_text, refid=text, **options)
    return [node], []

roles.register_local_role('grasple_ref', grasple_ref_role)

def setup(app):
    app.add_directive("grasple", Grasple)
    app.connect('builder-inited', lambda app: exercise_titles.clear())

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }