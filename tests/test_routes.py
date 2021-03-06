from unittest.mock import patch
from signal_interpreter_server.routes import signal_interpreter_app, JsonParser

# pylint: disable=missing-function-docstring, missing-class-docstring, Missing module docstring


def test_interpreter_signal():
    signal_interpreter_app.testing = True
    signal_interpreter_app_instance = signal_interpreter_app.test_client()

    with patch.object(JsonParser, 'get_signal_title', return_value='ECU Reset') as mock_get_signal_title:
        with signal_interpreter_app_instance as client:
            payload = {'signal':'11'}
            response = client.post('/', json=payload)
            mock_get_signal_title.assert_called_with('11')
            assert response.get_json() == 'ECU Reset'
