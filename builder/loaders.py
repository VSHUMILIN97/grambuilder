from pathlib import Path


def make_text_loader(text: str):
    """ Create text loader for builder, that does not use path at all, since
        data already retrieved
    """
    def test_loader(_path: Path) -> str:
        return text
    return test_loader
