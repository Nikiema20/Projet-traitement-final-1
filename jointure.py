class Jointure :
    def __init__ (self, nature):# la jointure est "inner", "outer"
        self.nature = nature
        
    
    def joindre(self, nom_table1 , nom_table2 , nom_colonne): # nom_table1 et nom_table2 son des str 
        text = "SELECT * FROM {} {} JOIN {}  USING({} , jour)".format(nom_table1,self.nature, nom_table2 , nom_colonne )  # exactement la syntaxe SQL pour une jointure
        return(text)
        
        
        
        
        
       
    
    
   
     
        
