import os
import codecs

from setuptools import setup, find_packages

REQUIREMENTS = ['gdown==3.11.1', 'requests==2.24.0', 'tensorflow', 'spacy', 'pandas']

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

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name="forest_utils",
        version=get_version('VERSION.txt'),
        description="Package for SmokeTrees model zoo",
        long_description=get_long_description(),
        url="https://github.com/smoke-trees/forest-utils",
        author="SmokeTrees",
        author_email=" info@smoketrees.dev",
        python_requires='>=3.4',
        packages=find_packages(include=[
            "forest_utils"
            "forest_utils.*"
        ], exclude=["test.*, test"]),
        include_package_data=True,
           classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
        install_requires=REQUIREMENTS,
        keywords='utils package modelzoo'
)