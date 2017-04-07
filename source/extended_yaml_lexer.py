import re

from pygments.lexers.data import YamlLexer
from pygments.token import Number, Token, Keyword


class ExtendedYAMLLexer(YamlLexer):
    def get_tokens(self, text, unfiltered=False):
        for type, value in super().get_tokens(text, unfiltered):
            if type == Token.Literal.Scalar.Plain:
                if value.isdigit() or re.match('^[0-9]*\.[0-9]+$', value):  # Smells like a number
                    type = Number
                if value in ('true', 'false', 'yes', 'no'):
                    type = Keyword
            yield (type, value)
