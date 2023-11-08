from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property #Para los getters y los setters
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_masa(self) -> None:
        pass

    @abstractmethod
    def produce_salsa(self) -> None:
        pass

    @abstractmethod
    def produce_queso(self) -> None:
        pass

    @abstractmethod
    def produce_ingredientes(self) -> None:
        pass

    @abstractmethod
    def produce_coccion(self) -> None:
        pass

    @abstractmethod
    def produce_presentacion(self) -> None:
        pass   

    @abstractmethod
    def produce_maridaje(self) -> None:
        pass

    @abstractmethod
    def produce_extras(self) -> None:
        pass


class BuilderPeperoni(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = PizzaPeperoni()

    @property
    def product(self) -> PizzaPeperoni:
        product = self._product
        self.reset()
        return product


    def produce_masa(self) -> None:
        self._product.add('Masa Fina')

    def produce_salsa(self) -> None:
        self._product.add('Tomate')

    def produce_queso(self) -> None:
        self._product.add('Mozzarella')

    def produce_ingredientes(self) -> None:
        self._product.add('Peperoni')

    def produce_coccion(self) -> None:
        self.product.add('Horno')

    def produce_presentacion(self) -> None:
        self.product.add('Caja de cartón') 

    def produce_maridaje(self) -> None:
        self.product.add('Cerveza')

    def produce_extras(self) -> None:
        self.product.add('Aceitunas')

class PizzaPeperoni():

    def __init__(self) -> None:
        self.parts = []
        self.parts.append('a')

    def add(self, part: Any) -> None:
        self.parts.append(part)
        print(self.parts)

    def list_parts(self) -> None:
        print('cucu2')
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """
                                                                                                                                        
    def build_pizza_para_niños(self) -> None:
        print('cucu1')
        self.builder.produce_masa()
        self.builder.produce_salsa()
        self.builder.produce_queso()
        self.builder.produce_coccion()
        print('cucu3')

    def build_pizza_completa(self) -> None:
        self.builder.produce_masa()
        self.builder.produce_salsa()
        self.builder.produce_queso()
        self.builder.produce_ingredientes()
        self.builder.produce_coccion()
        self.builder.produce_presentacion()
        self.builder.produce_maridaje()
        self.builder.produce_extras()


if __name__ == "__main__":

    director = Director()
    builder = BuilderPeperoni()
    director.builder = builder

    print("Producto Basico: ")
    director.build_pizza_para_niños()
    print(builder.product.parts)
    builder.product.list_parts()

    print("\n")

    print('Pizza Completa:')
    director.build_pizza_completa()
    builder.product.list_parts()