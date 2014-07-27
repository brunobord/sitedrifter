# Sitedrifter

Sitedrifter is a Markdown to HTML converter to build static websites. It's an enhanced version of the builder used in [Star drifter project](https://github.com/brunobord/stardrifter), hence the name.

## Install

Via pip, in a virtualenv, for example:

    pip install sitedrifter

Or simply clone this repository and install it in dev mode:

    git clone https://github.com/brunobord/sitedrifter.git
    cd sitedrifter
    pip install -e ./

You may now have access to the binary ``drift``.

```shell
$ drift --version
version 1.0-dev
```

## Usage

### Create a projet

```shell
$ mkdir new_project
$ cd new_project
$ drift init
```

### Edit your pages

Your markdown files live in the ``src/`` directory. Edit as many files as you want, using *.md*, *.markdown* or *.mkd* extension.

If a snippet (or an extract) of your content is used several times in your content, simply create a fragment.

```shell
$ cd src/
$ mkdir fragments
$ cd fragments
$ echo "Used several times" > frag1.md
```

As of now, anytime you want to include this snippet in your content, just use the specific markup:

```markdown
Here is my content...

~~frag1~~

Now there is the rest of your content.
```

You may also want to customise your web pages, add CSS and Javascripts files. You'll have two directories that will be duplicated in your build directory: ``static`` and ``vendor``.

### Build a project

The following command will build your pages and put them in the build directory, along with the statics.

```
$ drift build
```

### Options

Here are the various optional arguments with their default value.

* ``--source-dir`` ("src/"): Source directory, where the markdown content is written
* ``--build-dir`` ("build/"): Directory where the web content is built
* ``--static-dir`` ("static/"): Directory where one can find the static files (JS, CSS, Images)
* ``--vendor-dir`` ("vendor/"): Directory where one can find static files (JS, CSS, Images), but coming from externale resources (external libs)
* ``--template-dir`` ("templates/"): Template directory, where we can find Jinja2 files
* ``--template-name`` ("base.html"): Base template name
* ``--navigation-file`` ("navigation.json"): Navigation file name (or full path)
* ``--root-name`` ("index"): The name of your root page (the home page)

----

## About

Sitedrifter is (c) 2014 Bruno Bord - This code is published under the terms of the MIT License. See the LICENSE file for more information.
