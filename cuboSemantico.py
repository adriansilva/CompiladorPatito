cuboTipos =   [[#INT  FLOAT  CHAR  BOOL
               [0,     1,    -1,   -1], #INT       TYPE: '+'
               [1,     1,    -1,   -1], #FLOAT
               [-1,   -1,     2,   -1], #CHAR
               [0,     1,    -1,    0], #BOOL
               ],

               [#INT  FLOAT  CHAR  BOOL
               [0,     1,    -1,   -1], #INT       TYPE: '-'
               [1,     1,    -1,   -1], #FLOAT
               [-1,   -1,     2,   -1], #CHAR
               [0,     1,    -1,    0], #BOOL
               ],

               [#INT  FLOAT  CHAR  BOOL
               [0,     1,    -1,    0], #INT       TYPE: '*'
               [1,     1,    -1,    0], #FLOAT
               [-1,   -1,    -1,   -1], #CHAR
               [0,     1,    -1,    0], #BOOL
               ],

               [#INT  FLOAT  CHAR  BOOL
               [0,     1,    -1,   -1], #INT       TYPE: '/'
               [1,     1,    -1,   -1], #FLOAT
               [-1,   -1,    -1,   -1], #CHAR
               [-1,    1,    -1,   -1], #BOOL
               ],

               [#INT  FLOAT  CHAR  BOOL
               [3,     3,    -1,    3], #INT       TYPE: '&&', '||'
               [3,     3,    -1,    3], #FLOAT
               [-1,   -1,    -1,   -1], #CHAR
               [3,     3,    -1,    3], #BOOL
               ],

               [#INT  FLOAT  CHAR  BOOL
               [3,     3,    -1,    3], #INT       TYPE: '<=', '>=', '<>', '<', '>', '=='
               [3,     3,    -1,    3], #FLOAT
               [-1,   -1,     3,   -1], #CHAR
               [3,     3,    -1,    3], #BOOL
               ],

               [#INT  FLOAT  CHAR  BOOL
               [0,    -1,    -1,   -1], #INT       TYPE: '='
               [1,     1,    -1,   -1], #FLOAT
               [-1,   -1,     2,   -1], #CHAR
               [-1,   -1,    -1,    3], #BOOL
               ]
             ]

cuboDimensiones = [[ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '+'
                         [1,         1,      -1], #Arreglo
                         [2,         2,       2]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '-'
                         [1,         1,      -1], #Arreglo
                         [2,         2,       2]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '*'
                         [1,        -1,       2], #Arreglo
                         [2,         2,       2]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '/'
                         [-1,       -1,      -1], #Arreglo
                         [-1,       -1,      -1]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '&&', '||'
                         [-1,       -1,      -1], #Arreglo
                         [-1,       -1,      -1]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '<=', '>=', '<', '>'
                         [-1,       -1,      -1], #Arreglo
                         [-1,       -1,      -1]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '==', '<>'
                         [-1,       -1,      -1], #Arreglo
                         [-1,       -1,      -1]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '='
                         [1,         1,      -1], #Arreglo
                         [2,        -1,       2]  #Matriz
                   ]
                  ]
#mat[3,3]
# A[3] = mat[0]
def typeToInt(tipo):
    switcher = {
        'INT':   0,
        'FLOAT': 1,
        'CHAR':  2,
        'BOOL':  3,
        '+':     0,
        '-':     1,
        '*':     2,
        '/':     3,
        '&&':    4,
        '||':    4,
        '<=':    5,
        '>=':    5,
        '<>':    5,
        '<':     5,
        '>':     5,
        '==':    5,
        'UNDEF': 5,
    }
    regresa = switcher.get(tipo, "Caracter inválido.")
    if isinstance(regresa,int):
        return regresa
    else:
        print("Tipo:", tipo)
        exit(-1)

def typeToIntDimension(tipo):
    switcher = {
        '+':     0,
        '-':     1,
        '*':     2,
        '/':     3,
        '&&':    4,
        '||':    4,
        '<=':    5,
        '>=':    5,
        '>':     5,
        '<':     5,
        '<>':    6,
        '==':    6,
        '=':     7,
        'UNDEF': 5,
    }
    regresa = switcher.get(tipo, "Caracter inválido.")
    if isinstance(regresa,int):
        return regresa
    else:
        print(tipo)
        exit(-1)

