# -*- coding: utf-8 -*-
"""K-means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mbixNWWgEG723VRM4YGAoj08JAUbsewl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data
df= pd.read_csv("ClusteringData.txt" , header=None)

def calculateEuclideanDistance(point1,point2):
  #x and y are np 
  squared_distance = ((point1-point2)**2).sum()
  distance = squared_distance ** 0.5
  return distance

df.head(2)

from numpy.random.mtrand import random_sample
class KMeans:

  def __init__(self , K=2 , max_iters=100 ):
    self.K=K
    self.max_iters=max_iters
    

    self.clusters=[[] for _ in range(self.K)]

    self.centroids=[BrokenPipeError]

    
   

    #Optimization;


  def predict(self , X):
    self.X=X.values
    self.n_samples , self.n_features = X.shape

    
      #List of sample indices for eachc cluster
    # so [1,45,6] for cluster 1 , [2,4,5] for cluster 2

    #Store centroids
    random_sample_idxs= np.random.choice(self.n_samples , self.K , replace=False)

    #Pick the k values in random sample
    self.centroids = [self.X[idx] for idx in random_sample_idxs]

    #Optimization
    #Run for max iteration

    for i in range(self.max_iters):
      
      #Create cluster
      self.clusters = self.create_clusters(self.centroids)

      if i ==0:
        self.plot(i)

      if i == 4:
        self.plot(i)

      #Update centroids
      centroids_old = self.centroids
      self.centroids = self.get_centroids(self.clusters)

      #Check if converged
      if self.converged(centroids_old , self.centroids):
        #Plot before exiting
        self.plot(i)
        break

      #Return cluster labels
    return self.get_cluster_labels(self.clusters)

    
  def get_cluster_labels(self , clusters):
    labels = np.empty(self.n_samples)
    for cluster_idx , cluster in enumerate(clusters):
      for inidivdual_idx in cluster:
        labels[inidivdual_idx]= cluster_idx

  def create_clusters(self , centroids):

    #Create a simple list to store the index of each df 
    # [1,2,3] belong to cluster 0 , [4,6] belong to cluster 1 , [5 , 7 , 8] belong to cluster 3
    clusters=[[] for _ in range(self.K)]

    for idx , sample in enumerate(self.X):

      #Get the index of where the sample centroid is
      centroid_idx = self.closest_centroid(sample , centroids)

      #For that cluster , append idc.
      clusters[centroid_idx].append(idx)
    return clusters

  def closest_centroid(self , sample , centroids):
    #Gets closest_centorid for a given point and the centroid
    #Instead of doing 
    #distances 
    #for point in centorids: distance.append(sample , point)
    #return min(distance)
    distances=[calculateEuclideanDistance(sample , point) for point in centroids]
    closeset_idx=np.argmin(distances)
    return closeset_idx

  def get_centroids(self , clusters):
    #Initialize centroids with zeores.
    centroids = np.zeros((self.K , self.n_features))
    # centroids[0]=20 , cenrroids[1] = 30
    #Get mean of each cluster
    #Get mean of each cluster
    for cluster_idx , cluster in enumerate(clusters):
      cluster_mean = np.mean(self.X[cluster] , axis=0)
      centroids[cluster_idx] = cluster_mean
    
    return centroids
    
  def converged(self , centroids_old , centroids):

    distances = [calculateEuclideanDistance(centroids_old[i] , centroids[i])  for i in range(self.K)]
    #Return the sum of distance. 

    if sum(distances) < 0.001 :
      return True
    return False
    

  def plot(self , iteration ):
    print("i am here")
    fig , ax = plt.subplots(figsize = (12,8))
    
    #title matplotlib
    
    for i , index in enumerate(self.clusters):
      point = self.X[index].T
      ax.scatter(*point)
    for point in self.centroids:
      ax.scatter(*point , marker = "x" , color="black" , linewidth = 2)
    plt.title("Iteration: " + str(iteration) + " Number of clusters : " + str(self.K))
    plt.show()

k = KMeans(K=2 , max_iters=150 )

y_pred = k.predict(df)




# def calcMeans(cluster):
#   #They contain all datapoints that belong to a cluster
#   center = cluster.mean(axis=0)
#   return center

# def getCentroidPoints(dataframe):
#   #From the dataframe get the cluster of each point

# #Functionality for number of cluster. Use sys arg. 
# #For now use k =2 
# k=2

# #Cluster data based on centroid

# #Centroid at the beginning are random points . 

# #After first iteration , you find the centroid of the point and use that in consecutive iterations.


# while True:
#   #iteration tracker 
#   i=0
#   #How to represent
#   new_df = df.assign(cluster=None)
   
#   centroids = []
#   #Pick k random points
#   if (i==0):
#     #pick 3 random points fom the df
#     #centroids = pick_random(df)
#     pass
#   else:
#     #Get centroids 
#     #centroids = getCentroidPoints(df)
#     pass
  
  
#    #for each point in the datafrmae. 
#    #Calculate euclidens distance with each value in centorids
#    #Pick max , set position of centorid as cluster so cluster 0 , 1 , 2 , ...
   
#   for index , row in new_df.iterrows():
    
#     total_distance = []
#     for value in centroids:
#       total_distance.append(calculateEuclideanDistance(new_df[index] , value ))
    
#     new_df[i]['cluster'] = min(total_distance)
   
#    #once the cluster is done .
#    #Find the cluster for each iteration

   
   




  
#   #Have a stopping condition for breaking.
#   #Return the df. 
#   break