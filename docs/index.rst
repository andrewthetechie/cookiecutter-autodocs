
cookiecutter-autodocs
=====================

Generate docs from a cookiecutter template. Pre-commit hook and github-action

Why?
----

`Cookiecutter <https://cookiecutter.readthedocs.io/en/stable/>`_ is a powerful tool to create templates for all sorts of projects, but
one of its downsides is it relies on a plain JSON file for its input (cookiecutter.json). Because JSON does not allow comments, you cannot
document your inputs without writing the documentation separately.

cookiecutter-autodocs allows you to write your Cookiecutter's input as a Toml file, cookiecutter.desc. In this file you can add defaults, info about the variable type,
and a description of each variable.

An example cookiecutter.desc

.. code-block:: toml

   [project_slug]
   default = "new_project"
   description = "The name of the project."
   type = "string"

   [python_version]
   default = "3.11.2"
   description = "What python version to use with this project"
   type = "string"

   [dev_requirements]
   default = []
   description = "What dev requirements does this project have"
   type = "list(string)"

   [author]
   default = ""
   description = "Who's the author?"
   type = "string"

This would generate into the following cookiecutter.json

.. code-block:: json

   {
       "project_slug": "new_project",
       "python_version": "3.11.2",
       "dev_requirements": [],
       "author": ""
   }

You can then use this ``cookiecutter.desc`` file to generate a ``cookiecutter.json`` file for your template as well as additional documentation, like a markdown table

.. code-block:: shell

   cookiecutter-autodocs generate markdown cookiecutter.desc

   +-----------------------------------------------------------------------------------------------+
   |      name      |                 description                |  default  |    type    |required|
   +----------------+--------------------------------------------+-----------+------------+--------+
   |  project_slug  |          The name of the project.          |new_project|   string   |  False |
   +----------------+--------------------------------------------+-----------+------------+--------+
   | python_version |What python version to use with this project|   3.11.2  |   string   |  False |
   +----------------+--------------------------------------------+-----------+------------+--------+
   |dev_requirements|What dev requirements does this project have|     []    |list(string)|  False |
   +----------------+--------------------------------------------+-----------+------------+--------+
   |     author     |              Who's the author?             |           |   string   |  True  |
   +-----------------------------------------------------------------------------------------------+

Installation
------------

Install the package using your favorite python package manager

.. code-block:: shell

   pip install cookiecutter-autodocs
   or
   pipx install cookiecutter-autodocs

The package is available on _pypi: https://pypi.org/project/cookiecutter-autodocs/.

Cookiecutter-autodocs can also be used with _docker: https://hub.docker.com/r/andrewthetechie/cookiecutter-autodocs, or in Github Actions or pre-commit.

.. toctree::
   :maxdepth: 2

   quickstart
   validation
   pre-commit-hooks
   github-actions
   cli
   development
   module


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
