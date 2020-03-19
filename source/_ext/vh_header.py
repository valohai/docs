from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


def setup(app):
    app.add_node(ValohaiHeaderNode, html=(visit_card_node, depart_card_node))
    app.add_directive('vh_header', ValohaiHeaderDirective)
    return {'version': '0.1'}  # identifies the version of our extension


class ValohaiHeaderNode(nodes.Structural, nodes.Element):
    pass


def visit_card_node(self, node):
    pass


def depart_card_node(self, node):
    pass


class ValohaiHeaderDirective(Directive):
    # defines the parameter the directive expects
    # directives.unchanged means you get the raw value from RST
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged
    }
    has_content = True
    add_index = True

    def run(self):
        sett = self.state.document.settings
        language_code = sett.language_code
        env = self.state.document.settings.env

        # gives you access to the parameter stored
        # in the main configuration file (conf.py)
        config = env.config

        # gives you access to the options of the directive
        options = self.options

        # we create a card and we add the section
        header_row_container = nodes.container(ids=['headerContainer'])
        header_row_container['classes'].append('dark-container row-center')

        header_column = nodes.container()
        header_column['classes'].append('bs-container')

        header_row = nodes.container()
        header_row['classes'].append('row-justify-end')

        text_col = nodes.container()
        text_col['classes'].append('col-4')

        text_content = nodes.paragraph(text=options['title'])
        text_content['classes'].append('header-text-light')

        text_col += text_content
        header_row += text_col

        search_col = nodes.container()
        search_col['classes'].append('bs-container col-7')

        search_form_group = nodes.container(ids=['searchForm'])
        search_form_group['classes'].append('form-group has-search')

        search_form = nodes.raw(
            text='<section id="search" role="search">' \
                 '<form class="search" action="/search/" method="get">' \
                 '<div class="form-group">' \
                 '<span class="fa fa-search form-control-feedback form-control-lg"></span>' \
                 '<input type="search" class="form-control form-control-lg" name="q" placeholder="Search our docs" />' \
                 '<input type="hidden" name="check_keywords" value="yes" />' \
                 '<input type="hidden" name="area" value="default" />' \
                 '</div>' \
                 '</form>' \
                 '</section>',
            format='html'
        )

        search_form += nodes.raw(
            text='<p id="popularlinks">Most popular topics: <a href="/core-concepts/">our core concepts</a>, ' \
                 '<a href="/valohai-yaml/">valohai.yaml</a> or '
                 '<a href="/valohai-cli/">valohai-cli</a></p>',
            format='html'
        )

        search_form_group += search_form

        search_col += search_form_group
        header_row += search_col

        header_column += header_row

        header_row_container += header_column

        # we return the result
        return [header_row_container]
