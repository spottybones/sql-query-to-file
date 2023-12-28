from click.testing import CliRunner
from sql_query_to_file.cli import cli
import pytest


@pytest.fixture(scope="session")
def runner():
    return CliRunner()


@pytest.fixture
def cli_arguments():
    return ["query.sql", "-"]


def test_cli_fails_without_arguments(runner):
    """test CLI fails when invoked without arguments"""
    result = runner.invoke(cli)
    assert result.exit_code != 0


def test_cli_required_arguments(runner, cli_arguments):
    """test that required arguments are provided"""
    with runner.isolated_filesystem():
        with open(cli_arguments[0], "w") as f:
            f.write("select * from table")

        result = runner.invoke(cli, cli_arguments)

    assert result.exit_code == 0, result.output


def test_cli_required_arguments_with_optional_sep(runner, cli_arguments):
    """test that required arguments are provided"""
    with runner.isolated_filesystem():
        with open(cli_arguments[0], "w") as f:
            f.write("select * from table")

        result = runner.invoke(cli, cli_arguments + ["--sep", "\t"])

    assert result.exit_code == 0
