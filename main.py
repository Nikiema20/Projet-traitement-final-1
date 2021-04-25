import csv
from datetime import date
from table import Table
#from graphique import Graphique
#from clustering import Clustering


if __name__ == "__main__":
  # creation de la table covid_hospit_incid_reg qui est une instance de la classe Table
  fich = open("covid_hospit_incid_reg.csv", "r")
  lect = csv.reader( fich, delimiter = ';')
  list_lignes_covid_hospit_incid_reg=[]
  for row in lect: 
    ligne = []
    annee =int( row[0][0:4]) # on retient l'année dans l'affichage de la date
    mois = int(row[0][5:7])
    jour= int(row[0][8:10])
    date_ligne= date(annee , mois , jour)
    ligne.append(date_ligne)
    ligne.append(row[1])
    ligne.append(row[2])
    ligne.append(int(row[3]))
    list_lignes_covid_hospit_incid_reg.append(ligne)
  fich.close()
  

  nom_colonnes = ["jour", "nom_region", "numero_region", "incid_rea"]

  table_covid_hospit_incid_reg = Table(nom_colonnes , list_lignes_covid_hospit_incid_reg)
   
  # importation de la table donnees_hospitalieres_classe_age_covid
  list_lignes_donnees_hospitalieres_classe_age_covid=[]
  fich1 = open("donnees_hospitalieres_classe_age_covid.csv","r")
  lect1=csv.reader(fich1 , delimiter=";")
  for row in lect1 : 
      ligne = [] # on rendra row  comme une liste
      ligne.append(row[0])
      ligne.append(row[1])
      annee =int( row[2][0:4]) # on retient l'année dans l'affichage de la date
      mois = int(row[2][5:7])
      jour= int(row[2][8:10])
      date_ligne = date(annee , mois , jour)
      ligne.append(date_ligne)
      ligne.append(int(row[3]))
      ligne.append(int(row[4]))
      ligne.append(int(row[5]))
      ligne.append(int(row[6]))
      list_lignes_donnees_hospitalieres_classe_age_covid.append(ligne)
  nom_colonnes_donnees_hospitalieres_classe_age_covid = ["reg","classe_age","jour","hospitalisation","reanimation","rad","décès"]
  table_donnees_hospitalieres_classe_age_covid = Table(list_lignes_donnees_hospitalieres_classe_age_covid,nom_colonnes_donnees_hospitalieres_classe_age_covid)
  fich.close()
  
  # creation de la table donnees_hospitalieres_covid
  
  list_lignes_donnees_hospitalieres_covid=[]
  fich = open("donnees_hospitalieres_covid.csv","r")
  lect2=csv.reader(fich1 , delimiter=";")
  for row in lect2 : 
      ligne = [] # on rendra row  comme une liste
      ligne.append(row[0])
      ligne.append(row[1])
      annee =int( row[2][0:4]) # on retient l'année dans l'affichage de la date
      mois = int(row[2][5:7])
      jour= int(row[2][8:10])
      date_ligne = date(annee , mois , jour)
      ligne.append(date_ligne)
      ligne.append(int(row[3]))
      ligne.append(int(row[4]))
      ligne.append(int(row[5]))
      ligne.append(int(row[6]))
      list_lignes_donnees_hospitalieres_covid.append(ligne)
  nom_colonnes_donnees_hospitalieres_covid = ["departement","sexe","jour","hospitalisation","reanimation","rad","décès"]
  table_donnees_hospitalieres_covid = Table(list_lignes_donnees_hospitalieres_covid,nom_colonnes_donnees_hospitalieres_covid)
  fich.close()
      
   


