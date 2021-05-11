import numpy as np
from estimateur_table import EstimateurTable
import datetime as d 
from table import Table

class Moyenne(EstimateurTable):  
    def traiter_table(self, table, list_colonnes):
        '''
        methode permettant de calculer la moyenne de variables donnees

        parameters
        __________
        table: Table
            table contenant les variables 
        list_colonnes: list
            liste contenant le nom des variables
        return 
        ______
        table_moyenne: Table
            table contenant les moyennes des variables choisies 
        '''
       
        nom_colonnes_res = []
        list_ligne_moyennes = []
        n=len(table.lignes)
        moyenne_colonnes = []
        for colonne in list_colonnes:
            nom_colonnes_res.append(colonne)
            index_colonnes = table.nom_colonnes.index(colonne)
            mean=0
            for i in range(n):
                mean = mean + table.lignes[i][index_colonnes]
            mean = mean/n
            moyenne_colonnes.append(mean)
        list_ligne_moyennes.append(moyenne_colonnes)
        table_moyenne =Table(nom_colonnes_res , list_ligne_moyennes)
        
        return(table_moyenne)

        