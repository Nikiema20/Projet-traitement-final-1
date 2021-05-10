import matplotlib.pyplot as plt
from travail.traitement_sql import bases
from travail.traitement_sql import v
from travail.aggregation import Aggregation
from abc import ABC
from datetime import date
from datetime import timedelta

class Graphique(ABC):
  def __init__(self, nom_variable, nom_table_dep , jour_debut=date(2020,5,1), jour_fin=date(2020,5,7), estimateur = "SUM" ): # par defaut, l'estimateur recherché est la somme; on pourra utiliser l'estimateur "AVG pour la moyenne "
    self.nom_variable = nom_variable
    self.jour_debut = jour_debut
    self.jour_fin = jour_fin
    self.estimateur = estimateur
    self.table_dep = nom_table_dep
  def afficher_evolution(self):
    liste_semaine1 = []
    # remplissions les composants de la semaine 1:
    semaine1= Aggregation(self.estimateur,self.jour_debut,self.jour_fin)
    res1 = v.execute(semaine1.traiter_table(self.table_dep,self.nom_variable ,"jour"))
    for ligne in res1:
      liste_semaine1.append(ligne[1])
        # remplissions la liste des valeurs pour la moyenne de la semaine2
        
    liste_semaine2 = []

        # création des dates de début et de fin pour la deuxième semaine 
    debut_semaine2 = self.jour_fin + timedelta(days=1)
    fin_semaine2= debut_semaine2 + timedelta(days=6)
    semaine2 = Aggregation(self.estimateur, debut_semaine2, fin_semaine2)
    res2 = v.execute(semaine2.traiter_table(self.table_dep,self.nom_variable,"jour"))
    for ligne in res2:
          liste_semaine2.append(ligne[1])

        
    plt.plot(list(range(1,len(liste_semaine1)+1)),liste_semaine1 , 'r',label = "semaine1".format(self.estimateur , self.nom_variable)) # 'r' signifie que cette ligne sera en rouge
    plt.plot(list(range(1,len(liste_semaine2)+1)),liste_semaine2, 'k' ,label = "semaine2".format(self.estimateur , self.nom_variable)) # 'k' signifie que cette ligne sera en noir
    plt.xlabel("Jours")
    plt.ylabel("{} des {}s".format(self.estimateur , self.nom_variable))
    plt.title("Représentation de l'évolution des {} par semaine \n pour les deux semaines allant du {} au {}".format(self.nom_variable , str(self.jour_debut),str(fin_semaine2)))
    plt.legend()
    plt.show()

  def afficher_taux(self):    
    liste_semaine1 = []
    # remplissions les composants de la semaine 1:
    semaine1= Aggregation(self.estimateur,self.jour_debut,self.jour_fin)
    res1 = v.execute(semaine1.traiter_table("donnees_hospitalieres_nouveaux_covid",self.nom_variable ,"jour"))
    for ligne in res1:
      liste_semaine1.append(ligne[1])
        # remplissions la liste des valeurs pour la moyenne de la semaine2
        
    liste_semaine2 = []

        # création des dates de début et de fin pour la deuxième semaine 
    debut_semaine2 = self.jour_fin + timedelta(days=1)
    fin_semaine2= debut_semaine2 + timedelta(days=6)
    semaine2 = Aggregation(self.estimateur, debut_semaine2, fin_semaine2)
    res2 = v.execute(semaine2.traiter_table("donnees_hospitalieres_nouveaux_covid",self.nom_variable,"jour"))
    for ligne in res2:
          liste_semaine2.append(ligne[1])
    liste_taux =  []
    for i in range(7):
      taux = (liste_semaine2[i]-liste_semaine1[i])/liste_semaine1[i]
      liste_taux.append(taux)
    plt.plot(list(range(1,len(liste_taux)+1), liste_taux , 'k' )
    plt.xlabel("Jours")
    plt.ylabel("taux d'accroissement")
    plt.title("Taux d'accroissement du nombre de {} par jour \n entre les deux semaines allant du {} au  {}".format(self.nom_variable , self.jour_debut , str(fin_semaine2)))
    plt.show()
    



        
  

        



        
        
        
