from transformation_table import TransformationTable
import datetime as d 

class TransformationTemporelle(TransformationTable):
    def __init__(self  , debut , fin ): # debut et fin sont de type date.time et on pourra donnc les comparer
        self.date_debut = debut 
        self.date_fin = fin
        

    def traiter_table(self, table): # table sera une instance de la classe table
        """ cette methode permet de surcharger lamethode de la classe mère et de retourne la tabe de données contenue dans la periode donnée"""
