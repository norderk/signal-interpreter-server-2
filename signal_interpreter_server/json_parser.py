"""class with the two methods load_file and get_signal_title"""

import json


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        with open(file_path, 'r') as json_file:
            self.data = json.load(json_file)
            print(self.data)

    def get_signal_title(self, identifier):
        for item in self.data['services']:
            if identifier == item['id']:
                return item['title']
        return print('No matching events in database')


# test = JsonParser()
# print(test.load_file(), test.get_signal_title('11'))
