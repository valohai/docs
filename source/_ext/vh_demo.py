from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


def setup(app):
    app.add_node(vh_demo_node, html=(visit_card_node, depart_card_node))
    app.add_directive('vh_demo', VHDemo)
    return {'version': '0.1'}  # identifies the version of our extension


class vh_demo_node(nodes.Structural, nodes.Element):
    pass


def visit_card_node(self, node):
    pass


def depart_card_node(self, node):
    pass


class VHDemo(Directive):
    required_arguments = 0
    optional_arguments = 2
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
        'bg_color': directives.unchanged,
    }
    has_content = True
    add_index = True

    def run(self):
        sett = self.state.document.settings
        language_code = sett.language_code
        env = self.state.document.settings.env

        config = env.config

        options = self.options

        headerRow = nodes.container()
        headerRow['classes'].append('{0}-container row-center justify-content-center'.format(options['bg_color']))

        headerRowContainer = nodes.container()
        headerRowContainer['classes'].append('row bs-container justify-content-center')

        if 'title' in options:
            titleRowContainer = nodes.container()
            titleRowContainer['classes'].append('row bs-container justify-content-center')
            titleRowContainer += nodes.raw(
                text='<h2 style="margin-bottom:5px;">{0}</h2>'.format(options['title']),
                format='html'
            )
            headerRowContainer += titleRowContainer

        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)

        node = vh_demo_node()
        node += par

        headerRowContainer += node

        headerRowContainer += nodes.raw(
            text='<div style="padding: 25px 0;"> \
            <a class="btn btn-red inline-block mb-2 mr-6" href="http://valohai.com/book-a-demo/" target="_blank">Book a demo</a> \
            </div>',
            format='html'
        )
        headerRow += headerRowContainer

        # we return the result
        return [headerRow]
