from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


def setup(app):
    app.add_node(ValohaiRowNode, html=(visit_card_node, depart_card_node))
    app.add_directive('vh_row', ValohaiRowDirective)
    return {'version': '0.1'}  # identifies the version of our extension


class ValohaiRowNode(nodes.Structural, nodes.Element):
    pass


def visit_card_node(self, node):
    pass


def depart_card_node(self, node):
    pass


class ValohaiRowDirective(Directive):
    required_arguments = 0
    optional_arguments = 2
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
        'bg_color': directives.unchanged,
        'element_id': directives.unchanged,
    }
    has_content = True
    add_index = True

    def run(self):
        sett = self.state.document.settings
        language_code = sett.language_code
        env = self.state.document.settings.env

        config = env.config

        options = self.options

        if 'element_id' in options:
            header_row = nodes.container(ids=[options['element_id']])
        else:
            header_row = nodes.container()

        header_row['classes'].append(('{0}-container row-center').format(options['bg_color']))

        header_row_container = nodes.container()
        header_row_container['classes'].append('row bs-container')

        if 'title' in options:
            title_row_container = nodes.container()
            title_row_container['classes'].append('row bs-container')
            title_row_container += nodes.raw(
                text='<h2 style="margin-bottom:5px;">{0}</h2>'.format(options['title']),
                format='html'
            )
            header_row += title_row_container

        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)

        node = ValohaiRowNode()
        node += par

        header_row_container += node

        header_row += header_row_container

        # we return the result
        return [header_row]
