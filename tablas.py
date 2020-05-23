class Funcion:
    tipo = None
    tablaVariable = None
    parametros = None

    def __init__(self, tipo):
        self.tipo = tipo
        self.tablaVariable = {}
        self.parametros = ""

class Variable:
    tipo = None
    dimension = None
    dirAlmacenamiento = None

    def __init__(self, tipo, dirAlmacenamiento):
        self.tipo = tipo
        self.dirAlmacenamiento = dirAlmacenamiento
        self.dimension = 0

class ManejadorDeTablas:
    tablaFunciones = None

    #DIRECCIONES DE VARIABLES
    #FORMATO [InicioDeSeccion, UltimaDireccionUtilizada]    ---    Inicio de Seccion sirve para ver si otra seccion va a hacer overwrite y marcar error
    globalInt = None
    globalFloat = None
    globalChar = None
    localInt = None
    localFloat = None
    localChar = None
    tempAddress = None
    constAddress = None

    def __init__(self):
        self.tablaFunciones = {}

        self.globalInt = [2000, 2000]
        self.globalFloat = [3000, 3000]
        self.globalChar = [4000, 4000]
        self.localInt = [5000, 5000]
        self.localFloat = [7000, 7000]
        self.localChar = [9000, 9000]
        self.tempAddress = [12000, 12000]
        self.constAddress = [14000, 14000]

    def addFuncion(self, nombreFuncion, tipoFuncion):
        f = Funcion(tipoFuncion)

        print("Añadiendo funcion:",nombreFuncion,"de tipo",tipoFuncion)

        if nombreFuncion in self.tablaFunciones:
            print("Error, la funcion", nombreFuncion, "ya fue declarada\n")
            exit(-1)

        self.tablaFunciones[nombreFuncion] = f
        #print(self.tablaFunciones)

    def deleteFuncion(self, nombreFuncion):
        self.tablaFunciones[nombreFuncion] = None
        #print(self.tablaFunciones)

    def addVariable(self, nombreFuncion, nombreVariable, tipoVariable, esParametro):
        address = None

        print("agregando variable", nombreVariable, "a", nombreFuncion)
        print()

        if nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable:
            print("Error, variable ya fue declarada\n", nombreVariable, nombreFuncion)
            exit(-1)



        if nombreFuncion == 'PROGRAMA' and tipoVariable == 'INT':
            address = self.globalInt[1]
            self.globalInt[1] += 1

        if nombreFuncion == 'PROGRAMA' and tipoVariable == 'FLOAT':
            address = self.globalFloat[1]
            self.globalFloat[1] += 1

        if nombreFuncion == 'PROGRAMA' and tipoVariable == 'CHAR':
            address = self.globalChar[1]
            self.globalChar[1] += 1

        if nombreFuncion != 'PROGRAMA' and tipoVariable == 'INT':
            address = self.localInt[1]
            self.localInt[1] += 1

        if nombreFuncion != 'PROGRAMA' and tipoVariable == 'FLOAT':
            address = self.localFloat[1]
            self.localFloat[1] += 1

        if nombreFuncion != 'PROGRAMA' and tipoVariable == 'CHAR':
            address = self.localChar[1]
            self.localChar[1] += 1        

        if nombreFuncion == 'TEMPORALES':
            address = self.tempAddress[1]
            self.tempAddress[1] += 1

        v = Variable(tipoVariable, address)

        if esParametro:
            if tipoVariable == 'INT':
                self.tablaFunciones[nombreFuncion].parametros += "i"
            if tipoVariable == 'FLOAT':
                self.tablaFunciones[nombreFuncion].parametros += "f"
            if tipoVariable == 'CHAR':
                self.tablaFunciones[nombreFuncion].parametros += "c"
            if tipoVariable == 'BOOL':
                self.tablaFunciones[nombreFuncion].parametros += "b"

        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable] = v
        #print(self.tablaFunciones[nombreFuncion].tablaVariable)

    def actualizarDimensiones(self, nombreFuncion, nombreVariable, dimension):
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable].dimension = dimension

    def contieneID(self, nombreFuncion, nombreVariable):
        return (nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable or
                nombreVariable in self.tablaFunciones["PROGRAMA"].tablaVariable)

    def existeFuncion(self, nombreFuncion):
        return (nombreFuncion in self.tablaFunciones)

    def getTipoVariable(self, func, var):
        if var in self.tablaFunciones[func].tablaVariable:
            return self.tablaFunciones[func].tablaVariable[var].tipo
        else:
            return self.tablaFunciones['PROGRAMA'].tablaVariable[var].tipo

    #Necesitamos un get dirección variable

    def getTipoFuncion(self,func):
        return self.tablaFunciones[func].tipo

    def getDimensionVariable(self, func, var):
        if var in self.tablaFunciones[func].tablaVariable:
            return self.tablaFunciones[func].tablaVariable[var].dimension
        else:
            return self.tablaFunciones['PROGRAMA'].tablaVariable[var].dimension

    def addConstante(self, con, tipoVariable):

        if con not in self.tablaFunciones['CONSTANTES'].tablaVariable:
            v = Variable(tipoVariable, self.constAddress[1])
            self.constAddress[1] += 1
            self.tablaFunciones['CONSTANTES'].tablaVariable[con] = v

    def getAddress(self, nombreFuncion, nombreVariable):
        return self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable].dirAlmacenamiento

    def printTablas(self):
        for i in self.tablaFunciones:
            print("función:",i,"de tipo:",self.tablaFunciones[i].tipo,"con parametros:",self.tablaFunciones[i].parametros)
            for j in self.tablaFunciones[i].tablaVariable:
                print("variable:",j,"de tipo:",self.tablaFunciones[i].tablaVariable[j].tipo)
