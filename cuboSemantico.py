mat = [[#INT  FLOAT  CHAR  BOOL
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
       [0,     1,    -1,   -1], #INT       TYPE: '*'
       [1,     1,    -1,   -1], #FLOAT
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
       [3,     3,    -1,    3], #INT       TYPE: '&&'
       [1,     1,    -1,   -1], #FLOAT
       [-1,   -1,    -1,   -1], #CHAR
       [-1,    1,    -1,   -1], #BOOL
       ],
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
        '||':    5,
        '<=':    6,
        '>=':    7,
        '<>':    8,
        '<':     9,
        '>':     10,
        '==':    11,
        'UNDEF': -1,
    }
    return switcher.get(tipo,"Caracter inválido.")

def cubo(tipo1, tipo2, operacion):
    tipoResultante = mat[typeToInt(operacion),typeToInt(tipo1), typeToInt(tipo2)]
    print(tipoResultante)
    # if dimensiones == (0): regresas un
