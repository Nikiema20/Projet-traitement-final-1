import csv
from datetime import date

#from graphique import Graphique
#from clustering import Clustering

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
nom_colonnes_covid_hospit_incid_reg = ["jour", "nom_region", "numero_region", "reanimation"]


# creation table 2 

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
fich.close()


# creation table 3 

list_lignes_donnees_hospitalieres_covid=[]
fich = open("donnees_hospitalieres_covid.csv","r")
lect2=csv.reader(fich , delimiter=";")
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