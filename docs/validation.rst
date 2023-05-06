Validation
################

.. _validation-label:

cookiecutter autodocs has a validation command that runs some rules against your cookiecutter.desc and cookiecutter.json.


.. code-block:: shell

    Usage: cookiecutter-autodocs validate [OPTIONS] COOKIECUTTER_DESC
                                        [COOKIECUTTER_JSON]

    ╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ *    cookiecutter_desc      PATH                 Path to the cookiecutter.desc file [default: None] [required]                                                              │
    │      cookiecutter_json      [COOKIECUTTER_JSON]  Path to the cookiecutter.json file. If not specified, the cookiecutter.json will be read from the same directory as the    │
    │                                                  cookiecutter.desc file                                                                                                     │
    │                                                  [default: None]                                                                                                            │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ --allow-empty-description    --no-allow-empty-description      Allow empty descriptions. If not set, an empty description will cause an error.                              │
    │                                                                [default: no-allow-empty-description]                                                                        │
    │ --help                                                         Show this message and exit.                                                                                  │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

    $ cookiecutter-autodocs validate cookiecutter.desc

    Validation succeeded

    $ echo $?
    0


Validation Rules
****************

These rules are currently very basic. If you have ideas for additional rules, please open an issue or a pull request.

- The description must not be empty (unless ``--allow-empty-description`` is specified)
- Every key in the cookiecutter.desc must exist in the cookiecutter.json and vice versa
- Values in the cookiecutter.json must be of the same type as in the cookiecutter.desc and must match
