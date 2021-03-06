from table import Table
import sqlite3 
from estimateur_table import EstimateurTable
from datetime import date



class Aggregation(EstimateurTable):
  """ classe permettant des operations sur les differents echelons
  attributes
  __________
  estimateur: str
    l'estimation à appliquer 
  date_debut: date
    la date de debut 
  date_fin: date
    la date de fin
  
  
  """
  def __init__(self , estimateur, debut=date(2020,3,1), fin=date(2021,4,1)): # les date de début et de fin sont par défaut celles ci.
    self.estimateur = estimateur # on rentrera un STR: "mean" pour moyenne, "sum" pour somme etc

    self.date_debut = str(debut)
    self.date_fin = str(fin)
  
  def traiter_table(self , nom_table,colonne_estimee, colonne_discriminante): # table est la table de départ sur laquelle on devra effectuer les traitements; nomtable est la table en str
    '''
    methode permettant de realiser une estimation par un echelon 

    parameters
    __________
    nom_table: Table
      la table de depart
    colonne_estimee: str
      le nom de la variable à estimer 
    colonne_discriminante: str
      le nom de la colonne de l'echelon
    return 
    ______
    text: tuple
    '''
    text = "SELECT {}, {}({}) FROM {} WHERE jour >= '{}' AND jour <= '{}' GROUP BY {}".format(colonne_discriminante, self.estimateur , colonne_estimee, nom_table, self.date_debut, self.date_fin, colonne_discriminante)
    return(text)
  
  

      


    

  
