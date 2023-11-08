from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
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