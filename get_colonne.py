from transformation_table import TransformationTable
import datetime as d 
from table import Table

class GetColonnes(TransformationTable):
    ''' classe permettant de collecter des colonnes d'une table 
    attributes
    __________
    liste_colonne: list
        liste contenant le nom des colonnes
    '''
    
    def __init__(self  , liste_colonne ): 
        '''constructeur
        parameters
        __________
        liste_colonne: list
        liste contenant le nom des colonnes
        '''

        self.liste_colonne=liste_colonne

    def traiter_table(self, table):
        ''' methode de surcharge de la classe mère
        attributes
        __________
        table; Table
            la table sur laquelle on collecte les colonnes
        return 
        _______
        Table
        '''
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