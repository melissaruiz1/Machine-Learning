#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: knn.py
# SPECIFICATION: Reads binary_points.csv and outputs LOO-CV error rate for 1NN
# FOR: CS 4200- Assignment #2
# TIME SPENT: 1 hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

wrong_pred = 0.0
total_pred = 0.0
db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    #--> add your Python code here
    X = []
    for data, instance in enumerate(db):
        trainingFeats = []
        if i != data:
            trainingFeats.append(instance[0])
            trainingFeats.append(instance[1])

            X.append(trainingFeats)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
    #--> add your Python code here
    Y = []
    for data, instance in enumerate(db):
        if i != data:
            if instance[2] == '+':
                Y.append(1)
            elif instance[2] == '-':
                Y.append(2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = []
    for data, instance in enumerate(db):
            if i == data:
                testSample.append(instance[0])
                testSample.append(instance[1])

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    for data, instance in enumerate(db):
            if i == data:
                if instance[2] == '+':
                    true_label = 1
                    total_pred += 1
                elif instance[2] == '-':
                    true_label = 2
                    total_pred += 1

    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

    if class_predicted != true_label:
        wrong_pred += 1

#print the error rate
#--> add your Python code here
error_rate = (wrong_pred / total_pred)
print('\nError Rate: ', error_rate)