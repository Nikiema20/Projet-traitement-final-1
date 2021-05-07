import csv
from datetime import date
from table import Table
from get_colonne import GetColonnes
from transformation_temporelle import TransformationTemporelle
from importation_donnee import Importation_donnee
from transformation_spatiale import TransformationSpatiale
from moyenne import Moyenne

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



if __name__ == "__main__":
  # creation des differentes tables
   
  #nom_colonnes_covid_hospit_incid_reg = ["jour", "nom_region", "numero_region", "reanimation"]
  #nom_colonnes_donnees_hospitalieres_classe_age_covid = ["reg","classe_age","jour","hospitalisation","reanimation","rad","dÃ©cÃ¨s"]
  #nom_colonnes_donnees_hospitalieres_covid = ["numero departement","sexe","jour","hospitalisation","reanimation","rad","dÃ©cÃ¨s"]
  #nom_colonnes_donnees_hospitalieres_etablissement_covid=["numero departement","jour","nombre"]
  #nom_colonnes_donnees_hospitalieres_nouveaux_covid = ["numero departement" , "jour", "incident hospitalisation" , "incident reanimation" , "incident décès" , "incident radio"]

  table_covid_hospit_incid_reg = Table(nom_colonnes_covid_hospit_incid_reg , list_lignes_covid_hospit_incid_reg)
  table_donnees_hospitalieres_classe_age_covid = Table(nom_colonnes_donnees_hospitalieres_classe_age_covid, list_lignes_donnees_hospitalieres_classe_age_covid)
  table_donnees_hospitalieres_covid = Table(nom_colonnes_donnees_hospitalieres_covid, list_lignes_donnees_hospitalieres_covid)
  table_donnees_hospitalieres_etablissements_covid = Table(nom_colonnes_donnees_hospitalieres_etablissements_covid , list_lignes_donnees_hospitalieres_etablissements_covid)
  table_donnees_hospitalieres_nouveaux_covid = Table(nom_colonnes_donnees_hospitalieres_nouveaux_covid , list_lignes_donnees_hospitalieres_nouveaux_covid)

  #Question 1: nombre total d'hospitalisation du au covid
  #Pour obtenir le nombre total, on fera la somme des hospitalisations dans les departements
  
  
  
  """a= GetColonnes(['nom_region','reanimation'])
  #print(a.traiter_table(table_covid_hospit_incid_reg))
  d1= date(2021,1,1)
  d2= date(2021,1,31)
  b= TransformationTemporelle(d1,d2)
  """
  #print(b.traiter_table(table_covid_hospit_incid_reg))"""
  # print(b.traiter_table(table_covid_hospit_incid_reg)) departement
  #k= TransformationSpatiale([6,94,44])
  #print(k.traiter_table(table_covid_hospit_incid_reg, "numero_region" ))

  
  #print(table_donnees_hospitalieres_covid)
  #covid_hospit=Importation_donnee('P:\\Projet_de_Traitemant\\Projet\\',"donnees_hospitalieres_covid.csv")
  #df=covid_hospit.import_csv()
  #df1 = df.pop(0)
  #print(covid_hospit.import_csv())
  #print(df)
  m = Moyenne()
  list_col = ["reanimation" , "hospitalisation"]
  res = m.traiter_table(table_donnees_hospitalieres_classe_age_covid,list_col)
  print(res)
  

 

  
  



      
   


