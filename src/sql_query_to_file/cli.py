"""
Command line interface / script entry
"""

import click


@click.command()
@click.argument(
    "query_file", type=click.Path(exists=True, dir_okay=False, allow_dash=True)
)
@click.argument("output", type=click.File("wb"))
@click.option("-s", "--sep", type=str, help="Optional separator if not comma")
def cli(query_file, output, sep):
    if sep:
        pass
