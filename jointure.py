import sqlite3 
import csv
from traitement_sql import bases
from traitement_sql import v
from abc import ABC 

class Jointure(ABC) :
    ''' classe permettant de faire la jointure 
    attrbutes
    _________
    nature: str
    '''
    def __init__ (self, nature):# la jointure est "inner", "full outer", "left outer" ...
        self.nature = nature # nature est en str
        
    
    def joindre(self, nom_table1 , nom_table2 , nom_colonne): # nom_table1 et nom_table2 son des str 
        text = "SELECT * FROM {}  {} JOIN {}  USING({} , jour)".format(nom_table1,self.nature, nom_table2 , nom_colonne )  # exactement la syntaxe SQL pour une jointure
        return(text)
  
