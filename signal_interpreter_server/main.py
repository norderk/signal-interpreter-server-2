#main pogram file
"""Use argparse to make it possible to run main.py with the argument --file_path
where you can specify the path to the signal database file"""

"""Import the JsonParser-instance from routes.py to main.py so you can use that 
instance for loading the file in the main-function. You do this by typing: 
"""
from argparse import ArgumentParser
from signal_interpreter_server.routes import signal_interpreter_app, json_parser


#file_path = '/signal_interpreter_server/signal_database.json'
#with open("C:/Users/enordqv1/PyCourse/my-python-project/signal_database.json") as json_file:
#    test = json.load(json_file)

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--file_path')
    return parser.parse_args()

"""Call the main()-function from an if-statement verifying 
that you are running the program from that particular file"""
def main():
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    signal_interpreter_app.run()

if __name__ == "__main__":
    main()
