class Funcion:
    tipo = None
    tablaVariable = None

    def __init__(self, tipo):
        self.tipo = tipo
        self.tablaVariable = {}

class Variable:
    tipo = None
    dimX = None
    dimY = None
    dirAlmacenamiento = None

    def __init__(self, tipo, dirAlmacenamiento):
        self.tipo = tipo
        self.dirAlmacenamiento = dirAlmacenamiento
        self.dimX = 0
        self.dimY = 0

class ManejadorDeTablas:
    tablaFunciones = {}

    def addFuncion(self, nombreFuncion, tipoFuncion):
        f = Funcion(tipoFuncion)

        if nombreFuncion in self.tablaFunciones:
            print("Error, la funcion", nombreFuncion, "ya fue declarada\n")
            exit(-1)

        self.tablaFunciones[nombreFuncion] = f
        #print(self.tablaFunciones)

    def deleteFuncion(self, nombreFuncion):
        self.tablaFunciones[nombreFuncion] = None
        #print(self.tablaFunciones)

    def addVariable(self, nombreFuncion, nombreVariable, tipoVariable, dirAlmacenamiento):
        v = Variable(tipoVariable, dirAlmacenamiento)

        #print("agregando variable", nombreVariable, "a", nombreFuncion)
        if nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable:
            print("Error, variable ya fue declarada\n", nombreVariable, nombreFuncion)
            exit(-1)

        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable] = v
        #print(self.tablaFunciones[nombreFuncion].tablaVariable)

    def actualizarDimensiones(self, nombreFuncion, nombreVariable, dimX):
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable].dimX = dimX

    def actualizarDimensiones(self, nombreFuncion, nombreVariable, dimX, dimY):
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable].dimX = dimX
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable].dimY = dimY

    def contieneID(self, nombreFuncion, nombreVariable):
        return (nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable and
                nombreVariable in self.tablaFunciones["PROGRAMA"].tablaVariable)

    def existeFuncion(self, nombreFuncion):
        return nombreFuncion in self.tablaFunciones
