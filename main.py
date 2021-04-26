import csv
from datetime import date
from table import Table
from get_colonne import GetColonnes
from transformation_temporelle import TransformationTemporelle
#from graphique import Graphique
#from clustering import Clustering
from structuration_donnees import list_lignes_covid_hospit_incid_reg
from structuration_donnees import nom_colonnes_covid_hospit_incid_reg
from structuration_donnees import nom_colonnes_donnees_hospitalieres_classe_age_covid
from structuration_donnees import list_lignes_donnees_hospitalieres_classe_age_covid
from structuration_donnees import list_lignes_donnees_hospitalieres_covid
from structuration_donnees import nom_colonnes_donnees_hospitalieres_covid


if __name__ == "__main__":
  # creation de la table covid_hospit_incid_reg qui est une instance de la classe Table
  

  table_covid_hospit_incid_reg = Table(nom_colonnes_covid_hospit_incid_reg , list_lignes_covid_hospit_incid_reg)
  a= GetColonnes(['nom_region','reanimation'])
  #print(a.traiter_table(table_covid_hospit_incid_reg))
  d1= date(2021,1,1)
  d2= date(2021,1,31)
  b= TransformationTemporelle(d1,d2)
  print(b.traiter_table(table_covid_hospit_incid_reg))
  
  table_donnees_hospitalieres_classe_age_covid = Table(nom_colonnes_donnees_hospitalieres_classe_age_covid, list_lignes_donnees_hospitalieres_classe_age_covid)
  
  # importation de la table donnees_hospitalieres_classe_age_covid

  
  # creation de la table donnees_hospitalieres_covid
  

  table_donnees_hospitalieres_covid = Table(nom_colonnes_donnees_hospitalieres_covid, list_lignes_donnees_hospitalieres_covid)
  
  
  

  
  

  

      
   


