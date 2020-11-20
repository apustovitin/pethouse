class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name(self, first_name):
        if isinstance(first_name, str):
            self.first_name = first_name

    def set_last_name(self, last_name):
        if isinstance(last_name, str):
            self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name
