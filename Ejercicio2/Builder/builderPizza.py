from Builder.builder import Builder
from Builder.agregarPizza import AgregarPizza

class BuilderPizza(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = AgregarPizza()

    @property
    def pizza(self) -> AgregarPizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def produce_masa(self) -> None:
        self._pizza.add("Fina")

    def produce_salsa(self) -> None:
        self._pizza.add("Tomate")

    def produce_queso(self) -> None:
        self._pizza.add("Mozarella")
    
    def produce_ingrediente1(self) -> None:
        self._pizza.add("Peperoni")    
        
    def produce_ingrediente2(self) -> None:
        self._pizza.add("Cebolla")    
    
    def produce_ingrediente3(self) -> None:
        self._pizza.add("Aceitunas")

    def produce_coccion(self) -> None:
        self._pizza.add('Horno')

    def produce_presentacion(self) -> None:
        self._pizza.add('Caja de cartón') 

    def produce_maridaje(self) -> None:
        self._pizza.add('Cerveza')

    def produce_extras(self) -> None:
        pass