import pytest

from builder.parsers.base import BaseParser


@pytest.mark.parametrize(
    'text, opts, expected', [
        (
            (
                """
                a
                b,
                cd
                forsenCD
                
                """,
                None,
                ['a', 'b,', 'cd', 'forsenCD']
            )
        ),
        (
                """
                a
                b,
                cd
                forsenCD
            
                """,
                {'depth': '500', 'parse_quality': 'xd'},
                ['a', 'b,', 'cd', 'forsenCD']
        ),
    ]
)
def test_base_parser_smoke(text, opts, expected):
    """ Checks: Common parser behaviour """
    parser = BaseParser(text, opts)
    result = parser.parse()
    assert result == expected
