class Funcion:
    tipo = None
    tablaVariable = None
    parametros = None
    inicianCuadruplos = None
    tieneReturn = None
    contadorInt = None
    contadorFloat = None
    contadorChar = None
    contadorBool = None
    contadorPoints = None
    contadorTemporales = None

    # Globales: Int 5000 Float 6000 Char 7000 Bool 8000
    # Funcion: Int 9000 Float 10000 Char 11000 Bool 12000
    # Constantes: Int 13000 Float 14000 Char 15000
    # Temporales: Int 16000 Float 18000 Char 20000 Bool 22000 Pointers 24000

    def __init__(self, tipo):
        self.tipo = tipo #Tipo de la función
        self.tablaVariable = {} #Un diccionario cuya llave es un string y su valor es un objeto de tipo variable
        self.parametros = "" #Un string que lleva la cuenta del tipo y la cantidad de parámetros
        self.inicianCuadruplos = 1 #Un entero que lleva la posición del cuádruplo en el que inicia la función en cuestión
        self.tieneReturn = False #Un boleano que determina si la función debería tener un return en base a su tipo

        #Un contador por cada espacio de memoria reservado para ese tipo de variables (si se reserva un arreglo el contador aumentará por el tamaño del arreglo)
        self.contadorInt = 0
        self.contadorFloat = 0
        self.contadorChar = 0
        self.contadorBool = 0
        self.contadorPoints = 0
        self.contadorTemporales = 0

class Variable:
    tipo = None
    dimension = None
    dirAlmacenamiento = None
    d1 = None
    d2 = None

    def __init__(self, tipo, dirAlmacenamiento, d1, d2):
        self.tipo = tipo #Tipo de la variable
        self.dirAlmacenamiento = dirAlmacenamiento #Dirección de almacenamiento
        self.dimension = 0 #Dimensión {0 si es valor único, 1 si es arreglo, 2 si es matriz}
        self.d1 = d1 #El tamaño de la dimensión actual 1 (Esto es la cantidad de columnas si es arreglo o la cantidad de filas si es matriz)
        self.d2 = d2 #El tamaño de la dimensión actual 2 (Cantidad de columnas en una matriz)

