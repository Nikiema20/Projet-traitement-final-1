        
from transformation_table import TransformationTable
import datetime as d 
from table import Table

class GetColonnes(TransformationTable):
    def __init__(self  , liste_colonne ): 
        self.liste_colonne=liste_colonne

    def traiter_table(self, table):
        L=[] #liste qui contiendra les nouvelles lignes de notre nouvelle table 
        M=[]
        for name in self.liste_colonne:
            M.append(table.nom_colonnes.index(name)) #on collecte les indices de positions des colonnes à garder
        for ligne in table.lignes:
            N=[]
            for indice in M:
                N.append(ligne[indice])
            L.append(N)
        return Table(self.liste_colonne, L)