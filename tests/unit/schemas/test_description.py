from cookiecutter_autodocs.schemas.description import CookieCutterDescription
from cookiecutter_autodocs.schemas.description import VariableDescription
from cookiecutter_autodocs.lib import files
import random
from copy import deepcopy

import pytest


@pytest.mark.asyncio
async def test_variable_description():
    """Test VariableDescription"""
    var_desc = VariableDescription(name="test", description="Test variable", default="test", type="str")
    assert var_desc.name == "test"
    assert var_desc.description == "Test variable"
    assert var_desc.default == "test"
    assert var_desc.type == "str"
    assert var_desc.required is False


@pytest.mark.asyncio
async def test_variable_description_not_required():
    var_desc = VariableDescription(
        name="test",
        description="Test variable",
        default="",
    )
    assert var_desc.name == "test"
    assert var_desc.description == "Test variable"
    assert var_desc.type == "str"
    assert var_desc.required is True


@pytest.mark.asyncio
async def test_variable_description_set_type():
    var_desc = VariableDescription(
        name="test",
        description="Test variable",
        default="str",
    )
    assert var_desc.name == "test"
    assert var_desc.description == "Test variable"
    assert var_desc.type == "str"


def test_cookiecutter_desription_cookiecutter_json(cookiecutter_desc):
    """Test CookieCutterDescription.cookiecutter_json"""
    json = cookiecutter_desc.cookiecutter_json

    for key, value in json.items():
        assert value == cookiecutter_desc.variables[key].default


def test_cookiecutter_desription_cookiecutter_desc_dict(cookiecutter_desc_dict):
    """Test CookieCutterDescription.cookiecutter_json"""
    desc = CookieCutterDescription(variables=cookiecutter_desc_dict)

    assert cookiecutter_desc_dict == desc.cookiecutter_desc_dict


@pytest.mark.asyncio
async def test_cookiecutter_description_from_cookiecutter_json(subtests, cookiecutter_json, cookiecutter_json_path):
    """Test CookieCutterDescription.from_cookiecutter_json"""
    desc = await CookieCutterDescription.from_cookiecutter_json(cookiecutter_json_path)

    for key, value in cookiecutter_json.items():
        with subtests.test(msg=f"{key}", key=key):
            assert desc.variables[key].name == key
            assert desc.variables[key].default == value
            assert desc.variables[key].type == type(value).__name__
            assert desc.variables[key].description == ""


@pytest.mark.asyncio
async def test_cookiecutter_description_to_cookiecutter_json(cookiecutter_json_path, tmp_path):
    """Test CookieCutterDescription.to_cookiecutter_json"""
    desc = await CookieCutterDescription.from_cookiecutter_json(cookiecutter_json_path)
    json_path = tmp_path / "cookiecutter.json"
    await desc.to_cookiecutter_json(json_path)

    cookiecutter_data = await files.load_cookiecutter_json(json_path)
    assert cookiecutter_data == desc.cookiecutter_json


@pytest.mark.asyncio
async def test_cookiecutter_description_from_cookiecutter_desc(cookiecutter_desc, tmp_path):
    path = tmp_path / "cookiecutter_desc"
    await cookiecutter_desc.to_cookiecutter_desc(path)
    loaded_desc = await CookieCutterDescription.from_cookiecutter_desc(path)
    assert cookiecutter_desc == loaded_desc


def test_cookiecutter_description_update_empty(cookiecutter_desc):
    existing_desc = CookieCutterDescription(variables={})
    existing_desc.update(cookiecutter_desc)
    for key, value in cookiecutter_desc.variables.items():
        assert existing_desc.variables[key] == value


def test_cookiecutter_description_update(cookiecutter_desc):

    # get three unique random variables from cookiecutter_desc
    variables_copy = deepcopy(cookiecutter_desc.variables)
    variable1 = cookiecutter_desc.variables[random.choice(list(variables_copy.keys()))]
    del variables_copy[variable1.name]
    variable2 = cookiecutter_desc.variables[random.choice(list(variables_copy.keys()))]

    variable1.description = "Updated description"
    variable2.default = "Updated default"

    existing_desc = CookieCutterDescription(variables={variable1.name: variable1, variable2.name: variable2})
    existing_desc.update(cookiecutter_desc)
    for key, value in cookiecutter_desc.variables.items():
        assert existing_desc.variables[key] == value


def test_cookiecutter_description_update_overwrite_empty_description():
    existing_desc = CookieCutterDescription(
        variables={"test": VariableDescription(name="test", description="", default="test", type="str")}
    )

    update_desc = CookieCutterDescription(
        variables={"test": VariableDescription(name="test", description="Test variable", default="test", type="str")}
    )

    existing_desc.update(update_desc)
    assert existing_desc.variables["test"].description == "Test variable"


def test_cookiecutter_description_validate_cookiecutter_json_ok(cookiecutter_desc):
    """Test CookieCutterDescription.validate_cookiecutter_json"""
    result, errors = cookiecutter_desc.validate_cookiecutter_json(cookiecutter_desc.cookiecutter_json)
    assert result
    assert errors == []


def test_cookiecutter_description_validate_missing_keys(subtests):
    """Test CookieCutterDescription.validate_cookiecutter_json"""
    cookiecutter_desc = CookieCutterDescription(
        variables={"test": VariableDescription(name="test", description="Test variable", default="test", type="str")}
    )

    with subtests.test(msg="Missing key in cookiecutter.json"):
        result, errors = cookiecutter_desc.validate_cookiecutter_json({})
        assert result is False
        assert errors == ["Variable test is not in the cookiecutter.json file"]

    with subtests.test(msg="Missing key in cookiecutter.desc"):
        result, errors = cookiecutter_desc.validate_cookiecutter_json({"test": "test", "not_test": "test"})
        assert result is False
        assert errors == ["Variable not_test is not in the cookiecutter.desc file"]


def test_cookiecutter_description_validate_missing_description(subtests):
    """Test CookieCutterDescription.validate_cookiecutter_json"""
    cookiecutter_desc = CookieCutterDescription(
        variables={"test": VariableDescription(name="test", description="", default="test", type="str")}
    )

    with subtests.test(msg="Missing description in cookiecutter.desc"):
        result, errors = cookiecutter_desc.validate_cookiecutter_json({"test": "test"})
        assert result is False
        assert errors == ["Variable test has an empty description"]

    with subtests.test(msg="Allow Missing description in cookiecutter.desc"):
        result, errors = cookiecutter_desc.validate_cookiecutter_json({"test": "test"}, allow_empty_desc=True)
        assert result is True
        assert errors == []


def test_cookiecutter_description_validate_type_mismatch(subtests):
    """Test CookieCutterDescription.validate_cookiecutter_json"""
    cookiecutter_desc = CookieCutterDescription(
        variables={
            "test": VariableDescription(name="test", description="Test variable", default="test", type="string")
        }
    )

    result, errors = cookiecutter_desc.validate_cookiecutter_json({"test": 1})
    assert result is False
    assert "Variable test has type int in cookiecutter.json, but type string in cookiecutter.desc" in errors
    assert "Variable test has default 1 in cookiecutter.json, but default test in cookiecutter.desc" in errors
