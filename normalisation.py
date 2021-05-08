from transformation_table import TransformationTable
from table import Table
class Normalisation (TransformationTable):
    def __init__(self  , centre_gravite ):
        self.centre_gravite=centre_gravite
        
    def traiter_table(self, table):
        L=[]
       
       
        for ligne in table.lignes:
            j=0
            m=[]
            for i in self.centre_gravite.lignes[0]:
                k= ligne[j]
                d=k-i
                j+=1
               
                
                m.append(d)
            L.append(m)
        return Table(self.centre_gravite.nom_colonnes, L) #print(m)