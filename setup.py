from distutils.core import setup

VERSION = '1.0-dev'

if __name__ == '__main__':
    setup(
        name='sitedrifter',
        version=VERSION,
        install_requires=['Markdown', "Jinja2"],
        scripts=['bin/drift']
    )
