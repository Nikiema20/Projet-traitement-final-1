from transformation_table import TransformationTable
import datetime as d 
from table import Table

class TransformationSpatiale(TransformationTable):
    def __init__(self, liste_numeros):
        #la liste contient les numéros des régions ou des départements qu'on souhaite garder 
        self.liste_numeros=liste_numeros

    def traiter_table(self, table):
        #on collecte l'indice de la variable qui nous interesse 
        