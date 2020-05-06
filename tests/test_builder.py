import os

from builder.core import Builder
from builder.loaders import make_text_loader
from builder.parsers import Parsers


CUR_PATH = os.path.dirname(__file__)


def test_core_for_grammar():
    """ Checks: grxml build for valid test grammar from text """
    with open(os.path.join(CUR_PATH, 'test.grxml')) as grxml:
        example = grxml.read()
    with open(os.path.join(CUR_PATH, 'test.txt')) as txt:
        text = txt.read()
    loader = make_text_loader(text)
    bldr = Builder('.', loader, Parsers('base').get_parser())
    grammar = bldr.build()
    assert grammar == example
