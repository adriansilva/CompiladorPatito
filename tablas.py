"""
class TablaFuncion:
    self.nombre = None
    self.tipo = None
    self.tablaVariable = None

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo



class TablaVariable:
    self.nombre = None
    self.tipo = None
    self.dirAlmacenamiento = None

    def __init__(self, nombre, tipo, dirAlmacenamiento):
        self.nombre = nombre
        self.tipo = tipo
        self.dirAlmacenamiento = dirAlmacenamiento
"""
import pandas as pd

class ManejadorDeTablas:
    base_dataframe_variables = [['Nombre','Valor']]
    df_variables = pd.DataFrame(base_dataframe_variables)
    base_dataframe_funciones = [['Nombre','Tabla de Variables'],['PROGRAMA',df_variables]]
    self.tablaFunciones = pd.DataFrame(base_dataframe_funciones)
    def __init__(self):
        self.nombre = nombre
        self.tipo = tipo
