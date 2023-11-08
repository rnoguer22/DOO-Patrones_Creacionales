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
    def pizza(self) -> None:
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
    def produce_ingrediente1(self) -> None:
        pass    
    
    @abstractmethod
    def produce_ingrediente1(self) -> None:
        pass   
    
    @abstractmethod
    def produce_ingrediente1(self) -> None:
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
        self._pizza = PizzaPeperoni()

    @property
    def pizza(self) -> PizzaPeperoni:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
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


class PizzaPeperoni():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
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

    def build_pizza(self) -> None:
        self._builder.produce_masa()
        self._builder.produce_salsa()
        self._builder.produce_queso()
        self._builder.produce_ingrediente1()
        self._builder.produce_ingrediente2()
        self._builder.produce_ingrediente3()
        self._builder.produce_coccion()
        self._builder.produce_presentacion()
        self._builder.produce_maridaje()
        self._builder.produce_extras()

    def build_pizza_para_niños(self) -> None:
        self._builder.produce_masa()
        self._builder.produce_salsa()
        self._builder.produce_queso()
        self._builder.produce_coccion()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = BuilderPeperoni()
    director.builder = builder

    print("Standard basic product: ")
    director.build_pizza()
    builder.pizza.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_pizza_para_niños()
    builder.pizza.list_parts()