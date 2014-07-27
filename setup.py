from distutils.core import setup

VERSION = '1.0.0-dev'

setup(
    name='sitedrifter',
    description="Sitedrifter is a Markdown to HTML converter to build "
                "static websites.",
    long_description="""
===========
Sitedrifter
===========

Sitedrifter is a Markdown to HTML converter to build static websites. It's an
enhanced version of the builder used in `Star drifter
project <https://github.com/brunobord/stardrifter>`_, hence the name.

Overview
--------

* Source files are in Markdown,
* You can build templates using Jinja2 syntax,
* Handling static files by copying `static` and `vendor` directories,
* Navigation handling via a JSON file,
* Fragment system: any snippet that has to be published more than once in the
  website can be put into a fragment and duplicated into the content,
* The ``drift`` binary tool has many options to customize source and build
  targets.

Install
-------

::

    pip install sitedrifter

Usage
-----

::

    drift init  # To start a site project
    drift build  # to build the website

License
-------

This is a MIT-licensed software, by Bruno Bord (c) 2014.

    """,
    url='https://github.com/brunobord/sitedrifter/',
    author="Bruno Bord",
    author_email='bruno@jehaisleprintemps.net',
    license="MIT",
    platforms='any',
    version=VERSION,
    install_requires=['Markdown', "Jinja2"],
    scripts=['bin/drift']
)
