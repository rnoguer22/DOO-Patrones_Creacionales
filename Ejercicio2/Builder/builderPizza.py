from Builder.builder import Builder
from Builder.agregarPizza import AgregarPizza

class BuilderPizza(Builder):
    def __init__(self, orden) -> None:
        self.reset()
        #Vamos a crear la pizza con la orden del pedido que nos llega a traves de la GUI
        self.orden = orden

    def reset(self) -> None:
        self._pizza = AgregarPizza()

    @property
    def pizza(self) -> AgregarPizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def produce_masa(self) -> None:
        self._pizza.add(self.orden[0])

    def produce_salsa(self) -> None:
        self._pizza.add(self.orden[1])

    def produce_queso(self) -> None:
        self._pizza.add(self.orden[2])
    
    def produce_ingrediente1(self) -> None:
        self._pizza.add(self.orden[3])    
        
    def produce_ingrediente2(self) -> None:
        self._pizza.add(self.orden[4])    
    
    def produce_ingrediente3(self) -> None:
        self._pizza.add(self.orden[5])

    def produce_coccion(self) -> None:
        self._pizza.add(self.orden[6])

    def produce_presentacion(self) -> None:
        self._pizza.add(self.orden[7]) 

    def produce_maridaje(self) -> None:
        self._pizza.add(self.orden[8])

    def produce_extras(self) -> None:
        self._pizza.add(self.orden[9])