from transformation_table import TransformationTable
from table import Table

class TransformationSpatiale(TransformationTable):
    ''' classe qui applique un filtre pour un espace donné
        attributes
        _________
        liste_numeros: list
            numero des departements ou region qu'on souhaite conserver
    '''
    def __init__(self, liste_numeros):   
        self.liste_numeros=liste_numeros

    def traiter_table(self, table,nom_variable):
       
        ''' methde permettant d'executer le filtre 
        parameters
        __________
        table: Table
        nom_variable: str
            nom de la variable sur laquelle on applique le filtre

        return
        ______
        Table
        '''

        L=[]
        indice= table.nom_colonnes.index(nom_variable) 
     
        for numero in self.liste_numeros:
          for ligne in table.lignes :
            if ligne[indice] == str(numero): 
                L.append(ligne)
           
       

        return Table(table.nom_colonnes,L)  
        
