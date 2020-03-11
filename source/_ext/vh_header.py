from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.locale import _
from docutils.parsers.rst import directives

def setup(app):
    app.add_node(vh_header_node, html=(visit_card_node, depart_card_node))
    app.add_directive('vh_header', VHHeaderDirective)

    return {'version': '0.1'}   # identifies the version of our extension

class vh_header_node(nodes.Structural, nodes.Element):
    pass

def visit_card_node(self, node):
    pass
 
def depart_card_node(self, node):
    pass

class VHHeaderDirective(Directive):
 
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
        headerRowContainer = nodes.container(ids=['headerContainer'])
        headerRowContainer['classes'].append('dark-container row-center')

        headerColumn = nodes.container()
        headerColumn['classes'].append('bs-container')

        headerRow = nodes.container()
        headerRow['classes'].append('row-justify-end')

        textCol = nodes.container()
        textCol['classes'].append('col-4')

        textContent = nodes.paragraph(text=options['title'])
        textContent['classes'].append('header-text-light')

        textCol += textContent
        headerRow += textCol
        
        searchCol = nodes.container()
        searchCol['classes'].append('bs-container col-7')

        searchFormGroup = nodes.container(ids=['searchForm'])
        searchFormGroup['classes'].append('form-group has-search')
        
        searchForm = nodes.raw(text='<section id="search" role="search">' \
                                        '<form class="search" action="/search/" method="get">' \
                                            '<div class="form-group">' \
                                                '<span class="fa fa-search form-control-feedback form-control-lg"></span>' \
                                                '<input type="search" class="form-control form-control-lg" name="q" placeholder="Search our docs" />' \
                                                '<input type="hidden" name="check_keywords" value="yes" />'\
                                                '<input type="hidden" name="area" value="default" />'\
                                            '</div>'\
                                        '</form>'\
                                        '</section>', format='html')
        
        searchForm += nodes.raw(text='<p id="popularlinks">Most popular topics: <a href="/docs/core-concepts/index">our core concepts</a>, ' \
                                        '<a href="/docs/valohai-yaml">valohai.yaml</a> or '
                                        '<a href="/docs/valohai-cli">valohai-cli</a></p>'
                                        , format='html')
        
        
        searchFormGroup += searchForm


        searchCol += searchFormGroup
        headerRow += searchCol

        headerColumn+= headerRow

        headerRowContainer += headerColumn
        


        # we return the result
        return [ headerRowContainer ]