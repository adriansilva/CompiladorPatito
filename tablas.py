class Funcion:
    tipo = None
    tablaVariable = None
    parametros = None
    contadorInt = None
    contadorFloat = None
    contadorChar = None
    contadorBool = None
    contadorTemporales = None
    contadorConstantes = None

    def __init__(self, tipo):
        self.tipo = tipo
        self.tablaVariable = {}
        self.parametros = ""
        self.contadorInt = 0
        self.contadorFloat = 0
        self.contadorChar = 0
        self.contadorBool = 0
        self.contadorTemporales = 13000
        self.contadorConstantes = 12000

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

    def __init__(self):
        self.tablaFunciones = {}

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
        direccion = 0
        print("agregando variable", nombreVariable, "a", nombreFuncion)
        print()
        if nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable:
            print("Error, variable ya fue declarada\n", nombreVariable, nombreFuncion)
            exit(-1)

        if esParametro:
            if tipoVariable == 'INT':
                self.tablaFunciones[nombreFuncion].parametros += "i"
            if tipoVariable == 'FLOAT':
                self.tablaFunciones[nombreFuncion].parametros += "f"
            if tipoVariable == 'CHAR':
                self.tablaFunciones[nombreFuncion].parametros += "c"
            if tipoVariable == 'BOOL':
                self.tablaFunciones[nombreFuncion].parametros += "b"
        else:
            if nombreFuncion == 'PROGRAMA':
                direccion = 5000
            if nombreFuncion == 'CONSTANTES':
                direccion = self.tablaFunciones[nombreFuncion].contadorConstantes
                self.tablaFunciones[nombreFuncion].contadorConstantes += 1
                pass
            if nombreFuncion == 'TEMPORALES':
                direccion = self.tablaFunciones[nombreFuncion].contadorTemporales
                cont = self.tablaFunciones[nombreFuncion].contadorTemporales
                self.tablaFunciones[nombreFuncion].contadorTemporales += 1
                nombreVariable = 'Temporal_' + str(cont)
                pass
            if nombreFuncion not in ['PROGRAMA','CONSTANTES','TEMPORALES']:
                print("ESTAMOS DECLARAAAANDO FUNCIONES.")
                direccion = 8000

            if tipoVariable == 'INT':
                direccion += self.tablaFunciones[nombreFuncion].contadorInt
                self.tablaFunciones[nombreFuncion].contadorInt += 1
            if tipoVariable == 'FLOAT':
                direccion += self.tablaFunciones[nombreFuncion].contadorFloat + 1000 #Floats en 6000/9000
                self.tablaFunciones[nombreFuncion].contadorFlot += 1
            if tipoVariable == 'CHAR':
                direccion += self.tablaFunciones[nombreFuncion].contadorChar + 2000 #Chars en 7000/10000
                self.tablaFunciones[nombreFuncion].contadorChar += 1
            if tipoVariable == 'BOOL':
                direccion += self.tablaFunciones[nombreFuncion].contadorBool + 3000 #Bools en 8000/11000
                self.tablaFunciones[nombreFuncion].contadorBool += 1

        v = Variable(tipoVariable, direccion)
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
    def getDireccionVariable(self,func,var):
        print(self.tablaFunciones['TEMPORALES'].tablaVariable)
        print("Esto es un var:",var, "Y aqui termina.")
        if var in self.tablaFunciones[func].tablaVariable:
            return self.tablaFunciones[func].tablaVariable[var].dirAlmacenamiento
        else:
            if var in self.tablaFunciones['CONSTANTES'].tablaVariable:
                return self.tablaFunciones['CONSTANTES'].tablaVariable[var].dirAlmacenamiento
            else:
                if var in self.tablaFunciones['TEMPORALES'].tablaVariable:
                    return self.tablaFunciones['TEMPORALES'].tablaVariable[var].dirAlmacenamiento
                else:
                    return self.tablaFunciones['PROGRAMA'].tablaVariable[var].dirAlmacenamiento
                    #print(self.tablaFunciones['CONSTANTES'].tablaVariable[var].dirAlmacenamiento,"\n\n\n\n\n\n\n\n\n\n\n\n")

    def getNewTemporal(self,tipoVariable):
        v = Variable(tipoVariable,self.tablaFunciones['TEMPORALES'].contadorTemporales)

        cont = self.tablaFunciones['TEMPORALES'].contadorTemporales
        self.tablaFunciones['TEMPORALES'].contadorTemporales += 1

        s = 'Temporal_'+str(cont)

        self.tablaFunciones['TEMPORALES'].tablaVariable[s] = v

        return cont

    def getParamsFuncion(self,func):
        return self.tablaFunciones[func].parametros

    def getTipoFuncion(self,func):
        return self.tablaFunciones[func].tipo

    def getDimensionVariable(self, func, var):
        if var in self.tablaFunciones[func].tablaVariable:
            return self.tablaFunciones[func].tablaVariable[var].dimension
        else:
            return self.tablaFunciones['PROGRAMA'].tablaVariable[var].dimension

    def addConstante(self, con, tipoVariable):
        v = Variable(tipoVariable, self.tablaFunciones['CONSTANTES'].contadorConstantes)

        if con not in self.tablaFunciones['CONSTANTES'].tablaVariable:
            self.tablaFunciones['CONSTANTES'].tablaVariable[con] = v
            self.tablaFunciones['CONSTANTES'].contadorConstantes += 1

    def printTablas(self):
        for i in self.tablaFunciones:
            print("función:",i,"de tipo:",self.tablaFunciones[i].tipo,"con parametros:",self.tablaFunciones[i].parametros)
            for j in self.tablaFunciones[i].tablaVariable:
                print("variable:",j,"de tipo:",self.tablaFunciones[i].tablaVariable[j].tipo)
