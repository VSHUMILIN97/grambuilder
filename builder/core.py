from pathlib import Path

from typing import Type, Callable, Optional, Mapping, List, ClassVar

import lxml.builder as xml

from lxml import etree

from builder.parsers.base import ParserProto


class Builder(object):
    """ Grammar builder API """

    ROOT_RULE: ClassVar[str] = 'RootRule'
    XML_NS: ClassVar[str] = 'http://www.w3.org/XML/1998/namespace'

    def __init__(
            self,
            path: str,
            loader: Callable[[Path], str],
            parser: Type[ParserProto],
            opts: Optional[Mapping[str, str]] = None
    ):
        _path = Path(path)
        _content = loader(_path)
        _parser: ParserProto = parser(_content, opts)
        self.data = _parser.parse()

    def build(self) -> str:
        """ Make text grammar from XML elements """
        grammar = self._get_grammar(self.data)
        return etree.tostring(
            grammar,
            pretty_print=True,
            encoding='utf-8',
            xml_declaration=True
        ).decode('utf-8')

    def _build_core_elements(self) -> Mapping[str, str]:
        """ Make dictionary with required headers for grxml file

        Notes: Check SRGS standard
            Kwargs cannot contain hyphens or html links
        """
        return {
            '{%s}lang' % self.XML_NS: 'ru-RU',
            'root': self.ROOT_RULE,
            'mode': 'voice',
            'version': '1.0',
            'xmlns': 'http://www.w3.org/2001/06/grammar',
            'tag-format': 'semantics/1.0'
        }

    def _get_grammar(self, items: List[str]) -> xml.E:
        """ Build grammar from retrieved items """
        return xml.E.grammar(
            xml.E.rule(
                xml.E(
                    'one-of',
                    *[
                        xml.E.item(
                            item
                        ) for item in items
                    ]
                ),
                id=self.ROOT_RULE
            ),
            self._build_core_elements(),
        )
