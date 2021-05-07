from estimateur_table import EstimateurTable
import datetime as d 
from table import Table

class Moyenne(EstimateurTable): # on va afficher le resultat sous forme d'une table 
    def traiter_table(self, table, list_colonnes): #colonne est une liste contenant les colonnes sur lesquelles on fait le calcul de la moyenne
        nom_colonnes_res = []
        list_ligne_moyennes = []
        list_ligne_somme=[]
        n=len(table.lignes)
        moyenne_colonnes = []
        moyenne_ligne=[]
        for colonne in list_colonnes:
            nom_colonnes_res.append(colonne)
            index_colonnes = table.nom_colonnes.index(colonne)
            somme=0
            mean=0
            for i in range(n):
                mean = mean + table.lignes[i][index_colonnes]
            somme =mean
            mean = mean/n
            moyenne_colonnes.append(mean)
            moyenne_ligne.append(somme)
        list_ligne_somme.append(moyenne_ligne)
        list_ligne_moyennes.append(moyenne_colonnes)
        table_moyenne =Table(nom_colonnes_res , list_ligne_moyennes)
        table_somme= Table(nom_colonnes_res, list_ligne_moyennes)
        return(table_moyenne)

        