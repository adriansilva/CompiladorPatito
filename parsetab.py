
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'declaracionFuncionleftPLUSMINUSleftMULTIPLYDIVIDEleftOPMATRIZASSIGN CARACTER CBRACKET CCORCH CHAR COLON COMA COMENTARIO CPAREN DESDE DIVIDE ENTERO ENTONCES ESCRIBE FLOAT FLOTANTE FUNCION HASTA HAZ ID IGNORE INT LEE LOGIC MIENTRAS MINUS MULTIPLY NEWLINE NUMBER OBRACKET OCORCH OPAREN OPMATRIZ PLUS PRINCIPAL PROGRAMA REGRESA RELOP SEMICOLON SI SINO VAR VOID\n    programa : PROGRAMA ID SEMICOLON programa2\n    \n    programa2 : declaracion programa2\n              | programa3\n    \n    programa3 : declaracionFuncion programa3\n              | principal\n    \n    principal : PRINCIPAL OPAREN CPAREN OBRACKET estatutos CBRACKET\n    \n    declaracion : VAR INT COLON declaracion2\n                | VAR FLOAT COLON declaracion2\n                | VAR CHAR COLON declaracion2\n    \n    declaracion2 : SEMICOLON\n    \n    declaracion2 : posibleID declaracion3\n    \n    declaracion3 : SEMICOLON\n    \n    declaracion3 : COMA declaracion2\n    \n    declaracion3 : ASSIGN expresion SEMICOLON\n    \n    declaracion3 : ASSIGN expresion COMA declaracion2\n    \n    declaracionFuncion : FUNCION VOID ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET\n                       | FUNCION INT ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET\n                       | FUNCION FLOAT ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET\n                       | FUNCION CHAR ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET\n    \n    declaracionFuncionParametros : empty\n    \n    declaracionFuncionParametros : INT ID\n                                 | FLOAT ID\n                                 | CHAR ID\n    \n    declaracionFuncionParametros : INT ID declaracionFuncionParametros2\n                                 | FLOAT ID declaracionFuncionParametros2\n                                 | CHAR ID declaracionFuncionParametros2\n    \n    declaracionFuncionParametros2 : COMA INT ID\n                                  | COMA FLOAT ID\n                                  | COMA CHAR ID\n    \n    declaracionFuncionParametros2 : COMA INT ID declaracionFuncionParametros2\n                                  | COMA FLOAT ID declaracionFuncionParametros2\n                                  | COMA CHAR ID declaracionFuncionParametros2\n    \n    declaracionFuncionVariables : empty\n                                | declaracion\n    \n    estatutos : empty\n    \n    estatutos : declaracion estatutos\n              | estatutoRepeticionIncondicional estatutos\n              | lectura estatutos\n    \n    lectura : LEE OPAREN posibleID lectura2 CPAREN SEMICOLON\n    \n    lectura2 : empty\n    \n    lectura2 : COMA posibleID lectura2\n    \n    asignacion : ID ASSIGN expresion SEMICOLON\n    \n    expresion : expresion LOGIC expresion\n              | expresion RELOP expresion\n    \n    expresion : termino1 OPMATRIZ\n    \n    expresion : termino\n    \n    termino : termino PLUS termino\n            | termino MINUS termino\n            | termino MULTIPLY termino\n            | termino DIVIDE termino\n    \n    termino : termino1 OPMATRIZ\n    \n    termino : termino1\n    \n    termino1 : posibleID\n             | ENTERO\n             | FLOTANTE\n             | CARACTER\n    \n    posibleID : ID\n    \n    posibleID : ID OCORCH expresion CCORCH\n    \n    posibleID : ID OCORCH expresion COMA expresion CCORCH\n    \n    termino1 : OPAREN expresion CPAREN\n    \n    estatutoRepeticionIncondicional : DESDE ID ASSIGN expresion HASTA expresion HAZ OBRACKET estatutos CBRACKET\n    \n    empty :\n    '
    
