#-------------------------------------------------------------------------
# AUTHOR: Melissa RUiz
# FILENAME: decision_tree.py
# SPECIFICATION: Generates a decision tree based on contact_lens.csv
# FOR: CS 4200- Assignment #1
# TIME SPENT: 20 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays
#importing some Python libraries

from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transfor the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# Young = 1, Presbyotic = 2, Prepresbyotic = 3
# Myope = 1, Hypermetrope = 2
# No = 1, Yes = 2
# Reduced = 1, Normal = 2
X = [[1,1,1,1], [2,1,1,2], [3,1,1,1], [3,1,1,2], [2,1,2,2], [1,1,2,2], [1,2,1,1], [3,1,2,1], [2,2,1,1], [1,1,2,1]]

#transfor the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
Y = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1]

#fiiting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


