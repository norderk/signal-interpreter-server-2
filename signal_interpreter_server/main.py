"""Main contains to functions, 1. parse_arguments:  make it possible to run main.py
with the argument --file_path where you can specify the path to the signal database file
2. main: runs json_parser and signal_interpreter"""

from argparse import ArgumentParser
from signal_interpreter_server.routes import signal_interpreter_app, json_parser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--file_path')
    return parser.parse_args()


def main():
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    signal_interpreter_app.run()


if __name__ == "__main__":
    main()
