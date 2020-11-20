from Cat import Cat
cats_list = [
    {"name": "Барон", "gender": "мальчик", "age": 2},
    {"name": "Сэм", "gender": "мальчик", "age": 2}
]

for cat_dict in cats_list:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat_dict)
    print(f'Name is {cat_obj.name}. Gender is {cat_obj.gender}. Age is {cat_obj.age}.')
