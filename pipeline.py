import random as np
import sqlite3 
import csv
from abc import ABC 
from traitement_sql import bases
from traitement_sql import v
from table import Table
class Pipeline(ABC) :
    def __init__ (self, table):
        self.table=table
        #self.variable=list_va
    def centrage (self, centre_gravite):
        L=[]
        m=[]

        for ligne in self.table.lignes:
            for i in range (len(centre_gravite.lignes[0])):
                m.append(ligne[i]-centre_gravite.lignes[0][i])

            L.append(m)    
        return Table(centre_gravite.nom_colonnes,L)  
       
       
    # codage de la jointure
    def jointure(self,nom_table1 , nom_table2, nom_col):
        text = "SELECT * FROM {} JOIN {}  USING({} , jour)".format(nom_table1, nom_table2 , nom_col )  # exactement la syntaxe SQL 
        return(text) # on va appliquer la syntaxe dans le main à l'aide d'un curseur nommé v
  
