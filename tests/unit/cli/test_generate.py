from cookiecutter_autodocs.cli.app import app
import asyncio


def test_cli_generate_desc(typer_test_runner, cookiecutter_json_path, tmp_path):
    path = tmp_path / "cookiecutter.desc"
    result = typer_test_runner.invoke(app, ["generate", "desc", str(cookiecutter_json_path), "-o", str(path)])

    assert result.exit_code == 0
    assert "Generating a new cookiecutter.desc file" in result.stdout


def test_cli_generate_desc_no_output(typer_test_runner, cookiecutter_json_path, tmp_path):
    tmp_path / "cookiecutter.desc"
    result = typer_test_runner.invoke(app, ["generate", "desc", str(cookiecutter_json_path)])

    assert result.exit_code == 0
    assert "Generating a new cookiecutter.desc file" in result.stdout


def test_cli_generate_desc_update(typer_test_runner, cookiecutter_desc, cookiecutter_json_path, tmp_path):
    path = tmp_path / "cookiecutter.desc"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(path))
    result = typer_test_runner.invoke(app, ["generate", "desc", str(cookiecutter_json_path), "-o", str(path)])

    assert result.exit_code == 0
    assert "Updating an existing cookiecutter.desc file at" in result.stdout


def test_cli_generate_cookiecutter(typer_test_runner, cookiecutter_desc, tmp_path):
    desc_path = tmp_path / "cookiecutter.desc"
    json_path = tmp_path / "cookiecutter.json"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(desc_path))
    result = typer_test_runner.invoke(app, ["generate", "cookiecutter", str(desc_path), "-o", str(json_path)])

    assert result.exit_code == 0
    assert "Generating a new cookiecutter.json file " in result.stdout


def test_cli_generate_cookiecutter_no_output(typer_test_runner, cookiecutter_desc, tmp_path):
    desc_path = tmp_path / "cookiecutter.desc"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(desc_path))
    result = typer_test_runner.invoke(app, ["generate", "cookiecutter", str(desc_path)])

    assert result.exit_code == 0
    assert "Generating a new cookiecutter.json file " in result.stdout


def test_cli_generate_cookiecutter_update(typer_test_runner, cookiecutter_desc, cookiecutter_json_path, tmp_path):
    desc_path = tmp_path / "cookiecutter.desc"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(desc_path))
    result = typer_test_runner.invoke(
        app, ["generate", "cookiecutter", str(desc_path), "-o", str(cookiecutter_json_path)]
    )

    assert result.exit_code == 0
    assert "Updating an existing cookiecutter.json file at " in result.stdout


def test_cli_generate_markdown(typer_test_runner, cookiecutter_desc, tmp_path):
    desc_path = tmp_path / "cookiecutter.desc"
    asyncio.run(cookiecutter_desc.to_cookiecutter_desc(desc_path))
    result = typer_test_runner.invoke(app, ["generate", "markdown", str(desc_path)])

    assert result.exit_code == 0
