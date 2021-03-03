#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: decision_tree.py
# SPECIFICATION: Trains on contact_lens_training_1.csv, contact_lens_training_2.csv, and contact_lens_training_3.csv to get lowest accuracy of the model during the 10 runs
# FOR: CS 4200- Assignment #2
# TIME SPENT: 2 hr
#-----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv','contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    class_num = 4
    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    for data in dbTraining:
        trainingFeats = []
        if data[0] == 'Young':
            trainingFeats.append(1)
        elif data[0] == 'Prepresbyopic':
            trainingFeats.append(2)
        elif data[0] == 'Presbyopic':
            trainingFeats.append(3)

        if data[1] == 'Myope':
            trainingFeats.append(1)
        elif data[1] == 'Hypermetrope':
            trainingFeats.append(2)

        if data[2] == 'No':
            trainingFeats.append(1)
        elif data[2] == 'Yes':
            trainingFeats.append(2)

        if data[3] == 'Normal':
            trainingFeats.append(1)
        elif data[3] == 'Reduced':
            trainingFeats.append(2)

        X.append(trainingFeats)

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    for data in dbTraining:
        if data[class_num] == 'Yes':
            Y.append(1)
        elif data[class_num] == 'No':
            Y.append(2)
    # loop your training and test tasks 10 times here
    for i in range(10):
        true = 0.0
        total = 0.0
        lowest_accuracy = 1.0

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        dbTest = []

        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)

        for data in dbTest:
            # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            # class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            # --> add your Python code here
            trainingFeats_test = []
            if data[0] == 'Young':
                trainingFeats_test.append(1)
            elif data[0] == 'Prepresbyopic':
                trainingFeats_test.append(2)
            elif data[0] == 'Presbyopic':
                trainingFeats_test.append(3)

            if data[1] == 'Myope':
                trainingFeats_test.append(1)
            elif data[1] == 'Hypermetrope':
                trainingFeats_test.append(2)

            if data[2] == 'No':
                trainingFeats_test.append(1)
            elif data[2] == 'Yes':
                trainingFeats_test.append(2)

            if data[3] == 'Normal':
                trainingFeats_test.append(1)
            elif data[3] == 'Reduced':
                trainingFeats_test.append(2)

            class_predicted = clf.predict([trainingFeats_test])[0]

            # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            # --> add your Python code here
            if data[class_num] == 'Yes':
                trueLabel = 1
                total += 1.0
            elif data[class_num] == 'No':
                trueLabel = 2
                total += 1.0

            if trueLabel == class_predicted:
                true += 1.0

        # find the lowest accuracy of this model during the 10 runs (training and test set)
        # --> add your Python code here
        ac = true / total
        if ac < lowest_accuracy:
            lowest_accuracy = ac

    # print the lowest accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that:
        # final accuracy when training on contact_lens_training_1.csv: 0.2
        # final accuracy when training on contact_lens_training_2.csv: 0.3
        # final accuracy when training on contact_lens_training_3.csv: 0.4
    # --> add your Python code here
    print('final accuracy when training on', ds, ': ', lowest_accuracy)