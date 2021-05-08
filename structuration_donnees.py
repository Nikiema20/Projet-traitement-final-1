import csv
from datetime import date
import json

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
nom_colonnes_donnees_hospitalieres_classe_age_covid = ["numero_region","classe_age","jour","hospitalisation","reanimation","rad","décès"]
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
nom_colonnes_donnees_hospitalieres_covid = ["numero_departement","sexe","jour","hospitalisation","reanimation","rad","décès"]
fich.close()

# creation table 4 
list_lignes_donnees_hospitalieres_etablissements_covid=[]
fich = open("donnees_hospitalieres_etablissements_covid.csv","r")
lect3=csv.reader(fich , delimiter=";")
for row in lect3 : 
      ligne = [] # on rendra row  comme une liste
      ligne.append(row[0])
      annee =int( row[1][0:4]) # on retient l'année dans l'affichage de la date
      mois = int(row[1][5:7])
      jour= int(row[1][8:10])
      date_ligne = date(annee , mois , jour)
      ligne.append(date_ligne)
      ligne.append(int(row[2]))
      list_lignes_donnees_hospitalieres_etablissements_covid.append(ligne)
nom_colonnes_donnees_hospitalieres_etablissements_covid = ["numero_departement" , "jour", "nombre"]
fich.close()


list_lignes_donnees_hospitalieres_nouveaux_covid=[]
fich = open("donnees_hospitalieres_nouveaux_covid.csv","r")
lect4=csv.reader(fich , delimiter=";")
for row in lect4 : 
      ligne = [] # on rendra row  comme une liste
      ligne.append(row[0])
      annee =int( row[1][0:4]) # on retient l'année dans l'affichage de la date
      mois = int(row[1][5:7])
      jour= int(row[1][8:10])
      date_ligne = date(annee , mois , jour)
      ligne.append(date_ligne)
      ligne.append(int(row[2]))
      ligne.append(int(row[3]))
      ligne.append(int(row[4]))
      ligne.append(int(row[5]))
      list_lignes_donnees_hospitalieres_nouveaux_covid.append(ligne)
nom_colonnes_donnees_hospitalieres_nouveaux_covid = ["numero_departement" , "jour", "incident hospitalisation" , "incident reanimation" , "incident décès" , "incident rad"]
fich.close()


#table json
with open("VacancesScolaires.json") as json_file :
      covidreader = json.load(json_file)
data_calendrier=covidreader["Calendrier"]
liste_ligne_calendrier_vacancesScolaire=[]
for i in range (len(data_calendrier)):
      cle=[]
      valeur=[]
      for key,value in data_calendrier[i].items():
            valeur.append(value)
            if not key in cle:
                  cle.append(key)
      liste_ligne_calendrier_vacancesScolaire+=[valeur]
nom_colonnes_calendrier_vacancesScolaire=[]
nom_colonnes_calendrier_vacancesScolaire=cle
#print(nom_colonnes_calendrier_vacancesScolaire)
#print(liste_ligne_calendrier_vacancesScolaire)


data_academie=covidreader["Academie"]
liste_ligne_academie_vacancesScolaire=[]
for i in range (len(data_academie)):
      cle=[]
      valeur=[]
      for key,value in data_academie[i].items():
            valeur.append(value)
            if not key in cle:
                  cle.append(key)
      liste_ligne_academie_vacancesScolaire+=[valeur]
nom_colonnes_academie_vacancesScolaire=[]
nom_colonnes_academie_vacancesScolaire=cle
#print(nom_colonnes_academie_vacancesScolaire)
#print(liste_ligne_academie_vacancesScolaire)
    

