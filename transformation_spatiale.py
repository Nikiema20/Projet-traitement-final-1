from transformation_table import TransformationTable
from table import Table

class TransformationSpatiale(TransformationTable):
    def __init__(self, liste_numeros):
        #la liste contient les numéros des régions ou des départements qu'on souhaite garder 
        self.liste_numeros=liste_numeros

    def traiter_table(self, table,nom_variable):
       
        """ cette methode permet de surcharger la methode de la classe mère et de retourne la tabe de données contenue dans la periode donnée"""
        L=[]
        indice= table.nom_colonnes.index(nom_variable) #la variable qui contient les dates, on prend sa position
     

            #on est dans le cas où on veut les données d'une journée 
            #on parcourt donc chaque ligne et garde les lignes où on a la date qu'on veut 
        for ligne in table.lignes :
            if ligne[indice] == str(self.liste_numeros ): #un problème pourrait se poser lors du test, comment entrons nous date_debut et fin pour la comparaison
                L.append(ligne)
           
       

        return Table(table.nom_colonnes,L) #Table(table.nom_colonnes,L) #ici je veux retourner un objet de type table
        #on collecte l'indice de la variable qui nous interesse 
        