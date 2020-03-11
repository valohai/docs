from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.locale import _
from docutils.parsers.rst import directives

def setup(app):
    app.add_node(card_node, html=(visit_card_node, depart_card_node))
    app.add_directive('card', CardDirective)

    return {'version': '0.1'}   # identifies the version of our extension

class card_node(nodes.Structural, nodes.Element):
    pass

class cardCollection_node(nodes.Structural, nodes.Element):
    pass

def visit_card_node(self, node):
    pass
 
def depart_card_node(self, node):
    pass


class CardDirective(Directive):
 
    # defines the parameter the directive expects
    # directives.unchanged means you get the raw value from RST
    required_arguments = 0
    optional_arguments = 4
    final_argument_whitespace = True
    option_spec = {
                    'box-style': directives.unchanged,
                    'image': directives.unchanged,
                    'image_alt': directives.unchanged,
                    'cta': directives.unchanged, 
                    'cta_link': directives.unchanged,
                    'button': directives.unchanged,
                    'title': directives.unchanged,
                    'title_link': directives.unchanged,
                    'columns': directives.unchanged,  }
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
         
        # we create the content of the blog post
        # because it contains any kind of RST
        # we parse parse it with function nested_parse
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)

        text_align_class = ''
        if('box-style' in options and options['box-style'] == 'center') : 
            text_align_class = '-center'
         
        # we create a card and we add the section
        bodyContainer = nodes.container()
        bodyContainer['classes'].append('card-body{0}'.format(text_align_class))
        node = card_node()
        node.set_class('card-body-{0}'.format(text_align_class))

        btnClass = 'btn'
        if('button' in options) :
            btnClass = 'btn btn-' + options['button'] 
        
        if('image' in options) :
            if('cta_link' in options) :
                node += nodes.raw(text='<a class="external text-center" href="{0}"><img src="{1}" alt="{2}" /></a>'.format(options['cta_link'], options['image'], options['image_alt']), format='html')
            else :
                node += nodes.image(uri=options['image'], alt=options['image_alt'])
        if('cta' in options) :
            node += nodes.raw(text='<p><a class="reference external {0}" href="{1}">{2}</a></p>'.format(btnClass, options['cta_link'], options['cta']), format='html')
        

        if('title' in options) :
            if('title_link' in options) :
                node += nodes.raw(text='<a class="h6 blue-link" href={0}>{1}</a>'.format(options['title_link'], options['title']), format='html')
            else :
                node += nodes.raw(text='<p class="h5">{0}</p>'.format(options['title']), format='html')


        node += par

        bodyContainer += node

        columns = 3
        if('columns' in options) :
            columns = options['columns']

        cardContainer = nodes.container()
        cardContainer['classes'].append('card-set-{0}cols'.format(columns))
        cardContainer += bodyContainer
         
        # we return the result
        return [ cardContainer ]
