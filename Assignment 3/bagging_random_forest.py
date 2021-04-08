#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: bagging_random_forest.py
# SPECIFICATION: Reads optdigits.tra and optdigits.names data to build a base classifier by using a decision tree, ensemble classifier
# and Random Forest. Also uses optdigits.tes to test accuracy of the models.
# FOR: CS 4200- Assignment #3
# TIME SPENT: 3 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
import csv

dbTraining = []
dbTest = []
X_training = []
Y_training = []
classVotes = [] #this array will be used to count the votes of each classifier

#reading the training data in a csv file
with open('optdigits.tra', 'r') as trainingFile:
  reader = csv.reader(trainingFile)
  for i, row in enumerate(reader):
      dbTraining.append(row)

#reading the test data in a csv file
with open('optdigits.tes', 'r') as testingFile:
  reader = csv.reader(testingFile)
  for i, row in enumerate(reader):
      dbTest.append (row)
      classVotes.append([0,0,0,0,0,0,0,0,0,0]) #inititalizing the class votes for each test sample

  print("Started my base and ensemble classifier ...")

  baseClassifierTrue = 0
  baseClassifierTotal = 0
  for k in range(20): #we will create 20 bootstrap samples here (k = 20). One classifier will be created for each bootstrap sample

      bootstrapSample = resample(dbTraining, n_samples=len(dbTraining), replace=True)

      #populate the values of X_training and Y_training by using the bootstrapSample
      #--> add your Python code here

      for instance in bootstrapSample:
          X_training.append(instance[:-1])
          Y_training.append(instance[-1])

      #fitting the decision tree to the data
      clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=None) #we will use a single decision tree without pruning it
      clf = clf.fit(X_training, Y_training)

      for i, testSample in enumerate(dbTest):

          #make the classifier prediction for each test sample and update the corresponding index value in classVotes. For instance,
          # if your first base classifier predicted 2 for the first test sample, then classVotes[0,0,0,0,0,0,0,0,0,0] will change to classVotes[0,0,1,0,0,0,0,0,0,0].
          # Later, if your second base classifier predicted 3 for the first test sample, then classVotes[0,0,1,0,0,0,0,0,0,0] will change to classVotes[0,0,1,1,0,0,0,0,0,0]
          # Later, if your third base classifier predicted 3 for the first test sample, then classVotes[0,0,1,1,0,0,0,0,0,0] will change to classVotes[0,0,1,2,0,0,0,0,0,0]
          # this arrays will consolidate the votes of all classifier for all test samples
          #--> add your Python code here

          classifier_prediction = clf.predict([testSample[:-1]])[0]
          classVotes[i][int(classifier_prediction)] += 1

          if k == 0: #for only the first base classifier, compare the prediction with the true label of the test sample here to start calculating its accuracy
             #--> add your Python code here

             if int(classifier_prediction) == int(testSample[-1]):
                 baseClassifierTrue = baseClassifierTrue + 1

             baseClassifierTotal = baseClassifierTotal + 1

      if k == 0: #for only the first base classifier, print its accuracy here
         #--> add your Python code here
         baseClassifierAccuracy = baseClassifierTrue / baseClassifierTotal

         print("Finished my base classifier (fast but relatively low accuracy) ...")
         print("My base classifier accuracy: " + str(baseClassifierAccuracy))
         print("")

  #now, compare the final ensemble prediction (majority vote in classVotes) for each test sample with the ground truth label to calculate the accuracy of the ensemble classifier (all base classifiers together)
  #--> add your Python code here
  ensembleClassifierTrue = 0
  ensembleClassifierTotal = 0

  for i, testSample in enumerate(dbTest):
      finalEnsemblePred = classVotes[i].index(max(classVotes[i]))
      truthLabel = testSample[-1]

      if int(truthLabel) == int(finalEnsemblePred):
          ensembleClassifierTrue = ensembleClassifierTrue + 1

      ensembleClassifierTotal = ensembleClassifierTotal + 1

  ensembleClassifierAccuracy = ensembleClassifierTrue / ensembleClassifierTotal

  #printing the ensemble accuracy here
  print("Finished my ensemble classifier (slow but higher accuracy) ...")
  print("My ensemble accuracy: " + str(ensembleClassifierAccuracy))
  print("")

  print("Started Random Forest algorithm ...")

  #Create a Random Forest Classifier
  clf=RandomForestClassifier(n_estimators=20) #this is the number of decision trees that will be generated by Random Forest. The sample of the ensemble method used before

  #Fit Random Forest to the training data
  clf.fit(X_training,Y_training)

  #make the Random Forest prediction for each test sample. Example: class_predicted_rf = clf.predict([[3, 1, 2, 1, ...]]
  #--> add your Python code here
  randomForestTotal = 0
  randomForestTrue= 0

  for i, testSample in enumerate(dbTest):
      class_predicted_rf = clf.predict([testSample[:-1]])[0]

      if int(class_predicted_rf) == int(testSample[-1]):
          randomForestTrue = randomForestTrue + 1

      randomForestTotal = randomForestTotal + 1

  #compare the Random Forest prediction for each test sample with the ground truth label to calculate its accuracy
  #--> add your Python code here

  randomForestAccuracy = randomForestTrue / randomForestTotal

  #printing Random Forest accuracy here
  print("Random Forest accuracy: " + str(randomForestAccuracy))

  print("Finished Random Forest algorithm (much faster and higher accuracy!) ...")




