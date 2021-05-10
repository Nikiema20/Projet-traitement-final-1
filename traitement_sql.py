import sqlite3 
bases = sqlite3.connect(':memory:')

import csv

import estimateur_table 
import operation_de_tables
import transformation_table
import get_colonne
import importation_donnee

import structuration_donnees
import table
import moyenne

import transformation_spatiale
import transformation_temporelle
from datetime import date
from table import Table
from get_colonne import GetColonnes
from transformation_temporelle import TransformationTemporelle
from importation_donnee import Importation_donnee
from transformation_spatiale import TransformationSpatiale
from moyenne import Moyenne
from aggregation import Aggregation
#from graphique import Graphique
#from clustering import Clustering

from structuration_donnees import list_lignes_covid_hospit_incid_reg
from structuration_donnees import nom_colonnes_covid_hospit_incid_reg
from structuration_donnees import nom_colonnes_donnees_hospitalieres_classe_age_covid
from structuration_donnees import list_lignes_donnees_hospitalieres_classe_age_covid
from structuration_donnees import list_lignes_donnees_hospitalieres_covid
from structuration_donnees import nom_colonnes_donnees_hospitalieres_covid
from structuration_donnees import nom_colonnes_donnees_hospitalieres_etablissements_covid
from structuration_donnees import nom_colonnes_donnees_hospitalieres_nouveaux_covid
from structuration_donnees import list_lignes_donnees_hospitalieres_etablissements_covid
from structuration_donnees import list_lignes_donnees_hospitalieres_nouveaux_covid 

table_covid_hospit_incid_reg = Table(nom_colonnes_covid_hospit_incid_reg , list_lignes_covid_hospit_incid_reg)
table_donnees_hospitalieres_classe_age_covid = Table(nom_colonnes_donnees_hospitalieres_classe_age_covid, list_lignes_donnees_hospitalieres_classe_age_covid)
  
  # importation de la table donnees_hospitalieres_classe_age_covid
  
  # creation de la table donnees_hospitalieres_covid
  

table_donnees_hospitalieres_covid = Table(nom_colonnes_donnees_hospitalieres_covid, list_lignes_donnees_hospitalieres_covid)
table_donnees_hospitalieres_etablissements_covid = Table(nom_colonnes_donnees_hospitalieres_etablissements_covid , list_lignes_donnees_hospitalieres_etablissements_covid)
table_donnees_hospitalieres_nouveaux_covid = Table(nom_colonnes_donnees_hospitalieres_nouveaux_covid , list_lignes_donnees_hospitalieres_nouveaux_covid)
v = bases.cursor()
v.execute("""CREATE TABLE covid_hospit_incid_reg (jour_text , nom_region_text , numero_region_integer , reanimation_integer)""")
l_covid_hospit_incid_reg= []
for ligne in table_covid_hospit_incid_reg.lignes:
    vrai_ligne = (str(ligne[0]), ligne[1], ligne[2], ligne[3])
    l_covid_hospit_incid_reg.append(vrai_ligne)
v.executemany("INSERT INTO covid_hospit_incid_reg VALUES (?,?,?,?)", l_covid_hospit_incid_reg)
  
 
  # création de la deuxième table donnees_hospitalieres_classe_age_covid en sql
v.execute("""CREATE TABLE donnees_hospitalieres_classe_age_covid (reg_text , classe_age_text, jour text, hospitalisation integer, reanimation integer, rad integer, décès integer) """)
l_donnees_hospitalieres_classe_age_covid=[]
for ligne in table_donnees_hospitalieres_classe_age_covid.lignes:
    vrai_ligne=(ligne[0],ligne[1],str(ligne[2]),ligne[3], ligne[4],ligne[5],ligne[6])
    l_donnees_hospitalieres_classe_age_covid.append(vrai_ligne)
v.executemany("INSERT INTO donnees_hospitalieres_classe_age_covid VALUES (?,?,?,?,?,?,?)", l_donnees_hospitalieres_classe_age_covid)

  





  # creation de la table donnees_hospitalieres_covid

v.execute("""CREATE TABLE donnees_hospitalieres_covid(numero_department text , sexe text, jour text, hospitalisation integer, reanimation integer, rad integer, décès integer) """)

l_donnees_hospitalieres_covid =[]

for ligne in table_donnees_hospitalieres_covid.lignes:
    vrai_ligne=(ligne[0],ligne[1],str(ligne[2]),ligne[3], ligne[4],ligne[5],ligne[6])
    l_donnees_hospitalieres_covid.append(vrai_ligne) 
v.executemany("INSERT INTO donnees_hospitalieres_covid VALUES (?,?,?,?,?,?,?)", l_donnees_hospitalieres_covid)

  # creation de la table donnees_hospitalieres_etablissements_covid

v.execute("""CREATE TABLE donnees_hospitalieres_etablissements_covid(numero_department text , jour text, nombre integer) """)
l_donnees_hospitalieres_etablissements_covid =[]
for ligne in table_donnees_hospitalieres_etablissements_covid.lignes:
    vrai_ligne = (ligne[0],str(ligne[1]),ligne[2])
    l_donnees_hospitalieres_etablissements_covid.append(vrai_ligne)
v.executemany("INSERT INTO donnees_hospitalieres_etablissements_covid VALUES (?,?,?)", l_donnees_hospitalieres_etablissements_covid)


   #creation de la table donnees_hospitalieres_nouveaux_covid

v.execute("""CREATE TABLE donnees_hospitalieres_nouveaux_covid(numero department text , jour text, incident_hospitalisation integer, incident_reanimation integer, incident_décès integer, incident_rad integer) """)

l_donnees_hospitalieres_nouveaux_covid =[]

for ligne in table_donnees_hospitalieres_nouveaux_covid.lignes:
    vrai_ligne=(ligne[0],str(ligne[1]),ligne[2],ligne[3], ligne[4],ligne[5])
    l_donnees_hospitalieres_nouveaux_covid.append(vrai_ligne) 
v.executemany("INSERT INTO donnees_hospitalieres_nouveaux_covid VALUES (?,?,?,?,?,?)", l_donnees_hospitalieres_nouveaux_covid)




  

  

    
  
  
  
  #v.execute("INSERT INTO covid_hospit_incid_reg (nom_region , numero_region , reanimation) VALUES (ligne[1],ligne[2],ligne[3])")
