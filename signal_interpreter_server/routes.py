"""Signal Interpreter Server: parses the attached file signal_database.json.
A POST-request to the server (containing a signal ID) looks up that ID in the signal database and
return the signal title."""

from flask import Flask, request, jsonify
from signal_interpreter_server.json_parser import JsonParser


# global_instances
signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


# @signal_interpreter_app.route("/", methods=["GET"])
# def server_function():
#     # choice_from = json_parser.load_file()
#     # choice_from = jsonify(choice_from)
#     # return choice_from
#     return 'This is the shit!'


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():

    data = request.get_json()
    ecu_resp = json_parser.get_signal_title(data['signal'])
    return_json = jsonify(ecu_resp)
    return return_json
