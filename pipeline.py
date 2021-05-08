import random as np

 
from table import Table
class Pipeline :
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