def intToType(entero):
    switcher = {
        0:    'INT',
        1:    'FLOAT',
        2:    'CHAR',
        3:    'BOOL',
    }
    regresa = switcher.get(entero, "Caracter inválido.")
    return regresa

def modificarDs(operacion, dimension1, dimension2, dsO1, dsO2):
    if operacion == '+' or operacion == '-':
        #Si es un arreglo +/- un valor único, ese valor se le añade a cada posición del arreglo
        if dimension1 ==1 and dimension2 == 0:
            return (operacion+str(dimension1)+str(dimension2),dsO1)
        #Si es un arreglo +/- un arreglo, dichos arreglos se suman sólo si tienen el mismo tamaño
        if dimension1 == 1 and dimension2 == 1:
            if dsO1 != dsO2:
                print("Para hacer una suma entre arreglos, es necesario que ambos sean del mismo tamaño.",dsO1,dsO2)
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),dsO1)
        #Si es una matriz +/- un valor único, ese valor se le añade a cada posición de la matriz.
        if dimension1 == 2 and dimension2== 0:
            return (operacion+str(dimension1)+str(dimension2),dsO1)
        #Si es una matriz +/- un arreglo, se verifica que el arreglo sea del mismo tamaño que una fila de la matriz y se suma a cada fila de dicha matriz
        if dimension1 == 2 and dimension2 == 1:
            if dsO1[1] != dsO2[0]:
                print("Para hacer una suma entre matriz y arreglo, es necesario que el tamaño del arreglo sea igual que la cantidad de columnas de la matriz.",dsO1,dsO2)
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),dsO1)
        #Si es una matriz +/- otra matriz, se verifica que tengan las mismas dimensiones y se suman los valores de las mismas posiciones.
        if dimension1 ==2 and dimension2 == 2:
            if dsO1 != dsO2:
                print("Para hacer una suma entre matríces, es necesario que ambas tengan las mismas dimensiones.",dsO1,dsO2)
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),dsO1)

    if operacion == '*':
        #Si es un arreglo * un valor único, se multiplica ese valor por cada posición del arreglo
        if dimension1 == 1 and dimension2 == 0:
            return (operacion+str(dimension1)+str(dimension2),dsO1)
        #Si es un arreglo * una matriz, se valida que el tamaño del arreglo sea del mismo tamaño que la cantidad de filas de la matriz  y se modifican las dimensiones del resultado como se explica a continuación
        if dimension1 == 1 and dimension2 == 2:
            if dsO1[1] != dsO2[0]:
                print("No se puede multiplicar las matrices porque las dimensiones no coinciden con el formato  a,b * b,c.")
                exit(-1) # 3x5 =  3x4 * 4x5
            else:
                return (operacion+str(dimension1)+str(dimension2),(dsO1[0],dsO2[1]))
        #Si es una matriz * un valor único, se multiplica ese valor por cada posición de la matriz
        if dimension1 == 2 and dimension2 == 0:
            return (operacion+str(dimension1)+str(dimension2),dsO1)
        #Si es una matriz * un arreglo, se valida que el tamaño de las columnas de la matriz se igual al tamaño de filas del arreglo (osea == 1 al final)
        if dimension1 == 2 and dimension2 == 1:
            if dsO1[1] != dsO2[0]:
                print("No se puede multiplicar las matrices porque las dimensiones no coinciden con el formato  a,b * b,c.")
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),(dsO1[0],dsO2[1]))
        #Si ambas son matriz se verifica que la cantidad de columnas de la primera sea igual a la cantidad de filas de la segunda
        if dimension1 == 2 and dimension2 == 2:
            if dsO1[1] != dsO2[0]:
                print("No se puede multiplicar las matrices porque las dimensiones no coinciden con el formato  a,b * b,c.")
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),(dsO1[0],dsO2[1]))

    if operacion == '=':
        #Si es un arreglo = valor único, se iguala cada casilla del arreglo al valor único
        if dimension1 == 1 and dimension2 == 0:
            return (operacion+str(dimension1)+str(dimension2),(dsO2,dsO1))

        #si es un arreglo = arreglo, se iguala cada casilla del arreglo 2 al arreglo 1 si son del mismo tamaño
        if dimension1 == 1 and dimension2 == 1:
            if dsO1 != dsO2:
                print("No se pueden igualar arreglos de diferentes dimensiones.")
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),(dsO2,dsO1))
        #Si es una matriz = valor único, se iguala cada casilla de la matriz a ese valor único
        if dimension1 == 2 and dimension2 == 0:
            return (operacion+str(dimension1)+str(dimension2),(dsO2,dsO1))
        #Si es una matriz = matriz, se iguala cada casilla de la segunda matriz a la primera matriz
        if dimension1 == 2 and dimension2 == 2:
            if dsO1 != dsO2:
                print("No se pueden igualar matrices de diferentes dimensiones.")
                exit(-1)
            else:
                return (operacion+str(dimension1)+str(dimension2),(dsO2,dsO1))