class ManejadorDeTablas:
    tablaFunciones = None

    def __init__(self):
        self.tablaFunciones = {}

    def addFuncion(self, nombreFuncion, tipoFuncion):
        f = Funcion(tipoFuncion)

        if nombreFuncion in self.tablaFunciones:
            print("Error, la funcion", nombreFuncion, "ya fue declarada\n")
            exit(-1)

        self.tablaFunciones[nombreFuncion] = f

    def deleteFuncion(self, nombreFuncion):
        self.tablaFunciones[nombreFuncion] = None
        #print(self.tablaFunciones)

    def comienzaFunc(self, func, funcStart):
        self.tablaFunciones[func].comienzaFunc = funcStart

    def getFuncComienza(self, func):
        return self.tablaFunciones[func].comienzaFunc

    def addVariable(self, nombreFuncion, nombreVariable, tipoVariable, esParametro):
        direccion = None
        esTemporal = 1

        #Si la vaiable fue declarada en el ambiente actual arrojar error
        if nombreVariable in self.tablaFunciones[nombreFuncion].tablaVariable:
            print("Error, variable ya fue declarada\n", nombreVariable, nombreFuncion)
            exit(-1)

        if esParametro:
            #Si se trata de un parámetro la dirección es la de las funciones
            direccion = 9000
            if tipoVariable == 'INT':
                self.tablaFunciones[nombreFuncion].parametros += "i"
                direccion += self.tablaFunciones[nombreFuncion].contadorInt
                self.tablaFunciones[nombreFuncion].contadorInt += 1
            if tipoVariable == 'FLOAT':
                self.tablaFunciones[nombreFuncion].parametros += "f"
                direccion += self.tablaFunciones[nombreFuncion].contadorFloat + 1000 #Floats en 6000/9000
                self.tablaFunciones[nombreFuncion].contadorFloat += 1
            if tipoVariable == 'CHAR':
                self.tablaFunciones[nombreFuncion].parametros += "c"
                direccion += self.tablaFunciones[nombreFuncion].contadorChar + 2000 #Chars en 7000/10000
                self.tablaFunciones[nombreFuncion].contadorChar += 1
            if tipoVariable == 'BOOL':
                self.tablaFunciones[nombreFuncion].parametros += "b"
                direccion += self.tablaFunciones[nombreFuncion].contadorBool + 3000 #Bools en 8000/11000
                self.tablaFunciones[nombreFuncion].contadorBool += 1
        else:
            #En caso de no ser función se le asigna su función respectiva ya sea global, constante, temporal o local
            if nombreFuncion == 'PROGRAMA':
                direccion = 5000
            if nombreFuncion == 'CONSTANTES':
                direccion = 13000
            if nombreFuncion == 'TEMPORALES':
                direccion = 16000
                esTemporal = 2
                self.tablaFunciones['TEMPORALES'].contadorTemporales += 1
            if nombreFuncion not in ['PROGRAMA','CONSTANTES','TEMPORALES']:
                direccion = 9000

            #Se le asigna la posición de memoria disponible en base a la cantidad de espacios ocupados
            if tipoVariable == 'INT':
                direccion += self.tablaFunciones[nombreFuncion].contadorInt
                self.tablaFunciones[nombreFuncion].contadorInt += 1
            if tipoVariable == 'FLOAT':
                direccion += self.tablaFunciones[nombreFuncion].contadorFloat + 1000*esTemporal #Floats en 6000/9000
                self.tablaFunciones[nombreFuncion].contadorFloat += 1
            if tipoVariable == 'CHAR':
                direccion += self.tablaFunciones[nombreFuncion].contadorChar + 2000*esTemporal #Chars en 7000/10000
                self.tablaFunciones[nombreFuncion].contadorChar += 1
            if tipoVariable == 'BOOL':
                direccion += self.tablaFunciones[nombreFuncion].contadorBool + 3000*esTemporal #Bools en 8000/11000
                self.tablaFunciones[nombreFuncion].contadorBool += 1

            if nombreFuncion == 'TEMPORALES':
                nombreVariable = 'Temporal_'+str(direccion)
        v = Variable(tipoVariable, direccion,1,1)
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable] = v

    def actualizarDimensiones(self, nombreFuncion, nombreVariable, dimension):
        self.tablaFunciones[nombreFuncion].tablaVariable[nombreVariable].dimension = dimension

    def asignard1(self,func,var,valor):
        self.tablaFunciones[func].tablaVariable[var].d1 = valor
        self.tablaFunciones[func].tablaVariable[var].dimension = 1

    def asignard2(self,func,var,valor):
        self.tablaFunciones[func].tablaVariable[var].d2 = valor
        self.tablaFunciones[func].tablaVariable[var].dimension = 2

    def asignarMemoria(self,func,var,tipoVariable):
        nuevaMemoria = self.tablaFunciones[func].tablaVariable[var].d1*self.tablaFunciones[func].tablaVariable[var].d2 - 1 #Porque ya reservaste 1 espacio automáticamente añ añadirla a la función

        if tipoVariable == 'INT':
            self.tablaFunciones[func].contadorInt += nuevaMemoria
        if tipoVariable == 'FLOAT':
            self.tablaFunciones[func].contadorFloat += nuevaMemoria
        if tipoVariable == 'CHAR':
            self.tablaFunciones[func].contadorChar += nuevaMemoria
        if tipoVariable == 'BOOL':
            self.tablaFunciones[func].contadorBool += nuevaMemoria

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

    def getDsVariable(self, func, var):
        if var in self.tablaFunciones[func].tablaVariable:
            return (self.tablaFunciones[func].tablaVariable[var].d1,self.tablaFunciones[func].tablaVariable[var].d2)
        else:
            return (self.tablaFunciones['PROGRAMA'].tablaVariable[var].d1,self.tablaFunciones['PROGRAMA'].tablaVariable[var].d2)

    def getDireccionVariable(self,func,var):
        if var in self.tablaFunciones[func].tablaVariable:
            return self.tablaFunciones[func].tablaVariable[var].dirAlmacenamiento
        else:
            if var in self.tablaFunciones['PROGRAMA'].tablaVariable:
                return self.tablaFunciones['PROGRAMA'].tablaVariable[var].dirAlmacenamiento
            else:
                if var in self.tablaFunciones['CONSTANTES'].tablaVariable:
                    return self.tablaFunciones['CONSTANTES'].tablaVariable[var].dirAlmacenamiento
                else:
                    return self.tablaFunciones['TEMPORALES'].tablaVariable[var].dirAlmacenamiento

    def getFuncionVariable(self,func,var):
        if var in self.tablaFunciones[func].tablaVariable:
            return func
        else:
            if var in self.tablaFunciones['PROGRAMA'].tablaVariable:
                return 'PROGRAMA'
            else:
                if var in self.tablaFunciones['CONSTANTES'].tablaVariable:
                    return 'CONSTANTES'
                else:
                    return 'TEMPORALES'

    def getNewTemporal(self,tipoVariable,d1,d2):
        #Dirección de memoria de las temporales
        direccion = 16000
        if tipoVariable == 'INT':
            direccion += self.tablaFunciones['TEMPORALES'].contadorInt
            self.tablaFunciones['TEMPORALES'].contadorInt += d1*d2
        if tipoVariable == 'FLOAT':
            direccion += self.tablaFunciones['TEMPORALES'].contadorFloat + 2000
            self.tablaFunciones['TEMPORALES'].contadorFloat += d1*d2
        if tipoVariable == 'CHAR':
            direccion += self.tablaFunciones['TEMPORALES'].contadorChar + 4000
            self.tablaFunciones['TEMPORALES'].contadorChar += d1*d2
        if tipoVariable == 'BOOL':
            direccion += self.tablaFunciones['TEMPORALES'].contadorBool + 6000
            self.tablaFunciones['TEMPORALES'].contadorBool += d1*d2
        if tipoVariable == 'POINT':
            direccion += self.tablaFunciones['TEMPORALES'].contadorPoints + 8000
            self.tablaFunciones['TEMPORALES'].contadorPoints += d1*d2

        v = Variable(tipoVariable, direccion, d1, d2)

        self.tablaFunciones['TEMPORALES'].tablaVariable['Temporal_'+str(direccion)] = v
        self.tablaFunciones['TEMPORALES'].contadorTemporales += 1

        return direccion

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
        if con in self.tablaFunciones['CONSTANTES'].tablaVariable:
            return

        #Dirección de memoria de las constantes
        direccion = 13000
        if tipoVariable == 'INT':
            direccion += self.tablaFunciones['CONSTANTES'].contadorInt
            self.tablaFunciones['CONSTANTES'].contadorInt += 1
        if tipoVariable == 'FLOAT':
            direccion += self.tablaFunciones['CONSTANTES'].contadorFloat + 1000 #Floats en 6000/9000
            self.tablaFunciones['CONSTANTES'].contadorFloat += 1
        if tipoVariable == 'CHAR':
            direccion += self.tablaFunciones['CONSTANTES'].contadorChar + 2000 #Chars en 7000/10000
            self.tablaFunciones['CONSTANTES'].contadorChar += 1
        if tipoVariable == 'BOOL':
            direccion += self.tablaFunciones['CONSTANTES'].contadorBool + 3000 #Bools en 8000/11000
            self.tablaFunciones['CONSTANTES'].contadorBool += 1
        v = Variable(tipoVariable, direccion,1,1)

        self.tablaFunciones['CONSTANTES'].tablaVariable[con] = v
        #print(self.tablaFunciones['CONSTANTES'].tablaVariable[con].dirAlmacenamiento)

    def printTablas(self):
        for i in self.tablaFunciones:
            print("función:",i,"de tipo:",self.tablaFunciones[i].tipo,"con parametros:",self.tablaFunciones[i].parametros)
            for j in self.tablaFunciones[i].tablaVariable:
                print("variable:",j,"de tipo:",self.tablaFunciones[i].tablaVariable[j].tipo)
        print("Las variables usadas por tipo en PROGRAMA son:")
        print(self.tablaFunciones['PROGRAMA'].contadorInt)
        print(self.tablaFunciones['PROGRAMA'].contadorFloat)
        print(self.tablaFunciones['PROGRAMA'].contadorChar)
        print(self.tablaFunciones['PROGRAMA'].contadorBool)
