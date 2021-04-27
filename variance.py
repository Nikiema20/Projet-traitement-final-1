from estimateur_table import EstimateurTable
from table import Table

class Variance(EstimateurTable):
    def traiter_table(self, table, nom_colonne): #colonne est une liste contenant la colonne sur laquelle on fait la moyenne
        mean=0
        for i in range(len(nom_colonne)):
            mean+=float(nom_colonne[i])
        return mean/len(nom_colonne)