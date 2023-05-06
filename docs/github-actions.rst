Github Actions
##############

.. _github-actions-label:

cookiecutter-autodocs offers a Github Action you can use with your project.


Github Actions Quickstart
*************************

You can use the Github Action by adding the following to your ``.github/workflows/`` directory:

.. code-block: yaml

      name: Autodocs

      on:
         push:

      jobs:
         build:
         runs-on: ubuntu-latest
         steps:
            - uses: actions/checkout@v2
            - name: Validate a cookiecutter.desc
              uses: andrewthetechie/cookiecutter-autodocs@v1
              with:
                  action: validate
                  cookiecutter_desc: cookiecutter.desc

You can use any of the `CLI Commands <cli-label>` by changing the ``action`` parameter.


Generated Docs
**************

<!-- action-docs-description -->
## Description

Generate docs for a cookiecutter template's inputs.


<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| - | - | - | - |
| action | What action to take with this action. One of validate, generate-desc, generate-cookiecutter, or generate-markdown | `false` | validate |
| cookiecutter_desc_file_path | Path to the cookiecutter.desc file | `false` | cookiecutter.desc |
| cookiecutter_json_file_path | Path to your the cookiecutter.desc file | `false` | cookiecutter.json |
| allow_empty_descriptions | Whether to allow an entry in cookiecutter.desc to have an empty description (blank string) when validating | `false` | false |



<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `docker` action.


<!-- action-docs-runs -->
