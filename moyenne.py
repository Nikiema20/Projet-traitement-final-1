from estimateur_table import EstimateurTable
import datetime as d 
from table import Table

class Moyenne(EstimateurTable):
    def traiter_table(table, colonne): #colonne est une liste contenant la colonne sur laquelle on fait la moyenne
        mean=0
        for i in range(len(colonne)):
            mean+=float(colonne[i])
        return mean/len(colonne)