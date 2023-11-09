from __future__ import annotations
from typing import Any
from Csv.csv import Csv


class AgregarPizza():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        csv = Csv('./orden.csv')
        csv.guardar_en_csv(self.parts)
        print('Pedido realizado con exito!')
        print("Su pedido es:")
        print(f"{', '.join(self.parts)}", end="")