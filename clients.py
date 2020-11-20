class Client:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name


class ClientBalance(Client):
    def __init__(self, balance=0, unit="руб."):
        self.balance = balance
        self.unit = unit

    def init_from_dict(self, dict):
        if isinstance(dict.get("first_name"), str):
            self.first_name = dict.get("first_name")
        if isinstance(dict.get("last_name"), str):
            self.last_name = dict.get("last_name")
        if dict.get("balance") >= 0 and isinstance(dict.get("balance"), int):
            self.balance = dict.get("balance")

    def balance_at_unit(self):
        return str(self.balance) + " " + self.unit

    def __str__(self):
        return f"клиент: {self.full_name()}, баланс: {self.balance_at_unit()}"


if __name__ == "__main__":
    test_client = ClientBalance()
    test_client.init_from_dict({"first_name": "Иван", "last_name": "Иванов", "balance": 1000})
    print(test_client)