class Funcion:
    tipo = None
    tablaVariable = {}

    def __init__(self, tipo):
        self.tipo = tipo

class Variable:
    tipo = None
    dirAlmacenamiento = None

    def __init__(self, tipo, dirAlmacenamiento):
        self.tipo = tipo
        self.dirAlmacenamiento = dirAlmacenamiento

class ManejadorDeTablas:
    tablaFunciones = {}

    def addFuncion(self, nombreFuncion, tipoFuncion):
        f = Funcion(tipoFuncion)
        self.tablaFunciones[nombreFuncion] = f
        print(self.tablaFunciones)

    def addVariable(self, nombreFuncion, nombreVariable, tipoVariable, dirAlmacenamiento):
        v = Variable(tipoVariable, dirAlmacenamiento)
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable] = v
        print(self.tablaFunciones[nombreFuncion].tablaVariable)

    def contieneID(self, nombreFuncion, nombreVariable):
        return nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable
