from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
from AbstractFactory.AbstractStatistics.abstractStatistics import AbstractStatistics
from AbstractFactory.AbstractGraphics.abstractGraphics import AbstractGraphics



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