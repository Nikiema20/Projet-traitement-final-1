import csv
from datetime import date
from table import Table
from get_colonne import GetColonnes
from transformation_temporelle import TransformationTemporelle
from importation_donnee import Importation_donnee
from transformation_spatiale import TransformationSpatiale
from moyenne import Moyenne
from somme import Somme
from graphique import Graphique
import sqlite3 
from traitement_sql import v
bases = sqlite3.connect(':memory:')
from aggregation import Aggregation
from kmeans import KMeans

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
from structuration_donnees import liste_ligne_academie_vacancesScolaire
from structuration_donnees import nom_colonnes_academie_vacancesScolaire
from structuration_donnees import liste_ligne_calendrier_vacancesScolaire
from structuration_donnees import nom_colonnes_calendrier_vacancesScolaire
from jointure import Jointure





if __name__ == "__main__":
  # creation des differentes tables
   
  #nom_colonnes_covid_hospit_incid_reg = ["jour", "nom_region", "numero_region", "reanimation"]
  #nom_colonnes_donnees_hospitalieres_classe_age_covid = ["reg","classe_age","jour","hospitalisation","reanimation","rad","dÃ©cÃ¨s"]
  #nom_colonnes_donnees_hospitalieres_covid = ["numero_departement","sexe","jour","hospitalisation","reanimation","rad","dÃ©cÃ¨s"]
  #nom_colonnes_donnees_hospitalieres_etablissement_covid=["numero_departement","jour","nombre"]
  #nom_colonnes_donnees_hospitalieres_nouveaux_covid = ["numero_departement" , "jour", "incident hospitalisation" , "incident reanimation" , "incident décès" , "incident rad"]

  #colonnes provenant du fichier json
  #nom_colonnes_academie_vacancesScolaire=['id', 'Code_Dpt', 'Dpt', 'Region', 'Academie', 'Zone', 'NomAcademie', 'Departement']
  #nom_colonnes_calendrier_vacancesScolaire=['id', 'Description', 'DateDebut', 'DateFin', 'Zone', 'annee_scolaire', 'Debut', 'Fin']
  
  
  table_covid_hospit_incid_reg = Table(nom_colonnes_covid_hospit_incid_reg , list_lignes_covid_hospit_incid_reg)
  table_donnees_hospitalieres_classe_age_covid = Table(nom_colonnes_donnees_hospitalieres_classe_age_covid, list_lignes_donnees_hospitalieres_classe_age_covid)
  table_donnees_hospitalieres_covid = Table(nom_colonnes_donnees_hospitalieres_covid, list_lignes_donnees_hospitalieres_covid)
  table_donnees_hospitalieres_etablissements_covid = Table(nom_colonnes_donnees_hospitalieres_etablissements_covid , list_lignes_donnees_hospitalieres_etablissements_covid)
  table_donnees_hospitalieres_nouveaux_covid = Table(nom_colonnes_donnees_hospitalieres_nouveaux_covid , list_lignes_donnees_hospitalieres_nouveaux_covid)
  
  table_academie_vacancesScolaire= Table(nom_colonnes_academie_vacancesScolaire,liste_ligne_academie_vacancesScolaire)
  table_calendrier_vacancesScolaire= Table(nom_colonnes_calendrier_vacancesScolaire, liste_ligne_calendrier_vacancesScolaire)
  
  
  # Les donnees des regions et des departements s'etendent du 18 mars 2020 au 3 mars 2021
  
  #Question 1: nombre total d'hospitalisation du au covid
  
  #Pour obtenir le nombre total, on fera la somme des hospitalisations sur la table contenant les regions et les classes d'ages
  # , à priori le nombre devrait être le même en utilisant les departements
  n=Somme()
  list_col = [ "hospitalisation"]
  res1= n.traiter_table(table_donnees_hospitalieres_classe_age_covid,list_col)
  print(res1)


  #question 2: le nombre de nouvelles hospitalisations durant les 7 derniers jours dans chaque département
  # on supposera au vue des donnees que nous sommes à la date du 27-12-2020
  d1=date(2020,12,19)
  d2=date(2020,12,26) # on aura les donnes du 19 au 26 car la comparaison est stricte dans la classe transformation temporelle
  a= Aggregation("SUM", d1, d2)
  resu= a.traiter_table("donnees_hospitalieres_nouveaux_covid", "incident_hospitalisation", "numero_departement")
  r=v.execute(resu)
  for i in r:
    print(i)

  #question 3: evolution de la moyenne des nouvelles hospitalisations journalieres de cette semaine par rapport à la semaine derniere
  #on fera donc deux courbes pour les comparaisons, une semaine sera consideree comme une succession de 7 jours 

  
  h = Graphique("incident_hospitalisation","donnees_hospitalieres_nouveaux_covid",date(2020,12,14) , date(2020,12,20), "AVG")
  h.afficher_evolution()
  #h.afficher_taux()

  # Question 4 : Kmeans avec k=3 sur les données des departements du mois de janvuers 2021, lisser avec une moyenne glissante de 7 jours
  # 1-charger les données de departement 
  table_donnees_hospitalieres_nouveaux_covid = Table(nom_colonnes_donnees_hospitalieres_nouveaux_covid , list_lignes_donnees_hospitalieres_nouveaux_covid)
  
  # 1-selectionner les données de janvier 2021
  d1= date(2021,1,1)
  d2= date(2021,1,31)
  b= TransformationTemporelle(d1,d2)
  donnee_janvier_2021=b.traiter_table(table_donnees_hospitalieres_covid)
  #print(donnee_janvier_2021)
  
  #2- selection les variables quantitatives de la base donnee_janvier_2021
  p=[ 'hospitalisation', 'reanimation', 'rad', 'décès']
  n= GetColonnes(p)
  
  donnee_janvier_2021_variables_quantitaives=n.traiter_table(table_donnees_hospitalieres_covid)
 # print(donnee_janvier_2021_variables_quantitaives)
  
  #3- lissage des données pour une moyenne glissantes de 7 jours
  # Création d'une instance Kmean
  z=KMeans(3)
  donnee_janvier_glissante=Table(p,z.moyenne_glissante_tableau(donnee_janvier_2021_variables_quantitaives,7))
  #print(donnee_janvier_glissante)
  
  #4- Faire le Kmeans
  # Centrée les donnes
  # calcul le centre de gravité
  m= Moyenne()
  centre_gravite = m.traiter_table(donnee_janvier_glissante,p)
  #print(centre_gravite)
  
  # - centre les données
  donnee_janvier_glissante_centre=z.normalisation(donnee_janvier_glissante, centre_gravite)
  #print(donnee_janvier_glissante_centre)
  
  # - inialiser les centres des classse
  centre_initiale=z.initialisation_centres(donnee_janvier_glissante_centre)
 # print(centre_initiale)

   # Creation des cluster
  clusters=z.creation_clusters(donnee_janvier_glissante_centre,centre_initiale)
 # print(Table(p,clusters))
  
  # Nombre individus dans les clusters
  nombre_classe=z.taille_cluster(clusters)
  #print(nombre_classe)
 
  


  # #Question 5: nouvelles admissions en reanimations la semaine après les vacances de Toussaint
  # Après visualisation de la table des vacances scolaires, les vacances de toussaint d'etalent du 17-10-2020 au 02-11-2020 et ce pour les zones A,B et C
  # On donnera donc le resultat uniquement sur la zone A
  deb= TransformationTemporelle(date(2020,11,3),date(2020,11,10))
  t1= deb.traiter_table(table_donnees_hospitalieres_nouveaux_covid)
  mid=TransformationSpatiale( [69,38,25,33,63,21,87,86] )
  fin=mid.traiter_table(t1, "numero_departement")
  s=Somme()
  result=s.traiter_table(fin, ["incident_reanimation"])
  print(result)
  #ATTENTION CE CODE MET DU TEMPS PAR MOMENT AVANT AFFICHAGE. L'IDEE SERAIT DE METTRE LES AUTRES PRINT EN COMMENTAIRE AVANT DE LE LANCER


  
  


