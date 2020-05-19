'''
Estoy considerando que tenemos una variable tipo Bool. Recuerdo que
habiamos dicho que no ibamos a tener, pero después de pensarlo bien,
me parece que lo mejor es sí tenerla. Habría que cambiar algunas cosas,
entre ellas los tokens del léxico para aceptar BOOL, TRUE, FALSE. También
en termino1 habría que agregar True y False, al igual que en todas las
declaraciones permitir declarar el BOOL.
'''

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
                         [1,         1,       1], #Arreglo
                         [2,         2,       2]  #Matriz
                   ],

                   [ #ValorÚnico  Arreglo  Matriz
                         [0,        -1,      -1], #ValorÚnico       TYPE: '*'
                         [1,         1,       1], #Arreglo
                         [2,         2,       2]  #Matriz
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
                         [-1,        1,      -1], #Arreglo
                         [-1,       -1,       2]  #Matriz
                   ]

                  ]

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
    if type(regresa) is int:
         return regresa
    else:
        print(regresa)
        exit(-1)

def cubo(tipo1, tipo2, operacion, dimension1, dimension2):
    tipoResultante = cuboTipos[typeToInt(operacion)][typeToInt(tipo1)][typeToInt(tipo2)]
    dimensionResultante = cuboDimensiones[typeToInt(operacion) if (operacion != '<>' and operacion != '==') else 6][dimension1][dimension2]
    if dimensionResultante == -1:
        print("Esta operación aritmética no es válida por discrepancias de dimensiones.")
        exit(-1)
    print("tipo:",tipoResultante, " // dimension:",dimensionResultante)
    return (tipoResultante,dimensionResultante)
    # if dimensiones == (0): regresas un
