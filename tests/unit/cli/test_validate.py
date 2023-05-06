from cookiecutter_autodocs.cli.app import app
from cookiecutter_autodocs.schemas.description import CookieCutterDescription
import asyncio


def test_cli_validate(typer_test_runner, cookiecutter_json_path, cookiecutter_desc, tmp_path):
    path = tmp_path / "cookiecutter_desc"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(path))
    result = typer_test_runner.invoke(app, ["validate", str(path), str(cookiecutter_json_path)])

    assert result.exit_code == 0
    assert "Validation succeeded" in result.stdout


def test_cli_validate_no_json_path(typer_test_runner, cookiecutter_json_path, cookiecutter_desc, tmp_path):
    path = tmp_path / "cookiecutter_desc"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(path))
    result = typer_test_runner.invoke(app, ["validate", str(path)])

    assert result.exit_code == 0
    assert "Validation succeeded" in result.stdout


def test_cli_validate_fails(typer_test_runner, cookiecutter_json_path, tmp_path):
    path = tmp_path / "cookiecutter_desc"

    asyncio.run(CookieCutterDescription(variables={}).to_cookiecutter_desc(path))
    result = typer_test_runner.invoke(app, ["validate", str(path), str(cookiecutter_json_path)])

    assert result.exit_code == 1
    assert "Validation failed:" in result.stdout
