class Jointure :
    def __init__ (self, p_nom_variable, d_nom_variable):
        self.p_nom_variable=p_nom_variable
        self.d_nom_variable=d_nom_variable
       
    def traiter(self, p_table, d_table):
         L=[]
         indice1= p_table.nom_colonnes.index(self.p_nom_variable)
         indice2= d_table.nom_colonnes.index(self.d_nom_variable)
         for p_ligne in p_table.lignes:  # Parcourir la première table
                for d_ligne in d_table.lignes: # parcourir la deuxieme table
                    if p_ligne[indice1]==d_ligne[indice2]: # Texte d'egalité
                        del(d_ligne[indice2])
                        p_ligne.extend(d_ligne)
                        L.append(p_ligne)
       
         return L