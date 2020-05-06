import enum

from typing import Type

from .base import ParserProto, BaseParser


class Parsers(enum.Enum):
    """ Parsers variants """
    BASE = 'base'

    def get_parser(self) -> Type[ParserProto]:
        """ Get appropriate parser from given input """
        return _parsers[self]


_parsers = {
    Parsers.BASE: BaseParser
}
