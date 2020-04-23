
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEleftOPMATRIZASSIGN CARACTER CBRACKET CCORCH CHAR COLON COMA COMENTARIO CPAREN DESDE DIVIDE ENTERO ENTONCES ESCRIBE FLOAT FLOTANTE FUNCION HASTA HAZ ID IGNORE INT LEE LOGIC MIENTRAS MINUS MULTIPLY NEWLINE NUMBER OBRACKET OCORCH OPAREN OPMATRIZ PLUS PRINCIPAL PROGRAMA REGRESA RELOP SEMICOLON SI SINO VAR VOID\n    programa : PROGRAMA ID SEMICOLON programa2\n    \n    programa2 : declaracion programa2\n              | programa3\n    \n    programa3 : declaracionFuncion programa3\n              | principal\n    \n    principal : PRINCIPAL OPAREN CPAREN OBRACKET estatutos CBRACKET\n    \n    declaracion : VAR INT COLON declaracion2\n                | VAR FLOAT COLON declaracion2\n                | VAR CHAR COLON declaracion2\n    \n    declaracion2 : SEMICOLON\n    \n    declaracion2 : ID declaracion3\n    \n    declaracion3 : SEMICOLON\n    \n    declaracion3 : COMA declaracion2\n    \n    declaracion3 : ASSIGN expresion SEMICOLON\n    \n    declaracion3 : ASSIGN expresion COMA declaracion2\n    \n    declaracionFuncion : FUNCION VOID ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos\n                       | FUNCION INT ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos\n                       | FUNCION FLOAT ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos\n                       | FUNCION CHAR ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos\n    \n    declaracionFuncion2 : ID\n                        | ID COMA declaracionFuncion2\n    \n    estatutos : empty\n    \n    estatutos : declaracion estatutos\n              | estatutoRepeticionIncondicional estatutos\n    \n    asignacion : ID ASSIGN expresion SEMICOLON\n    \n    expresion : expresion LOGIC expresion\n              | expresion RELOP expresion\n    \n    expresion : termino1 OPMATRIZ\n    \n    expresion : termino\n    \n    termino : termino PLUS termino\n            | termino MINUS termino\n            | termino MULTIPLY termino\n            | termino DIVIDE termino\n    \n        termino : termino1 OPMATRIZ\n        \n    termino : termino1\n    \n    termino1 : ID\n             | ENTERO\n             | FLOTANTE\n             | CARACTER\n    \n    termino1 : OPAREN expresion CPAREN\n    \n    estatutoRepeticionIncondicional : DESDE ID ASSIGN expresion HASTA expresion HAZ OBRACKET estatutos CBRACKET\n    \n    empty :\n    '
    
