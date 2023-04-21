# https://en.wikipedia.org/wiki/Comparison_of_executable_file_formats

import importlib.metadata
import sys

from surfactant.cmd.generate import sbom as generate

import click


@click.group()
def main():
    pass

@click.command("version")
def version():
    """Print version information."""
    click.echo(importlib.metadata.version("surfactant"))
    sys.exit(0)

main.add_command(generate)
main.add_command(version)

if __name__ == "__main__":
    main()
