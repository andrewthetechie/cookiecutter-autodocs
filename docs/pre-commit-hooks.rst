Pre-commit Hooks
################

.. _pre-commit-hooks-label:

cookiecutter autodocs offers two pre-commit hooks to use in your project:

- `cookiecutter-autodocs-generate`: Will generate a cookiecutter.json for any cookiecutter.desc in the commit/repo. Assumes the cookiecutter.json is in the same directory as the cookiecutter.desc. Useful to automatically sync changes from your cookiecutter.desc to your cookiecutter.json on commit.
- `cookiecutter-autodocs-validate`: Validates cookiecutter.desc/json combos. Assumes the files live next to each other in a directory. See `Validation <validation-label>` for more info on validation

Pre-commit Quickstart
*********************

To use cookiecutter autodocs with pre-commit, add the following to your .pre-commit-config.yaml:

.. code-block:: yaml

    - repo: https://github.com/andrewthetechie/cookiecutter-autodocs
      # Pick a tag or sha to point at, or use latest
      rev: latest
      hooks:
        - id: cookiecutter-autodocs-generate
        - id: cookiecutter-autodocs-validate
