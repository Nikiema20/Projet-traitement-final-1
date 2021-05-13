import unittest 
import importation_donnee as jd 
import kmeans as k
import structuration_donnees as m

class JeuxTest(unittest.TestCase): 

 
    def test_importe_classe(self): 
        test1 = jd.Importation_donnee('P:/Projet_de_Traitemant/projet 8/Projet-traitement-final-1/','covid_hospit_incid_reg.csv') 
    
        self.assertIsInstance(test1, jd.Importation_donnee) 
         
         
    def test_import_donnee(self): 
         test1 = jd.Importation_donnee('P:/Projet_de_Traitemant/projet 8/Projet-traitement-final-1/','covid_hospit_incid_reg.csv') 
          
         self.assertTrue(test1.import_csv()) 
   
          
    def test_lien_fichier(self): 
        test1 = jd.Importation_donnee('P:/Projet_de_Traitemant/projet 8/Projet-traitement-final-1/','VacancesScolaires.json') 
        self.assertTrue(test1.import_json())
     
    def test_centre_gravite(self):
        test2=m.list_lignes_covid_hospit_incid_reg
        self.assertTrue(test2)
    
    def test_kmeans(self): 
        test1 = k.KMeans(3)
        self.assertTrue(test1)
unittest.main() 

