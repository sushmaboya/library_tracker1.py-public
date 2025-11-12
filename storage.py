import json

class FileStorage:
    def __init__(self, filename="books.json"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
