#!/usr/bin/env python

from pathlib import Path
import os

import click

CWD = Path(__file__).parents[1]
click.echo(CWD)

@click.group()
def cli():
    pass

@click.command('clone')
@click.argument('url')
@click.argument('dest', default='')
def clone(url, dest):
    cmd = f"make -f {CWD / 'Makefile'} clone url={url} dest={dest}"
    click.echo(cmd)
    os.system(cmd)

@click.command()
def pull():
    cmd = f"make -f {CWD / 'Makefile'} pull"
    click.echo(cmd)
    os.system(cmd)

cli.add_command(clone)
cli.add_command(pull)

if __name__ == '__main__':
    cli()
