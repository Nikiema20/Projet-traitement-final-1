mport numpy as np
import matplotlib.pyplot as plt
from table import Table
 
class KMeans :
    def __init (self, table,nombre_classe):
        self.table= table
        self.nombre_classe=nombre_classe
        self.max_iterations=1000
        self.nombre_ligne=len(self.table.lignes)
        self.nombre_colonne=len(self.table.nom_colonnes)



    def moyenne(self,liste):

        somme = 0
        effectif = len(list)
        for i in range(effectif):
            somme = somme + liste[i]
        moyenne = somme / effectif
        return moyenne 


    def moyenne_ligne(self, tableau):


        resu = []
        for i in range( tableau.nom_colonnes):
            resu.append(self.moyenne(tableau.lignes[i]))  
        return resu

    def moyenne_colonne(self, tableau):

        Y = np.asarray(self.tableau.lignes)
        trans = np.transpose(Y)
        tab= tolist(trans)
        resu = self.moyenne_ligne(tab)
        return resu   