def cubo(tipo1, tipo2, operacion, dimension1, dimension2, dsO1, dsO2):
    #Si es un pointer, aquí es tratado como un entero (porque es una dirección de memoria entera) para determinar las operaciones correspondientes
    if tipo1 == "POINT":
        tipo1 = "INT"
    if tipo2 == "POINT":
        tipo2 = "INT"

    #Si la operación es un = se establece el index en 6
    tipoResultante = cuboTipos[typeToInt(operacion) if (operacion != '=') else 6][typeToInt(tipo1)][typeToInt(tipo2)]
    dimensionResultante = cuboDimensiones[typeToIntDimension(operacion)][dimension1][dimension2]
    #En caso de tener un index de -1, la operación no se pudo realizar con éxito
    if dimensionResultante == -1:
        if dimension1 == 0:
            dimensionO1 = "Valor Único"
        if dimension1 == 1:
            dimensionO1 = "Arreglo"
        if dimension1 == 2:
            dimensionO1 = "Matriz"
        if dimension2 == 0:
            dimensionO2 = "Valor Único"
        if dimension2 == 1:
            dimensionO2 = "Arreglo"
        if dimension2 == 2:
            dimensionO2 = "Matriz"

        print("Esta operación aritmética no es válida por discrepancias de dimensiones o no es soportada por el compilador:",dimensionO1,operacion,dimensionO2)
        exit(-1)
    if tipoResultante == -1:
        print("Esta operación aritmética no es válida por incongruencias de tipos:",tipo1,operacion,tipo2)
        exit(-1)
    #Si se trata de un arreglo o una matriz y está ejecutando alguna de las siguientes operaciones, modifica las Ds (dimensiones actuales) y el oeprador para la MV
    if dimension1+dimension2 > 0 and operacion in ['+','-','*','=']:
        resultado = modificarDs(operacion, dimension1, dimension2, dsO1, dsO2)
        operacion = resultado[0]
        dsO1 = resultado[1]

    return (operacion,intToType(tipoResultante),dimensionResultante,dsO1)

def cuboSolitario(tipo1, operacion, dimension1, dsO1):
    if dimension1 == 0:
        print("Las operaciones matriciales sólo se pueden hacer con matríces y no con valores únicos.")
        exit(-1)
    if operacion == '$':
        if dimension1 != 2 or dsO1[0] != dsO1[1]:
            print("Para obtener el determinante de una matriz, se necesita que esta sea cuadrada.")
            exit(-1)
        else:
            return (operacion,'FLOAT',0,(1,1)) # El determinante es un valor único de tipo FLOAT
    if operacion == '¡':
        if dimension1 == 1:
            return (operacion,tipo1,2,(dsO1[1],dsO1[0])) # Si era un arreglo, la transpuesta va a ser una matriz de dimension (1,x)
        else:
            if dsO1[0] == 1: # 1x4 = 4x1
                return (operacion,tipo1,1,(dsO1[1],dsO1[0])) # Si era una matriz, el resultado es la transpuesta tal cual con las mismas dimensiones.
            else: # 2x4 = 4x2
                return (operacion,tipo1,2,(dsO1[1],dsO1[0])) # Si era una matriz, el resultado es la transpuesta tal cual con las mismas dimensiones.
    if operacion == '?':
        if dimension1 != 2 or dsO1[0] != dsO1[1]:
            print("Para obtener la inversa de una matriz, se necesita que esta sea cuadrada.")
            exit(-1)
        else:
            return (operacion,'FLOAT',2,dsO1) # La inversa de una matriz mantiene sus dimensiones pero los valores pueden llegar a ser flotantes independientemente de si antes eran enteros o no.
