from person import Person

class Volunteer(Person):
    def __init__(self, settlement_type="г.", settlement_name="", status=""):
        self.settlement_type = settlement_type
        self.settlement_name = settlement_name
        self.status = status

    def set_settlement_name(self, settlement_name):
        if isinstance(settlement_name, str):
            self.settlement_name = settlement_name

    def set_status(self, status):
        if isinstance(status, str):
            self.status = status

    def init_from_dict(self, dict):
        self.set_first_name(dict.get("first_name"))
        self.set_last_name(dict.get("last_name"))
        self.set_settlement_name(dict.get("settlement_name"))
        self.set_status(dict.get("status"))

    def settlement(self):
        return self.settlement_type + " " + self.settlement_name

    def __str__(self):
        return f"{self.full_name()}, {self.settlement()}, статус: {self.status}"


class FeastGuest(Volunteer):
    pass


if __name__ == "__main__":
    test_guest = FeastGuest()
    test_guest.init_from_dict({"first_name": "Иван", "last_name": "Иванов",
                               "settlement_name": "Москва", "status": "Наставник"})
    print(test_guest)
