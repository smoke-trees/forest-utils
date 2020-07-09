import os
import click
import pkg_resources
from pathlib import Path

from utils import create
from utils import pull

def get_version():
    with open(os.path.join('..','..', 'VERSION.txt')) as file:
        return file.read().split("==")[-1].strip()

INFORMATION = {
    'name': "forest",
    'version': get_version(),
}

@click.group(help='A CLI Tool for uploading model to model zoo')
@click.version_option(INFORMATION['version'])
@click.pass_context
def main(ctx):
    pass

@main.command(help='Initialize zoo repository')
@click.pass_context
def init(ctx):
    create.create_dir_tree()


@main.command(help='Pull models from model zoo')
@click.pass_context
@click.option('--all', '-a', is_flag=True, help="Pull all the files from the github origin")
def pull(ctx, docker):
    pull.get_files()

if __name__ == "__main__":
    main()
