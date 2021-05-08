#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: clustering.py
# SPECIFICATION: Run k-means to check which k value maximizes the Silhouette coefficient
# FOR: CS 4200- Assignment #5
# TIME SPENT: 2 hrs
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn import metrics

max_k = 0
max_sil = 0
k_value = []
silhouette_scores = []

X_training = pd.read_csv('training_data.csv', sep=',', header=None) #reading the data by using Pandas library

#run kmeans testing different k values from 2 until 20 clusters
     #Use:  kmeans = KMeans(n_clusters=k, random_state=0)
     #      kmeans.fit(X_training)
     #--> add your Python code
for k in range(2, 21):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_training)
     #for each k, calculate the silhouette_coefficient by using: silhouette_score(X_training, kmeans.labels_)
     #find which k maximizes the silhouette_coefficient
     #--> add your Python code here
    k_value.append(k)
    silhouette_temp = silhouette_score(X_training, kmeans.labels_)
    silhouette_scores.append(silhouette_temp)
    if silhouette_temp > max_sil:
        max_sil = silhouette_temp
        max_k = k

#plot the value of the silhouette_coefficient for each k value of kmeans so that we can see the best k
#--> add your Python code here
plt.plot(k_value, silhouette_scores)
plt.xlabel('k')
plt.ylabel('Silhouette Coefficient')
plt.title('K vs Silhouette Coefficient')
plt.show()

#reading the validation data (clusters) by using Pandas library
#--> add your Python code here
testing = pd.read_csv('testing_data.csv', sep=',', header=None)

#assign your data labels to vector labels (you might need to reshape the row vector to a column vector)
# do this: np.array(df.values).reshape(1,<number of samples>)[0]
#--> add your Python code here
labels = np.array(testing.values).reshape(1, len(testing.values))[0]

#Calculate and print the Homogeneity of this kmeans clustering
print("K-Means Homogeneity Score = " + metrics.homogeneity_score(labels, kmeans.labels_).__str__())
#--> add your Python code here

#rung agglomerative clustering now by using the best value o k calculated before by kmeans
#Do it:
#agg = AgglomerativeClustering(n_clusters=<best k value>, linkage='ward')
#agg.fit(X_training)
agg = AgglomerativeClustering(n_clusters=max_k, linkage='ward')
agg.fit(X_training)

#Calculate and print the Homogeneity of this agglomerative clustering
print("Agglomerative Clustering Homogeneity Score = " + metrics.homogeneity_score(labels, agg.labels_).__str__())
