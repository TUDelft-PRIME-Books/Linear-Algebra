from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils import nodes
from docutils.parsers.rst import roles
import re

exercise_titles = {}

class Grasple(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'label': directives.unchanged}
    has_content = True
    counter = {}

    RE_CHAPTER_NUMBER = re.compile(r"/Chapter(?P<chapter_num>[0-9]+)/")

    def run(self):
        try:
            # Get the chapter number from the path. Not ideal but it works for now. 
            current_source = self.state.document.current_source

            m = self.RE_CHAPTER_NUMBER.search(current_source)

            if m != None:
                section_number = m["chapter_num"]
            else:
                section_number = 0

            # Increment the counter for this section
            Grasple.counter[section_number] = Grasple.counter.get(section_number, 0) + 1

            # Get the exercise number for this section
            exercise_number = Grasple.counter[section_number]

            # Create the title node, including the exercise number
            title_text = f'Grasple Exercise {section_number}.{exercise_number}'
            title_node = nodes.title(title_text, title_text)

            # Create the content node
            iframe_src = self.arguments[0]  # Get the URL of the iframe from the directive argument
            iframe_html = f"""
            <iframe src="{iframe_src}" width="95%" height="560px">
            </iframe>
            """
            content_node = nodes.raw('', iframe_html, format='html')

            # Create the exercise node (an admonition) and add the title and content
            exercise_node = nodes.admonition()
            exercise_node += title_node
            exercise_node += content_node

            label = self.options.get('label', None)
            if label is not None:
                label = f"{label}"  # Prepend "grasple-" to the label
                target_node = nodes.target('', '', ids=[label])
                exercise_node.insert(0, target_node)
                self.state.document.note_explicit_target(target_node)
                exercise_titles[label] = title_text  # Store the title in the global dictionary

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