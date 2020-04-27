class TablaFuncion:
    self.nombre = None
    self.tipo = None
    self.tablaVariable = None

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo



class TablaVariable:
    self.nombre = None
    self.tipo = None
    self.dirAlmacenamiento = None

    def __init__(self, nombre, tipo, dirAlmacenamiento):
        self.nombre = nombre
        self.tipo = tipo
        self.dirAlmacenamiento = dirAlmacenamiento