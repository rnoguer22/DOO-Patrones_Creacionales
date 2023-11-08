from Builder.builder import Builder


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

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