"""
Common parser, which is do nothing, but uses the content of the file
and return the processed content
"""
from typing import List, Mapping, Optional
from typing_extensions import runtime_checkable, Protocol


@runtime_checkable
class ParserProto(Protocol):
    content: str
    parser_options: Optional[Mapping[str, str]]

    def parse(self) -> List[str]: ...


class BaseParser(ParserProto):
    """ Default parser for the text files """

    def __init__(
            self,
            content: str,
            p_opts: Optional[Mapping[str, str]] = None
    ):
        self.content: str = content
        self.p_opts: Mapping[str, str] = p_opts if p_opts is not None else {}

    def parse(self) -> List[str]:
        """ Create array of non-empty strings from given content

        Returns:
            <item /> tag content iterable

        """
        return [
            line for line in filter(
                None,
                [line.strip() for line in self.content.splitlines()]
            )
        ]
