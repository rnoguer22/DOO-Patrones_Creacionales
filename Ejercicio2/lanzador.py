from Builder.director import Director
from Builder.builderPizza import BuilderPizza

class Lanzador():
    def __init__(self) -> None:
        pass

    def lanzar(self) -> None:
        director = Director()
        builder = BuilderPizza()
        director.builder = builder

        print("Pizza: ")
        director.build_pizza()
        builder.pizza.list_parts()