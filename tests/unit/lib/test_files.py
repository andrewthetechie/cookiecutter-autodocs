import random
import string
from cookiecutter_autodocs.lib import files
from pathlib import Path

import pytest


@pytest.mark.asyncio
async def test_load_cookiecutter_json(cookiecutter_json, cookiecutter_json_path):
    cookiecutter_data = await files.load_cookiecutter_json(cookiecutter_json_path)
    assert cookiecutter_data == cookiecutter_json

    # test we convert a string to a path properly
    cookiecutter_data_from_str = await files.load_cookiecutter_json(str(cookiecutter_json_path))
    assert cookiecutter_data_from_str == cookiecutter_json


@pytest.mark.asyncio
async def test_load_cookiecutter_json_missing_file():
    rand1 = "".join(random.choice(string.ascii_letters) for i in range(10))
    rand2 = "".join(random.choice(string.ascii_letters) for i in range(10))
    test_path = f"./{rand1}/{rand2}/cookiecutter.json"
    assert Path(test_path).exists() is False
    with pytest.raises(FileNotFoundError):
        await files.load_cookiecutter_json(test_path)


@pytest.mark.asyncio
async def test_load_cookiecutter_description_missing_file():
    rand1 = "".join(random.choice(string.ascii_letters) for i in range(10))
    rand2 = "".join(random.choice(string.ascii_letters) for i in range(10))
    test_path = f"./{rand1}/{rand2}/cookiecutter_desc"
    assert Path(test_path).exists() is False
    with pytest.raises(FileNotFoundError):
        await files.load_cookiecutter_description(test_path)
