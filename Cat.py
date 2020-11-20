class Cat:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict):
        if isinstance(cat_dict.get("name"), str):
            self.name = cat_dict.get("name")
        if cat_dict.get("gender") == "мальчик" or cat_dict.get("gender") == "девочка":
            self.gender = cat_dict.get("gender")
        if cat_dict.get("age") >= 0 and isinstance(cat_dict.get("age"), int):
            self.age = cat_dict.get("age")


if __name__ == "__main__":
    test_cat = Cat()
    test_cat.init_from_dict({"name": "Barsik", "gender": "мальчик", "age": 2})
    print(f'Name is {test_cat.name}. Gender is {test_cat.gender}. Age is {test_cat.age}.')
