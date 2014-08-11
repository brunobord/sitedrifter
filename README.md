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

## Template

Sitedrifter builds the pages using a Jinja2-based template. Along with the content, according to the context, it injects useful variables into the template, so you can use them in your templates.


* ``path_prefix``: when you're on the root page, it's "." but when you're in a deeper page, it's the relative path (such as: ".."),
* ``root_name``: It's the name of the root page, as defined in the ``--root-name`` option,
* ``date``: the current date and time. (a.k.a. "now"),
* ``navigation``: the content of the ``navigation.json`` file, serialized to be used by the navigation loop.
* ``current``: the current name of the page,

### Navigation

This file should be a JSON list. Here is an example:

```json
[
    {"caption": "Prepare"},
    {"url": "other", "caption": "See Other sections"},
    {"url": "", "caption": "Adventure", "children": [
        {"url": "marketplace", "caption": "Marketplace"},
        {"url": "travel", "caption": "Space Travel"}
    ]}
]
```

When there's not URL, the navigation item will be interpreted as a simple non-interactive list item. It'll be used as a section title.

When you define children, they'll be used as a sub-navigation item list.

----

## About

Sitedrifter is (c) 2014 Bruno Bord - This code is published under the terms of the MIT License. See the LICENSE file for more information.