_lr_action_items = {'OCORCH':([70,],[85,]),'HASTA':([70,93,94,95,97,98,99,102,108,114,121,123,124,125,126,127,128,129,134,135,],[-57,-56,-46,-52,-55,-54,-53,118,-58,-45,-44,-43,-49,-52,-47,-50,-48,-60,-59,-51,]),'FUNCION':([0,],[1,]),'CARACTER':([85,87,90,96,106,107,109,110,111,112,113,118,],[93,93,93,93,93,93,93,93,93,93,93,93,]),'COMA':([23,24,26,51,52,53,70,73,91,92,93,94,95,97,98,99,100,108,114,119,121,123,124,125,126,127,128,129,134,135,],[30,30,30,30,30,30,-57,89,103,107,-56,-46,-52,-55,-54,-53,116,-58,-45,103,-44,-43,-49,-52,-47,-50,-48,-60,-59,-51,]),'FLOAT':([1,11,12,13,14,30,34,],[6,19,19,19,19,43,46,]),'VAR':([25,27,28,29,47,48,49,50,59,61,63,71,72,74,75,86,88,101,117,130,133,137,139,],[34,34,34,34,34,34,34,34,34,34,34,-9,-10,-7,-8,-11,-12,-13,-14,-15,-39,34,-61,]),'CCORCH':([70,92,93,94,95,97,98,99,108,114,121,122,123,124,125,126,127,128,129,134,135,],[-57,108,-56,-46,-52,-55,-54,-53,-58,-45,-44,134,-43,-49,-52,-47,-50,-48,-60,-59,-51,]),'OPMATRIZ':([70,93,95,97,98,99,108,125,129,134,],[-57,-56,114,-55,-54,-53,-58,135,-60,-59,]),'MULTIPLY':([70,93,94,95,97,98,99,108,114,124,125,126,127,128,129,134,135,],[-57,-56,110,-52,-55,-54,-53,-58,-51,-49,-52,110,-50,110,-60,-59,-51,]),'OBRACKET':([25,27,28,29,33,35,36,38,39,40,71,72,74,75,86,88,101,117,130,136,],[-62,-62,-62,-62,-33,47,-34,48,49,50,-9,-10,-7,-8,-11,-12,-13,-14,-15,137,]),'COLON':([44,45,46,],[54,55,56,]),'PLUS':([70,93,94,95,97,98,99,108,114,124,125,126,127,128,129,134,135,],[-57,-56,111,-52,-55,-54,-53,-58,-51,-49,-52,-47,-50,-48,-60,-59,-51,]),'OPAREN':([7,8,9,10,62,85,87,90,96,106,107,109,110,111,112,113,118,],[11,12,13,14,80,96,96,96,96,96,96,96,96,96,96,96,96,]),'RELOP':([70,92,93,94,95,97,98,99,100,102,108,114,115,121,122,123,124,125,126,127,128,129,131,134,135,],[-57,106,-56,-46,-52,-55,-54,-53,106,106,-58,-45,106,106,106,106,-49,-52,-47,-50,-48,-60,106,-59,-51,]),'INT':([1,11,12,13,14,30,34,],[5,17,17,17,17,41,45,]),'MINUS':([70,93,94,95,97,98,99,108,114,124,125,126,127,128,129,134,135,],[-57,-56,113,-52,-55,-54,-53,-58,-51,-49,-52,-47,-50,-48,-60,-59,-51,]),'ENTERO':([85,87,90,96,106,107,109,110,111,112,113,118,],[98,98,98,98,98,98,98,98,98,98,98,98,]),'CPAREN':([11,12,13,14,15,18,20,21,22,23,24,26,31,32,37,51,52,53,67,68,69,70,91,93,94,95,97,98,99,104,105,108,114,115,119,121,123,124,125,126,127,128,129,132,134,135,],[-62,-62,-62,-62,-20,25,27,28,29,-23,-21,-22,-26,-24,-25,-27,-29,-28,-30,-32,-31,-57,-62,-56,-46,-52,-55,-54,-53,-40,120,-58,-45,129,-62,-44,-43,-49,-52,-47,-50,-48,-60,-41,-59,-51,]),'VOID':([1,],[3,]),'DIVIDE':([70,93,94,95,97,98,99,108,114,124,125,126,127,128,129,134,135,],[-57,-56,112,-52,-55,-54,-53,-58,-51,-49,-52,112,-50,112,-60,-59,-51,]),'FLOTANTE':([85,87,90,96,106,107,109,110,111,112,113,118,],[97,97,97,97,97,97,97,97,97,97,97,97,]),'ID':([3,4,5,6,16,17,19,41,42,43,54,55,56,60,80,85,87,89,90,96,103,106,107,109,110,111,112,113,116,118,],[7,8,9,10,23,24,26,51,52,53,70,70,70,78,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'HAZ':([70,93,94,95,97,98,99,108,114,121,123,124,125,126,127,128,129,131,134,135,],[-57,-56,-46,-52,-55,-54,-53,-58,-45,-44,-43,-49,-52,-47,-50,-48,-60,136,-59,-51,]),'DESDE':([47,48,49,50,59,61,63,71,72,74,75,86,88,101,117,130,133,137,139,],[60,60,60,60,60,60,60,-9,-10,-7,-8,-11,-12,-13,-14,-15,-39,60,-61,]),'CBRACKET':([47,48,49,50,57,58,59,61,63,64,65,66,71,72,74,75,77,79,81,86,88,101,117,130,133,137,138,139,],[-62,-62,-62,-62,-35,76,-62,-62,-62,82,83,84,-9,-10,-7,-8,-37,-36,-38,-11,-12,-13,-14,-15,-39,-62,139,-61,]),'ASSIGN':([70,73,78,108,134,],[-57,87,90,-58,-59,]),'$end':([2,76,82,83,84,],[0,-16,-19,-17,-18,]),'LEE':([47,48,49,50,59,61,63,71,72,74,75,86,88,101,117,130,133,137,139,],[62,62,62,62,62,62,62,-9,-10,-7,-8,-11,-12,-13,-14,-15,-39,62,-61,]),'SEMICOLON':([54,55,56,70,73,89,93,94,95,97,98,99,100,108,114,116,120,121,123,124,125,126,127,128,129,134,135,],[72,72,72,-57,88,72,-56,-46,-52,-55,-54,-53,117,-58,-45,72,133,-44,-43,-49,-52,-47,-50,-48,-60,-59,-51,]),'LOGIC':([70,92,93,94,95,97,98,99,100,102,108,114,115,121,122,123,124,125,126,127,128,129,131,134,135,],[-57,109,-56,-46,-52,-55,-54,-53,109,109,-58,-45,109,109,109,109,-49,-52,-47,-50,-48,-60,109,-59,-51,]),'CHAR':([1,11,12,13,14,30,34,],[4,16,16,16,16,42,44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([85,87,90,96,106,107,109,118,],[92,100,102,115,121,122,123,131,]),'declaracion3':([73,],[86,]),'empty':([11,12,13,14,25,27,28,29,47,48,49,50,59,61,63,91,119,137,],[15,15,15,15,33,33,33,33,57,57,57,57,57,57,57,104,104,57,]),'lectura2':([91,119,],[105,132,]),'declaracionFuncionParametros2':([23,24,26,51,52,53,],[31,32,37,67,68,69,]),'lectura':([47,48,49,50,59,61,63,137,],[63,63,63,63,63,63,63,63,]),'termino':([85,87,90,96,106,107,109,110,111,112,113,118,],[94,94,94,94,94,94,94,124,126,127,128,94,]),'declaracionFuncionVariables':([25,27,28,29,],[35,38,39,40,]),'termino1':([85,87,90,96,106,107,109,110,111,112,113,118,],[95,95,95,95,95,95,95,125,125,125,125,95,]),'declaracion':([25,27,28,29,47,48,49,50,59,61,63,137,],[36,36,36,36,61,61,61,61,61,61,61,61,]),'declaracionFuncionParametros':([11,12,13,14,],[18,20,21,22,]),'declaracion2':([54,55,56,89,116,],[71,74,75,101,130,]),'estatutos':([47,48,49,50,59,61,63,137,],[58,64,65,66,77,79,81,138,]),'declaracionFuncion':([0,],[2,]),'estatutoRepeticionIncondicional':([47,48,49,50,59,61,63,137,],[59,59,59,59,59,59,59,59,]),'posibleID':([54,55,56,80,85,87,89,90,96,103,106,107,109,110,111,112,113,116,118,],[73,73,73,91,99,99,73,99,99,119,99,99,99,99,99,99,99,73,99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracionFuncion","S'",1,None,None,None),
  ('programa -> PROGRAMA ID SEMICOLON programa2','programa',4,'p_programa','yaccPatito.py',27),
  ('programa2 -> declaracion programa2','programa2',2,'p_programa2','yaccPatito.py',33),
  ('programa2 -> programa3','programa2',1,'p_programa2','yaccPatito.py',34),
  ('programa3 -> declaracionFuncion programa3','programa3',2,'p_programa3','yaccPatito.py',41),
  ('programa3 -> principal','programa3',1,'p_programa3','yaccPatito.py',42),
  ('principal -> PRINCIPAL OPAREN CPAREN OBRACKET estatutos CBRACKET','principal',6,'p_principal','yaccPatito.py',48),
  ('declaracion -> VAR INT COLON declaracion2','declaracion',4,'p_declaracion','yaccPatito.py',54),
  ('declaracion -> VAR FLOAT COLON declaracion2','declaracion',4,'p_declaracion','yaccPatito.py',55),
  ('declaracion -> VAR CHAR COLON declaracion2','declaracion',4,'p_declaracion','yaccPatito.py',56),
  ('declaracion2 -> SEMICOLON','declaracion2',1,'p_declaracion2_1','yaccPatito.py',62),
  ('declaracion2 -> posibleID declaracion3','declaracion2',2,'p_declaracion2_2','yaccPatito.py',68),
  ('declaracion3 -> SEMICOLON','declaracion3',1,'p_declaracion3_1','yaccPatito.py',74),
  ('declaracion3 -> COMA declaracion2','declaracion3',2,'p_declaracion3_2','yaccPatito.py',80),
  ('declaracion3 -> ASSIGN expresion SEMICOLON','declaracion3',3,'p_declaracion3_3','yaccPatito.py',86),
  ('declaracion3 -> ASSIGN expresion COMA declaracion2','declaracion3',4,'p_declaracion3_4','yaccPatito.py',92),
  ('declaracionFuncion -> FUNCION VOID ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET','declaracionFuncion',10,'p_declaracionFuncion','yaccPatito.py',98),
  ('declaracionFuncion -> FUNCION INT ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET','declaracionFuncion',10,'p_declaracionFuncion','yaccPatito.py',99),
  ('declaracionFuncion -> FUNCION FLOAT ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET','declaracionFuncion',10,'p_declaracionFuncion','yaccPatito.py',100),
  ('declaracionFuncion -> FUNCION CHAR ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET','declaracionFuncion',10,'p_declaracionFuncion','yaccPatito.py',101),
  ('declaracionFuncionParametros -> empty','declaracionFuncionParametros',1,'p_declaracionFuncionParametros_1','yaccPatito.py',108),
  ('declaracionFuncionParametros -> INT ID','declaracionFuncionParametros',2,'p_declaracionFuncionParametros_2','yaccPatito.py',114),
  ('declaracionFuncionParametros -> FLOAT ID','declaracionFuncionParametros',2,'p_declaracionFuncionParametros_2','yaccPatito.py',115),
  ('declaracionFuncionParametros -> CHAR ID','declaracionFuncionParametros',2,'p_declaracionFuncionParametros_2','yaccPatito.py',116),
  ('declaracionFuncionParametros -> INT ID declaracionFuncionParametros2','declaracionFuncionParametros',3,'p_declaracionFuncionParametros_3','yaccPatito.py',122),
  ('declaracionFuncionParametros -> FLOAT ID declaracionFuncionParametros2','declaracionFuncionParametros',3,'p_declaracionFuncionParametros_3','yaccPatito.py',123),
  ('declaracionFuncionParametros -> CHAR ID declaracionFuncionParametros2','declaracionFuncionParametros',3,'p_declaracionFuncionParametros_3','yaccPatito.py',124),
  ('declaracionFuncionParametros2 -> COMA INT ID','declaracionFuncionParametros2',3,'p_declaracionFuncionParametros2_3','yaccPatito.py',130),
  ('declaracionFuncionParametros2 -> COMA FLOAT ID','declaracionFuncionParametros2',3,'p_declaracionFuncionParametros2_3','yaccPatito.py',131),
  ('declaracionFuncionParametros2 -> COMA CHAR ID','declaracionFuncionParametros2',3,'p_declaracionFuncionParametros2_3','yaccPatito.py',132),
  ('declaracionFuncionParametros2 -> COMA INT ID declaracionFuncionParametros2','declaracionFuncionParametros2',4,'p_declaracionFuncionParametros2_4','yaccPatito.py',138),
  ('declaracionFuncionParametros2 -> COMA FLOAT ID declaracionFuncionParametros2','declaracionFuncionParametros2',4,'p_declaracionFuncionParametros2_4','yaccPatito.py',139),
  ('declaracionFuncionParametros2 -> COMA CHAR ID declaracionFuncionParametros2','declaracionFuncionParametros2',4,'p_declaracionFuncionParametros2_4','yaccPatito.py',140),
  ('declaracionFuncionVariables -> empty','declaracionFuncionVariables',1,'p_declaracionFuncionVariables','yaccPatito.py',146),
  ('declaracionFuncionVariables -> declaracion','declaracionFuncionVariables',1,'p_declaracionFuncionVariables','yaccPatito.py',147),
  ('estatutos -> empty','estatutos',1,'p_estatutos_1','yaccPatito.py',152),
  ('estatutos -> declaracion estatutos','estatutos',2,'p_estatutos_2','yaccPatito.py',157),
  ('estatutos -> estatutoRepeticionIncondicional estatutos','estatutos',2,'p_estatutos_2','yaccPatito.py',158),
  ('estatutos -> lectura estatutos','estatutos',2,'p_estatutos_2','yaccPatito.py',159),
  ('lectura -> LEE OPAREN posibleID lectura2 CPAREN SEMICOLON','lectura',6,'p_lectura','yaccPatito.py',165),
  ('lectura2 -> empty','lectura2',1,'p_lectura2_1','yaccPatito.py',170),
  ('lectura2 -> COMA posibleID lectura2','lectura2',3,'p_lectura2_3','yaccPatito.py',175),
  ('asignacion -> ID ASSIGN expresion SEMICOLON','asignacion',4,'p_asignacion_4','yaccPatito.py',180),
  ('expresion -> expresion LOGIC expresion','expresion',3,'p_expresion_3','yaccPatito.py',185),
  ('expresion -> expresion RELOP expresion','expresion',3,'p_expresion_3','yaccPatito.py',186),
  ('expresion -> termino1 OPMATRIZ','expresion',2,'p_expresion_2','yaccPatito.py',192),
  ('expresion -> termino','expresion',1,'p_expresion_1','yaccPatito.py',198),
  ('termino -> termino PLUS termino','termino',3,'p_termino_3','yaccPatito.py',214),
  ('termino -> termino MINUS termino','termino',3,'p_termino_3','yaccPatito.py',215),
  ('termino -> termino MULTIPLY termino','termino',3,'p_termino_3','yaccPatito.py',216),
  ('termino -> termino DIVIDE termino','termino',3,'p_termino_3','yaccPatito.py',217),
  ('termino -> termino1 OPMATRIZ','termino',2,'p_termino_2','yaccPatito.py',244),
  ('termino -> termino1','termino',1,'p_termino_1','yaccPatito.py',250),
  ('termino1 -> posibleID','termino1',1,'p_termino1_1','yaccPatito.py',256),
  ('termino1 -> ENTERO','termino1',1,'p_termino1_1','yaccPatito.py',257),
  ('termino1 -> FLOTANTE','termino1',1,'p_termino1_1','yaccPatito.py',258),
  ('termino1 -> CARACTER','termino1',1,'p_termino1_1','yaccPatito.py',259),
  ('posibleID -> ID','posibleID',1,'p_posibleID_1','yaccPatito.py',265),
  ('posibleID -> ID OCORCH expresion CCORCH','posibleID',4,'p_posibleID_4','yaccPatito.py',271),
  ('posibleID -> ID OCORCH expresion COMA expresion CCORCH','posibleID',6,'p_posibleID_6','yaccPatito.py',277),
  ('termino1 -> OPAREN expresion CPAREN','termino1',3,'p_termino1_3','yaccPatito.py',283),
  ('estatutoRepeticionIncondicional -> DESDE ID ASSIGN expresion HASTA expresion HAZ OBRACKET estatutos CBRACKET','estatutoRepeticionIncondicional',10,'p_estatutoRepeticionIncondicional','yaccPatito.py',290),
  ('empty -> <empty>','empty',0,'p_empty','yaccPatito.py',298),
]
