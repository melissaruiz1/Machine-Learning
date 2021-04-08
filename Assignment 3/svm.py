#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: svm.py
# SPECIFICATION: Reads optdigits.tra to build SVM classifiers and find the best prediction performance.
# FOR: CS 4200- Assignment #3
# TIME SPENT: 2 hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import svm
import csv

dbTraining = []
dbTest = []
X_training = []
Y_training = []
c = [1, 5, 10, 100]
degree = [1, 2, 3]
kernel = ["linear", "poly", "rbf"]
decision_function_shape = ["ovo", "ovr"]
highestAccuracy = 0

#reading the data in a csv file
with open('optdigits.tra', 'r') as trainingFile:
  reader = csv.reader(trainingFile)
  for i, row in enumerate(reader):
      X_training.append(row[:-1])
      Y_training.append(row[-1:])

#reading the data in a csv file
with open('optdigits.tes', 'r') as testingFile:
  reader = csv.reader(testingFile)
  for i, row in enumerate(reader):
      dbTest.append(row)

#created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
#--> add your Python code here

for c_items in c: #iterates over c
    for degree_items in degree: #iterates over degree
        for kernel_items in kernel: #iterates kernel
           for decision_function_shape_items in decision_function_shape: #iterates over decision_function_shape
                true = 0
                total = 0

                #Create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape as hyperparameters. For instance svm.SVC(c=1)
                clf = svm.SVC(C=c_items, degree=degree_items, kernel=kernel_items, decision_function_shape=decision_function_shape_items)

                #Fit Random Forest to the training data
                clf.fit(X_training, Y_training)

                #make the classifier prediction for each test sample and start computing its accuracy
                #--> add your Python code here

                for instance in dbTest:
                    class_predicted = clf.predict([instance[:-1]])[0]

                    if int(class_predicted) == int(instance[-1]):
                        true = true + 1

                    total = total + 1

                accuracy = true / total
                #check if the calculated accuracy is higher than the previously one calculated. If so, update update the highest accuracy and print it together with the SVM hyperparameters
                #Example: "Highest SVM accuracy so far: 0.92, Parameters: a=1, degree=2, kernel= poly, decision_function_shape = 'ovo'"
                #--> add your Python code here

                if accuracy > highestAccuracy:
                    highestAccuracy = accuracy

                    results = ""

                    results = str(highestAccuracy) + \
                              ", Parameters: a = " + str(c_items) + \
                              ", degree = " + str(degree_items) + \
                              ", kernel = " + str(kernel_items) + \
                              ", decision_function_shape = " + str(decision_function_shape_items)

                    print("Highest SVM accuracy so far: ", results)

#print the final, highest accuracy found together with the SVM hyperparameters
#Example: "Highest SVM accuracy: 0.95, Parameters: a=10, degree=3, kernel= poly, decision_function_shape = 'ovr'"
#--> add your Python code here
print("Highest SVM accuracy: ", results)











