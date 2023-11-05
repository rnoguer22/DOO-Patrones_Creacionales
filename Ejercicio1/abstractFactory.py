from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_graphic(self) -> AbstractGraphics:
        pass

    @abstractmethod
    def calculate_statistic(self) -> AbstractStatistics:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_graphic(self) -> AbstractGraphics:
        return Mean()

    def calculate_statistic(self) -> AbstractStatistics:
        return GraficoBarras()


class ConcreteFactory2(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_graphic(self) -> AbstractGraphics:
        return Mode()

    def calculate_statistic(self) -> AbstractStatistics:
        return GraficoBarras()
    
class ConcreteFactory3(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_graphic(self) -> AbstractGraphics:
        return Median()

    def calculate_statistic(self) -> AbstractStatistics:
        return GraficoBarras()
    
class ConcreteFactory4(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_graphic(self) -> AbstractGraphics:
        return Mean()

    def calculate_statistic(self) -> AbstractStatistics:
        return GraficoHistograma()
    
class ConcreteFactory5(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_graphic(self) -> AbstractGraphics:
        return Mode()

    def calculate_statistic(self) -> AbstractStatistics:
        return GraficoHistograma()
    
class ConcreteFactory6(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_graphic(self) -> AbstractGraphics:
        return Median()

    def calculate_statistic(self) -> AbstractStatistics:
        return GraficoHistograma()


class AbstractGraphics(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def create_graphic(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class GraficoBarras(AbstractGraphics):
    def create_graphic(self) -> str:
        return "Devolveria un grafico de barras"


class GraficoHistograma(AbstractGraphics):
    def create_graphic(self) -> str:
        return "Devolveria un histograma"


class AbstractStatistics(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def calculate_statistic(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def graphic_statistic(self, collaborator: AbstractGraphics) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class Mean(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return "Devolveria la media"

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la media"


class Mode(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return "Calcularia la moda"

    def graphic(self, collaborator: AbstractGraphics) -> str:
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la moda"
    
class Median(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return "Calcularia la mediana"

    def graphic(self, collaborator: AbstractGraphics) -> str:
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la mediana"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())