_lr_action_items = {'ASSIGN':([36,58,],[51,73,]),'$end':([2,6,9,11,13,19,57,],[0,-3,-5,-1,-4,-2,-6,]),'FLOTANTE':([51,67,73,79,80,81,82,84,86,103,],[64,64,64,64,64,64,64,64,64,64,]),'CPAREN':([14,46,47,48,49,50,64,65,66,69,70,71,75,83,88,94,95,96,97,98,99,100,102,108,],[23,59,-20,61,62,63,-38,-29,-39,-35,-37,-36,-21,99,-28,-33,-35,-30,-32,-31,-40,-26,-27,-34,]),'INT':([8,12,],[17,22,]),'PLUS':([64,65,66,69,70,71,88,94,95,96,97,98,99,108,],[-38,80,-39,-35,-37,-36,-34,-33,-35,-30,-32,-31,-40,-34,]),'OPAREN':([7,24,25,26,27,51,67,73,79,80,81,82,84,86,103,],[14,32,33,34,35,67,67,67,67,67,67,67,67,67,67,]),'DESDE':([31,37,38,39,40,41,42,53,54,72,87,90,91,92,93,101,111,113,],[44,-9,-10,-8,-7,44,44,-11,-12,-13,-14,44,44,44,44,-15,44,-41,]),'RELOP':([64,65,66,68,69,70,71,83,88,89,94,95,96,97,98,99,100,102,108,109,],[-38,-29,-39,86,-35,-37,-36,86,-28,86,-33,-35,-30,-32,-31,-40,86,86,-34,86,]),'HAZ':([64,65,66,69,70,71,88,94,95,96,97,98,99,100,102,108,109,],[-38,-29,-39,-35,-37,-36,-28,-33,-35,-30,-32,-31,-40,-26,-27,-34,110,]),'HASTA':([64,65,66,69,70,71,88,89,94,95,96,97,98,99,100,102,108,],[-38,-29,-39,-35,-37,-36,-28,103,-33,-35,-30,-32,-31,-40,-26,-27,-34,]),'PRINCIPAL':([4,5,10,37,38,39,40,41,42,45,53,54,55,56,72,87,90,91,92,93,101,104,105,106,107,113,],[7,7,7,-9,-10,-8,-7,-42,-42,-22,-11,-12,-23,-24,-13,-14,-42,-42,-42,-42,-15,-16,-19,-17,-18,-41,]),'MULTIPLY':([64,65,66,69,70,71,88,94,95,96,97,98,99,108,],[-38,81,-39,-35,-37,-36,-34,-33,-35,81,-32,81,-40,-34,]),'CHAR':([8,12,],[16,20,]),'LOGIC':([64,65,66,68,69,70,71,83,88,89,94,95,96,97,98,99,100,102,108,109,],[-38,-29,-39,84,-35,-37,-36,84,-28,84,-33,-35,-30,-32,-31,-40,84,84,-34,84,]),'COLON':([20,21,22,],[28,29,30,]),'FUNCION':([4,5,10,37,38,39,40,41,42,45,53,54,55,56,72,87,90,91,92,93,101,104,105,106,107,113,],[8,8,8,-9,-10,-8,-7,-42,-42,-22,-11,-12,-23,-24,-13,-14,-42,-42,-42,-42,-15,-16,-19,-17,-18,-41,]),'PROGRAMA':([0,],[1,]),'COMA':([36,47,64,65,66,68,69,70,71,88,94,95,96,97,98,99,100,102,108,],[52,60,-38,-29,-39,85,-35,-37,-36,-28,-33,-35,-30,-32,-31,-40,-26,-27,-34,]),'CARACTER':([51,67,73,79,80,81,82,84,86,103,],[66,66,66,66,66,66,66,66,66,66,]),'OPMATRIZ':([64,66,69,70,71,95,99,],[-38,-39,88,-37,-36,108,-40,]),'OBRACKET':([23,37,38,39,40,53,54,72,74,76,77,78,87,101,110,],[31,-9,-10,-8,-7,-11,-12,-13,90,91,92,93,-14,-15,111,]),'CBRACKET':([31,37,38,39,40,41,42,43,45,53,54,55,56,72,87,101,111,112,113,],[-42,-9,-10,-8,-7,-42,-42,57,-22,-11,-12,-23,-24,-13,-14,-15,-42,113,-41,]),'VOID':([8,],[15,]),'SEMICOLON':([3,28,29,30,36,52,64,65,66,68,69,70,71,85,88,94,95,96,97,98,99,100,102,108,],[4,38,38,38,54,38,-38,-29,-39,87,-35,-37,-36,38,-28,-33,-35,-30,-32,-31,-40,-26,-27,-34,]),'VAR':([4,10,31,37,38,39,40,41,42,53,54,59,61,62,63,72,87,90,91,92,93,101,111,113,],[12,12,12,-9,-10,-8,-7,12,12,-11,-12,12,12,12,12,-13,-14,12,12,12,12,-15,12,-41,]),'FLOAT':([8,12,],[18,21,]),'ENTERO':([51,67,73,79,80,81,82,84,86,103,],[70,70,70,70,70,70,70,70,70,70,]),'MINUS':([64,65,66,69,70,71,88,94,95,96,97,98,99,108,],[-38,82,-39,-35,-37,-36,-34,-33,-35,-30,-32,-31,-40,-34,]),'ID':([1,15,16,17,18,28,29,30,32,33,34,35,44,51,52,60,67,73,79,80,81,82,84,85,86,103,],[3,24,25,26,27,36,36,36,47,47,47,47,58,71,36,47,71,71,71,71,71,71,71,36,71,71,]),'DIVIDE':([64,65,66,69,70,71,88,94,95,96,97,98,99,108,],[-38,79,-39,-35,-37,-36,-34,-33,-35,79,-32,79,-40,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracionFuncion':([4,5,10,],[5,5,5,]),'estatutoRepeticionIncondicional':([31,41,42,90,91,92,93,111,],[42,42,42,42,42,42,42,42,]),'declaracionFuncion2':([32,33,34,35,60,],[46,48,49,50,75,]),'principal':([4,5,10,],[9,9,9,]),'programa':([0,],[2,]),'empty':([31,41,42,90,91,92,93,111,],[45,45,45,45,45,45,45,45,]),'declaracion3':([36,],[53,]),'declaracion':([4,10,31,41,42,59,61,62,63,90,91,92,93,111,],[10,10,41,41,41,74,76,77,78,41,41,41,41,41,]),'programa2':([4,10,],[11,19,]),'programa3':([4,5,10,],[6,13,6,]),'termino1':([51,67,73,79,80,81,82,84,86,103,],[69,69,69,95,95,95,95,69,69,69,]),'expresion':([51,67,73,84,86,103,],[68,83,89,100,102,109,]),'estatutos':([31,41,42,90,91,92,93,111,],[43,55,56,104,105,106,107,112,]),'termino':([51,67,73,79,80,81,82,84,86,103,],[65,65,65,94,96,97,98,65,65,65,]),'declaracion2':([28,29,30,52,85,],[37,39,40,72,101,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
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
  ('declaracion2 -> ID declaracion3','declaracion2',2,'p_declaracion2_2','yaccPatito.py',68),
  ('declaracion3 -> SEMICOLON','declaracion3',1,'p_declaracion3_1','yaccPatito.py',74),
  ('declaracion3 -> COMA declaracion2','declaracion3',2,'p_declaracion3_2','yaccPatito.py',80),
  ('declaracion3 -> ASSIGN expresion SEMICOLON','declaracion3',3,'p_declaracion3_3','yaccPatito.py',86),
  ('declaracion3 -> ASSIGN expresion COMA declaracion2','declaracion3',4,'p_declaracion3_4','yaccPatito.py',92),
  ('declaracionFuncion -> FUNCION VOID ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos','declaracionFuncion',9,'p_declaracionFuncion','yaccPatito.py',98),
  ('declaracionFuncion -> FUNCION INT ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos','declaracionFuncion',9,'p_declaracionFuncion','yaccPatito.py',99),
  ('declaracionFuncion -> FUNCION FLOAT ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos','declaracionFuncion',9,'p_declaracionFuncion','yaccPatito.py',100),
  ('declaracionFuncion -> FUNCION CHAR ID OPAREN declaracionFuncion2 CPAREN declaracion OBRACKET estatutos','declaracionFuncion',9,'p_declaracionFuncion','yaccPatito.py',101),
  ('declaracionFuncion2 -> ID','declaracionFuncion2',1,'p_declaracionFuncion2','yaccPatito.py',108),
  ('declaracionFuncion2 -> ID COMA declaracionFuncion2','declaracionFuncion2',3,'p_declaracionFuncion2','yaccPatito.py',109),
  ('estatutos -> empty','estatutos',1,'p_estatutos_1','yaccPatito.py',115),
  ('estatutos -> declaracion estatutos','estatutos',2,'p_estatutos_2','yaccPatito.py',120),
  ('estatutos -> estatutoRepeticionIncondicional estatutos','estatutos',2,'p_estatutos_2','yaccPatito.py',121),
  ('asignacion -> ID ASSIGN expresion SEMICOLON','asignacion',4,'p_asignacion_4','yaccPatito.py',127),
  ('expresion -> expresion LOGIC expresion','expresion',3,'p_expresion_3','yaccPatito.py',132),
  ('expresion -> expresion RELOP expresion','expresion',3,'p_expresion_3','yaccPatito.py',133),
  ('expresion -> termino1 OPMATRIZ','expresion',2,'p_expresion_2','yaccPatito.py',139),
  ('expresion -> termino','expresion',1,'p_expresion_1','yaccPatito.py',145),
  ('termino -> termino PLUS termino','termino',3,'p_termino_3','yaccPatito.py',161),
  ('termino -> termino MINUS termino','termino',3,'p_termino_3','yaccPatito.py',162),
  ('termino -> termino MULTIPLY termino','termino',3,'p_termino_3','yaccPatito.py',163),
  ('termino -> termino DIVIDE termino','termino',3,'p_termino_3','yaccPatito.py',164),
  ('termino -> termino1 OPMATRIZ','termino',2,'p_termino_2','yaccPatito.py',188),
  ('termino -> termino1','termino',1,'p_termino_1','yaccPatito.py',194),
  ('termino1 -> ID','termino1',1,'p_termino1_1','yaccPatito.py',200),
  ('termino1 -> ENTERO','termino1',1,'p_termino1_1','yaccPatito.py',201),
  ('termino1 -> FLOTANTE','termino1',1,'p_termino1_1','yaccPatito.py',202),
  ('termino1 -> CARACTER','termino1',1,'p_termino1_1','yaccPatito.py',203),
  ('termino1 -> OPAREN expresion CPAREN','termino1',3,'p_termino1_3','yaccPatito.py',209),
  ('estatutoRepeticionIncondicional -> DESDE ID ASSIGN expresion HASTA expresion HAZ OBRACKET estatutos CBRACKET','estatutoRepeticionIncondicional',10,'p_estatutoRepeticionIncondicional','yaccPatito.py',216),
  ('empty -> <empty>','empty',0,'p_empty','yaccPatito.py',224),
]
