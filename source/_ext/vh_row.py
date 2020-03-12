from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


def setup(app):
    app.add_node(vh_row_node, html=(visit_card_node, depart_card_node))
    app.add_directive('vh_row', VHRowDirective)
    return {'version': '0.1'}  # identifies the version of our extension


class vh_row_node(nodes.Structural, nodes.Element):
    pass


def visit_card_node(self, node):
    pass


def depart_card_node(self, node):
    pass


class VHRowDirective(Directive):
    required_arguments = 0
    optional_arguments = 2
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
        'bg_color': directives.unchanged,
        'element_id': directives.unchanged,
        'title': directives.unchanged
    }
    has_content = True
    add_index = True

    def run(self):
        sett = self.state.document.settings
        language_code = sett.language_code
        env = self.state.document.settings.env

        config = env.config

        options = self.options

        if ('element_id' in options):
            headerRow = nodes.container(ids=[options['element_id']])
        else:
            headerRow = nodes.container()

        headerRow['classes'].append(('{0}-container row-center').format(options['bg_color']))

        headerRowContainer = nodes.container()
        headerRowContainer['classes'].append('row bs-container')

        if 'title' in options:
            titleRowContainer = nodes.container()
            titleRowContainer['classes'].append('row bs-container')
            titleRowContainer += nodes.raw(text='<h2 style="margin-bottom:5px;">{0}</h2>'.format(options['title']),
                                           format='html')
            headerRow += titleRowContainer

        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)

        node = vh_row_node()
        node += par

        headerRowContainer += node

        headerRow += headerRowContainer

        # we return the result
        return [headerRow]
