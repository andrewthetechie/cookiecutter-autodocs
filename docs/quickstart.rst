Quick Start
###########


Writing a cookiecutter.desc
***************************

A cookiecutter.desc is a TOML document that describes the cookiecutter.json you want to produce with it. An example might look like this:

.. code-block:: toml

   [project_slug]
   description="The project's slug"
   default = ""
   type = "str"

   [python_version]
   default = "3.11.2"
   description = "What python version to use with this project"
   type = "str"

   [author]
   default = ""
   description = "Who's the author?"
   type = "str"

   [number]
   default = 7
   description = "Just a number"
   type = "int"

   [_extensions]
   default = ["mycustom.JinjaExtension"]
   description = "Extensions for this template"
   type = "list"

With this cookiecutter.desc, you can generate a cookiecutter.json file for your template.

.. code-block:: shell

   cookiecutter-autodocs generate cookiecutter cookiecutter.desc
   Generated cookiecutter.json from cookiecutter.desc

   cat cookiecutter.json
   {
      "project_slug": "",
      "python_version": "3.11.2",
      "author": "",
      "number": 7
      "_extensions": ["mycustom.JinjaExtension"]
   }

Generating a cookiecutter.desc from an existing template
========================================================

cookiecutter-autodocs can also generate a new cookiecutter.desc from a cookiecutter.json.

.. code-block:: shell

   cookiecutter-autodocs generate desc cookiecutter.json
   Generating a new cookiecutter.desc file at cookiecutter.desc
   Generated cookiecutter.desc from cookiecutter.json

   cat cookiecutter.desc
   [project_slug]
   description = ""
   default = ""
   type = "str"
   required = true

   [python_version]
   description = ""
   default = "3.11.2"
   type = "str"
   required = false

   [author]
   description = ""
   default = ""
   type = "str"
   required = true

   [number]
   description = ""
   default = 7
   type = "int"
   required = false

   [_extensions]
   default = ["mycustom.JinjaExtension"]
   description = ""
   type = "list"

You can then fill in descriptions for each variable and use the ``cookiecutter.desc`` to keep the ``cookiecutter.json`` up to date as the template changes. cookiecutter-autodocs will always try to update an existing desc or json file

Generating markdown from a cookiecutter.desc
============================================

**Note: This feature is still in development.**

cookiecutter-autodocs can also generate markdown documentation from a cookiecutter.desc. This is useful for keeping documentation up to date as the template changes.

.. code-block:: shell

   cookiecutter-autodocs generate markdown cookiecutter.desc
   ```
   +--------------------------------------------------+
   |      name      |description|default|type|required|
   +----------------+-----------+-------+----+--------+
   |  project_slug  |           |       | str|  True  |
   +----------------+-----------+-------+----+--------+
   | python_version |           | 3.11.2| str|  False |
   +----------------+-----------+-------+----+--------+
   |dev_requirements|           |   []  |list|  False |
   +----------------+-----------+-------+----+--------+
   |     author     |           |       | str|  True  |
   +----------------+-----------+-------+----+--------+
   |     number     |           |   7   | int|  False |
   +--------------------------------------------------+```


Pre-commit and Github Actions
==============================

cookiecutter-autodocs also offers a `Github Action <github-actions-label>`_ and `Pre-commit hooks <pre-commit-hooks-label>`_ to use in your projects.
