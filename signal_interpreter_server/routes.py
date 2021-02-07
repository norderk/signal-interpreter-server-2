#routes

#imports
from flask import Flask, request, jsonify
from signal_interpreter_server.json_parser import JsonParser

#global_instances
signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()

""" add some functionality to the Signal Interpreter Server so it can parse the 
attached file signal_database.json. When sending a POST-request to the server 
containing a signal ID, it should look up that ID in the signal database and 
return the signal title."""

"""Create a global instance of JsonParser in routes.py, in the same way as signal_interpreter_app. 
You do this by just typing: json_parser = JsonParser() in the beginning of the file."""


@signal_interpreter_app.route("/", methods=["GET"])
def server_function():
    #choice_from = json_parser.load_file()
    #choice_from = jsonify(choice_from)
    #return choice_from
    return 'This is the shit!'

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    ECU_resp = json_parser.get_signal_title(data['signal'])
    return_json = jsonify(ECU_resp)
    return return_json


