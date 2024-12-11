from pathlib import Path


def read_markdown_file(markdown_file: str) -> str:
    """
    Reads a markdown file and returns the text content.

    Args:
        markdown_file (str): The path to the markdown file to read.

    Returns:
        str: The text content of the markdown file.
    """
    return Path(markdown_file).read_text()
