from transformation_table import TransformationTable
import datetime as d 
from table import Table

class TransformationTemporelle(TransformationTable):
    def __init__(self  , debut , fin ): # debut et fin sont de type date.time et on pourra donnc les comparer
        self.date_debut = debut 
        self.date_fin = fin
        #date debut < date fin
        

    def traiter_table(self, table): # table sera une instance de la classe table
        """ cette methode permet de surcharger la methode de la classe mère et de retourne la tabe de données contenue dans la periode donnée"""
        L=[]
        indice_date= table.nom_colonnes.index('jour') #la variable qui contient les dates, on prend sa position
        if self.date_debut==self.date_fin:
            #on est dans le cas où on veut les données d'une journée 
            #on parcourt donc chaque ligne et garde les lignes où on a la date qu'on veut 
            for ligne in table.lignes :
                if ligne[indice_date]==self.date_debut: #un problème pourrait se poser lors du test, comment entrons nous date_debut et fin pour la comparaison
                    L.append(ligne)
        elif self.date_debut< self.date_fin:
            for ligne in table.lignes:
                if ligne[indice_date] >= self.date_debut and ligne[indice_date] <= self.date_fin:
                    L.append(ligne)
        else:
            return "error"

        return Table(table.nom_colonnes,L) #ici je veux retourner un objet de type table 
