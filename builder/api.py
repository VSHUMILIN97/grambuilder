""" API builder public API """
import click

from .core import Builder
from .loaders import make_text_loader
from .parsers import Parsers


@click.command()
@click.option(
    '--source-path',
    '-s',
    help=(
        'Path to the text file with normalised item sources'
    )
)
def console() -> int:
    """ Console API """
    pass


async def web(text: str) -> str:
    """ Web API for grammar creating """
    bldr = Builder(
        'fake-path',
        make_text_loader(text),
        Parsers('base').get_parser()
    )
    return bldr.build()
