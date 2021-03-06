from unittest.mock import patch
from signal_interpreter_server.main import main, ArgumentParser, parse_arguments
from signal_interpreter_server.routes import JsonParser, signal_interpreter_app

# pylint: disable=missing-function-docstring, missing-class-docstring, missing module docstring


class MockArguments:
    file_path = "path/to/file"


@patch.object(ArgumentParser, 'parse_args', return_value=MockArguments)
@patch.object(ArgumentParser, 'add_argument')
def test_parse_argument(mock_add_argument, mock_parse_args):
    assert parse_arguments() == MockArguments
    mock_add_argument.assert_called_with('--file_path')
    mock_parse_args.assert_called_once()


@patch.object(signal_interpreter_app, 'run')
@patch.object(JsonParser, 'load_file')
@patch('signal_interpreter_server.main.parse_arguments', return_value=MockArguments)
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    main()
    mock_parse_arguments.assert_called_once()
    mock_load_file.assert_called_with(MockArguments.file_path)
    mock_run.assert_called_once()
