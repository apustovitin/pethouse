from geometry import Rectangle, Square, Circle

figures = [Rectangle(3, 4), Rectangle(12, 5), Square(5), Square(10), Circle(5), Circle(6)]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())