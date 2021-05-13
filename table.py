class Table:
  ''' classe qui permet de instancier  les tables initiales
    attributes
    __________
    nom_colonnes: list
      liste des noms des colonnes 
    lignes: list[list]
      liste des lignes de la table 
  '''
  def __init__(self , nom_col , list_lignes):
    
    self.nom_colonnes = nom_col # nom_colonnes est la liste des noms des colonnes de la table 
    self.lignes = list_lignes # list_lignes contiendra la liste des lignes de la tables
  

  def ajouter_lignes(self , ligne, position=-1): # l'élément est par défaut ajouté à la fin de la table 
    """ Cette fonction permet d'ajouter une ligne à une table à la position souhaitée 
     paramètres
     ___________
     ligne : list
     ligne une observation de la table
     
     return  :
         Elle retourne une table
    """
    
    if len(ligne)==len(self.nom_colonnes):  # si on a bien un meme nombre de colonnes que la table de départ...
      self.lignes.insert(position, ligne) # on inserre la liste ne question à cette position
    
  def supprimer_ligne(self , position):
    ''' suppression d'une ligne d'une table donnee
    paramètres
    ___________
    position : int
    prendre la position de la ligne à supprimer
    
    return :
        Elle retourne une table
    '''
    if position < len(self.lignes -1): # si il existe une ligne à cette position ...
      self.lignes.remove(self.lignes[position]) # on la supprime

  def ajouter_colonne(self, nom_colonne , valeurs_colonnes , position_colonne=-1):
    '''
    ajout d'une colonne a une table 
    parameters
    __________
    nom_colonne: str
      nom de la colonne
    valeurs_colonnes: list
    
    return :
        Elle retourne une table
    '''
    self.nom_colonnes.insert( position_colonne , nom_colonne)
    for i in range(len(self.lignes)):
      self.lignes[i].insert(position_colonne, valeurs_colonnes[i])
  
  def supprimer_colonne(self, position=-1):
    ''' suppression d'une colonne
    '''
    if position < len(self.nom_colonnes):
      self.nom_colonnes.remove(self.nom_colonnes[position])
      for i in range(len(self.lignes)):
        self.lignes[i].remove[self.lignes[i][position]]

  def __str__(self):
    '''
    methode permettant d'afficher une table dans tous ses formats conventionnels
    
    return : 
        Elle retourne une table 
    '''
    affichage = ""
    for nom_colonne in self.nom_colonnes[:-1]:
      affichage=affichage + nom_colonne+"; "
    affichage = affichage + self.nom_colonnes[-1] + "\n"
    for ligne in self.lignes:
      
      affichage_liste = ""
      for i in range(len(ligne)-1):
        affichage_liste= affichage_liste+ "{0"+"["+str(i)+"]" + "} ; "
      affichage_liste = affichage_liste + "{0"+"["+str(len(ligne)-1)+"]" + "} "
      
      liste_format = []
      for i in ligne:
        liste_format.append(i)
      affichage_liste = affichage_liste.format(liste_format)
      affichage = affichage + affichage_liste
      affichage += "\n"
      
    return(affichage)
    
   


        
        


    





