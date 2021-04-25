class Table:
  def __init__(self , nom_col , list_lignes):
    self.nom_colonnes = nom_col # nom_colonnes est la liste des noms des colonnes de la table 
    self.lignes = list_lignes # list_lignes contiendra la liste des lignes de la tables
  

  def ajouter_lignes(self , ligne, position=-1): # l'élément est par défaut ajoouté à la fin de la table 
    """ Cette fonction permet d'ajouter une ligne à une table à la position souhaitée """
    if len(ligne)==len(self.nom_colonnes):  # si on a bien un meme nombre de colonnes que la table de départ...
      self.lignes.insert(position, ligne) # on inserre la liste ne question à cette position
    
  def supprimer_ligne(self , position):
    if position < len(self.lignes -1): # si il existe une ligne à cette position ...
      self.lignes.remove(self.lignes[position]) # on la supprime

  def ajouter_colonne(self, nom_colonne , valeurs_colonnes , position_colonne=-1):
    self.nom_colonnes.insert( position_colonne , nom_colonne)
    for i in range(len(self.lignes)):
      self.lignes[i].insert(position_colonne, valeurs_colonnes[i])
  
  def supprimer_colonne(self, position=-1):
    if position < len(self.nom_colonnes):
      self.nom_colonnes.remove(self.nom_colonnes[position])
      for i in range(len(self.lignes)):
        self.lignes[i].remove(self.lignes[i][position])
  








