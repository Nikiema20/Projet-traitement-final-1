from estimateur_table import EstimateurTable
import datetime as d 
from table import Table

class Somme(EstimateurTable): # on va afficher le resultat sous forme d'une table 
    def traiter_table(self, table, list_colonnes): #colonne est une liste contenant les colonnes sur lesquelles on fait le calcul de la moyenne
        nom_colonnes_res = []
        list_ligne_somme=[]
        n=len(table.lignes)
        somme_colonnes = []
        for colonne in list_colonnes:
            nom_colonnes_res.append(colonne)
            index_colonnes = table.nom_colonnes.index(colonne)
            somme=0
            mean=0
            for i in range(n):
                mean = mean + table.lignes[i][index_colonnes]
            somme =mean
            somme_colonnes.append(somme)
        list_ligne_somme.append(somme_colonnes)
        table_somme= Table(nom_colonnes_res, list_ligne_somme)
        return( table_somme)