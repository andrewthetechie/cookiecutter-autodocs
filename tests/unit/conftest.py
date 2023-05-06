import json
from cookiecutter_autodocs.schemas import VariableDescription
from cookiecutter_autodocs.schemas.description import CookieCutterDescription
import pytest
from ruamel.yaml import YAML

yaml = YAML(typ="safe")


@pytest.fixture
def cookiecutter_json():
    return {
        "project_slug": "test-project",
        "name": "Test Project",
        "description": "A test project",
        "author": "Test Author",
        "email": "testemail@email.com",
        "version": "0.1.0",
        "year": "2020",
        "license": "MIT",
        "value_with_empty_default": "",
        "integer": 1,
        "boolean": True,
        "list": ["a", "b", "c"],
        "dict": {"a": 1, "b": 2, "c": 3},
        "float": 1.0,
        "list_of_dicts": [{"a": 1}, {"b": 2}, {"c": 3}],
        "dict_of_lists": {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]},
    }


def _dumped_fixture(path, dumper, dumper_kwargs, obj):
    with open(path, "w") as fh:
        dumper(obj, fh, **dumper_kwargs)

    return path


@pytest.fixture
def cookiecutter_json_path(cookiecutter_json, tmp_path):
    yield _dumped_fixture(tmp_path / "cookiecutter.json", json.dump, {}, cookiecutter_json)


@pytest.fixture
def cookiecutter_desc_dict(cookiecutter_json):
    return {
        key: VariableDescription(name=key, default=value, description="Test")
        for key, value in cookiecutter_json.items()
    }


@pytest.fixture
def cookiecutter_desc(cookiecutter_desc_dict):
    return CookieCutterDescription(variables=cookiecutter_desc_dict)


@pytest.fixture
def typer_test_runner():
    from typer.testing import CliRunner

    return CliRunner()
