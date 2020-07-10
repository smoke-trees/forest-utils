import os
import re
import codecs

from setuptools import setup

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="forest-utils",
    version=get_version('VERSION.txt'),
    author="Smoketrees",
    author_email=" info@smoketrees.dev",
    install_requires=[
        'gdown==3.11.1',
        'requests==2.24.0',
        'tensorflow',
        'spacy==2.2.0',
        'pandas',
        'click',
        'transformers',
        'torch'
    ],
)