#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: naive_bayes.py
# SPECIFICATION: Outputs the classification of each test instance from the test set if the classification confidence is greater than or equal to 0.75
# FOR: CS 4200- Assignment #2
# TIME SPENT: --
#-----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

dbTraining = []
dbTest = []
# reading the training data
# --> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTraining.append(row)

# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
X = []
for instance in dbTraining:
    trainingFeats = []

    if instance[1] == 'Overcast':
        trainingFeats.append(1)
    elif instance[1] == 'Rain':
        trainingFeats.append(2)
    elif instance[1] == 'Sunny':
        trainingFeats.append(3)

    if instance[2] == 'Cool':
        trainingFeats.append(1)
    elif instance[2] == 'Hot':
        trainingFeats.append(2)
    elif instance[2] == 'Mild':
        trainingFeats.append(3)

    if instance[3] == 'High':
        trainingFeats.append(1)
    elif instance[3] == 'Normal':
        trainingFeats.append(2)

    if instance[4] == 'Strong':
        trainingFeats.append(1)
    elif instance[4] == 'Weak':
        trainingFeats.append(2)

    X.append(trainingFeats)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
Y = []
for instance in dbTraining:
    if instance[5] == 'Yes':
        Y.append(1)
    elif instance[5] == 'No':
        Y.append(2)

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) +
      "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions.
# --> add your Python code here
# -->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for instance in dbTest:
    samples = []

    if instance[1] == 'Overcast':
        samples.append(1)
    elif instance[1] == 'Rain':
        samples.append(2)
    elif instance[1] == 'Sunny':
        samples.append(3)

    if instance[2] == 'Cool':
        samples.append(1)
    elif instance[2] == 'Hot':
        samples.append(2)
    elif instance[2] == 'Mild':
        samples.append(3)

    if instance[3] == 'High':
        samples.append(1)
    elif instance[3] == 'Normal':
        samples.append(2)

    if instance[4] == 'Strong':
        samples.append(1)
    elif instance[4] == 'Weak':
        samples.append(2)

    predicted = clf.predict_proba([samples])[0]
