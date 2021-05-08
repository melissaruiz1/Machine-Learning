#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: collaborative_filtering.py
# SPECIFICATION: Makes a galleries and restaurants user-based recommendation for user 100
# FOR: CS 4200- Assignment #5
# TIME SPENT: 1 hr
#-----------------------------------------------------------*/

#importing some Python libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

sim = []
galleries = []
restaurants = []
similarities = 0
active_user_rating = 0

df = pd.read_csv('trip_advisor_data.csv', sep=',', header=0)  # reading the data by using the Pandas library ()

# iterate over the other 99 users to calculate their similarity with the active user (user 100) according to their category ratings (user-item approach)
# do this to calculate the similarity:
   #vec1 = np.array([[1,1,0,1,1]])
   #vec2 = np.array([[0,1,0,1,1]])
   #cosine_similarity(vec1, vec2)
   #do not forget to discard the first column (User ID) when calculating the similarities
   #--> add your Python code here
lastRow = df.iloc[[-1]]
for i, row in df.iterrows():
    if i == len(df) - 1:
        break
    vec1 = np.array([[row['dance clubs'], row['juice bars'], row['museums'], row['resorts'], row['parks/picnic spots'],
                      row['beaches'], row['theaters'], row['religious institutions']]])
    vec2 = np.array([lastRow['dance clubs'], lastRow['juice bars'], lastRow['museums'], lastRow['resorts'],
                     lastRow['parks/picnic spots'], lastRow['beaches'], lastRow['theaters'],
                     lastRow['religious institutions']]).reshape(1, 8)

    if i == 0:
        active_user_rating = sum(vec2[0]) / len(vec2[0])
    sim.append((i, cosine_similarity(vec1, vec2)[0][0]))

# find the top 10 similar users to the active user according to the similarity calculated before
top_neighbors = sorted(sim, reverse=True)[:10]
for x in top_neighbors:
    print("User ID: " + str(x[0]) + ", Similarity: " + str(x[1]))

# Compute a prediction from a weighted combination of selected neighbors’ for both categories evaluated (galleries and restaurants)
for x in top_neighbors:
    gal = float(df.at[x[0], 'galleries']) * x[1]
    rest = float(df.at[x[0], 'restaurants']) * x[1]

    similarities += x[1]
    galleries.append(gal)
    restaurants.append(rest)

    gallery = sum(galleries) / similarities
    restaurant = sum(restaurants) / similarities

print("Galleries prediction: ", str((gallery + active_user_rating)))
print("Restaurants prediction: ", str((restaurant + active_user_rating)))



