import numpy as np
#import matplotlib.pyplot as plt
from table import Table
import math
class KMeans :
    def __init__(self, nombre_classe):
        self.nombre_classe=nombre_classe
        self.max_iteration=1000

    def moyenne(self,liste):

        somme = 0
        effectif = len(liste)
        for i in range(effectif):
            somme = somme + liste[i]
        if effectif==0:
            effectif+=0.01
            moyenne = somme / effectif
        else :
          moyenne = somme / effectif  
        return moyenne 

    

        
    def moyenne_ligne(self, tableau_liste):
# tableau =_liste est une liste de liste 
        resu = []
        for i in range( len(tableau_liste)):
            resu.append(self.moyenne(tableau_liste[i]))  
        return resu

    def moyenne_colonne(self, tableau):

        Y = np.asarray(tableau)
        trans = np.transpose(Y)
        tab= trans.tolist()
        resu = self.moyenne_ligne(tab)
        return resu  
        
        
    
    def liste_distance(self,X,Y ):

        
        
         
        # On calcule les distances du point à l'ensemble des centres de classe
        liste = []
        
        for ligne in range(self.nombre_classe):
            somme=0
            for j in range(len(Y)):
                somme=somme + math.sqrt((X[j]-Y[ligne][j])**2)
            liste.append(somme)
        #return len(Y) #liste.append( somme )
        return liste
        #for i in range(self.nombre_classe):
        #    liste.append(math.sqrt(sum([(a-b) ** 2 for a, b in zip(X, Y[i])])))
       # return liste      
        
        
    def initialisation_centres(self, tables):
                
        table=np.array(tables.lignes)
        centres = np.zeros((self.nombre_classe, table.shape[1]))
        for k in range(self.nombre_classe):
            centre = table[np.random.choice(range(table.shape[0]))]
            centres[k] = centre
        return centres


    def creation_clusters(self,  table, centres):
        '''
         X: array numpy  (matrice des données)
        centres: liste des centres
        '''
        X=np.array(table.lignes)
        # Création d'une liste contenant l'ensemble des points affectés à chaque cluster
        clusters =[] # [[] for _ in range(self.nombre_classe)]

        # On cherche le centre de classe le plus proche de notre point 
        for j in range(self.nombre_classe):
            m=[]
            for indice_point, point in enumerate(X):
                centre_voisin = np.argmin(self.liste_distance(point,centres))
                #clusterappend(centre_voisin)
                m.append(centre_voisin)
            clusters.append(m)    
    
        return clusters

        
        
        
    def nouveau_centres(self, clusters, table):
        X=np.array(table.lignes)       
        # On définit les nouveaux centres comme moyenne des points appartenant à la classe
        centres = np.zeros((self.nombre_classe, X.shape[1]))
        for indice, cluster in enumerate(clusters):
            #w=Table.traiter_table(X[cluster])
            nouveau_centre = self.moyenne_colonne(X[cluster])
            centres[indice] = nouveau_centre
        return centres

        
        
        
    def taille_cluster (self,clusters):
        m=[]
        
        for ligne in range(self.nombre_classe):
            somme=0
            for j in range(len(clusters[1])):
                 if clusters[ligne][j]==ligne:
                     somme+=1
            m.append(somme) #print(j[ligne])
        return m       
                #if ligne==clusters:
                 #  somme+=1
           # m.append(somme)
        #return m
    
    def prediction_classe(self, clusters, X):
               
        # On crée la liste des clusters en affectant à chaque individu sa classe
        
        classification =[] # np.zeros(X.shape[0])
        for indice_classe, cluster in enumerate(clusters):
            m=[]
            for indice_individu in cluster:
                m.append(indice_classe)
            classification.append(m)
                #classification[indice_individu] = indice_classe
        return classification

        
    def variance(self, X):
       
        somme = 0
        effectif = len(X)
        for i in range(effectif):
            somme = somme + (X[i] - self.moyenne(X))**2
        variance = somme / effectif
        return variance
    
    def ecart_type(self, X):
         
        return (self.variance(X)**0.5)  
    
        
    def moyenne_mobile(self, X, ecart):
        '''
        ecart :  le pas
        '''
        
        sortie = [sum(X[0:ecart]) / ecart, ]
        for i in range(ecart, len(X)):
            sortie.append(sortie[-1] - X[i - ecart] / ecart + X[i] / ecart)
        return sortie    
        
    
     

    def moyenne_glissante_tableau(self, X,ecart):
        """
        Méthode permettant de calculer la moyenne mobile d'une matrice
        
        Parametres
        ----------
        X: list
        fenetre: int (fenetrage de la moyenne glissante)
        
        Returns
        -------
        Moyenne_mobile: list
            La moyenne mobile d'une matrice
        """  
        
        Y = np.asarray(X.lignes)
        trans = np.transpose(Y)
        Z= trans.tolist()
        
        table_moyenne = []
        for x in Z:
            table_moyenne.append(self.moyenne_mobile(x,ecart))
        K = np.asarray(table_moyenne)
        trans_finale = np.transpose(K)
        P= trans_finale.tolist()
        return P

#from transformation_table import TransformationTable
#from table import Table
#class Normalisation (TransformationTable):
   # def __init__(self  , centre_gravite ):
       # self.centre_gravite=centre_gravite
        
    def normalisation (self, table,centre_gravite):
        L=[]
       
       
        for ligne in table.lignes:
            j=0
            m=[]
            for i in centre_gravite.lignes[0]:
                k= ligne[j]
                d=k-i
                j+=1
               
                
                m.append(d)
            L.append(m)
        return Table(centre_gravite.nom_colonnes, L) #print(m)