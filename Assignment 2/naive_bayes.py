#-------------------------------------------------------------------------
# AUTHOR: Melissa Ruiz
# FILENAME: naive_bayes.py
# SPECIFICATION: Outputs the classification of each test instance from the test set if the classification confidence is greater than or equal to 0.75
# FOR: CS 4200- Assignment #2
# TIME SPENT: 2 hr
#-----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data
# --> add your Python code here
class_num = 5
dbTraining = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTraining.append(row)

# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
X = []
for data in dbTraining:
    trainingFeats = []
    if data[1] == 'Sunny':
        trainingFeats.append(1)
    elif data[1] == 'Overcast':
        trainingFeats.append(2)
    elif data[1] == 'Rain':
        trainingFeats.append(3)

    if data[2] == 'Cool':
        trainingFeats.append(1)
    elif data[2] == 'Mild':
        trainingFeats.append(2)
    elif data[2] == 'Hot':
        trainingFeats.append(3)

    if data[3] == 'Normal':
        trainingFeats.append(1)
    elif data[3] == 'High':
        trainingFeats.append(2)

    if data[4] == 'Weak':
        trainingFeats.append(1)
    elif data[4] == 'Strong':
        trainingFeats.append(2)

    X.append(trainingFeats)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
Y = []
for data in dbTraining:
    if data[class_num] == 'Yes':
        Y.append(1)
    elif data[class_num] == 'No':
        Y.append(2)

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
dbTest = []
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
for data in dbTest:
    samples = []
    if data[1] == 'Sunny':
        samples.append(1)
    elif data[1] == 'Overcast':
        samples.append(2)
    elif data[1] == 'Rain':
        samples.append(3)

    if data[2] == 'Cool':
        samples.append(1)
    elif data[2] == 'Mild':
        samples.append(2)
    elif data[2] == 'Hot':
        samples.append(3)

    if data[3] == 'Normal':
        samples.append(1)
    elif data[3] == 'High':
        samples.append(2)

    if data[4] == 'Weak':
        samples.append(1)
    elif data[4] == 'Strong':
        samples.append(2)

    predicted = clf.predict_proba([samples])[0]

    if (predicted[0] > predicted[1]) and (predicted[0] >= 0.75):
        print(data[0].ljust(15), data[1].ljust(15), data[2].ljust(15), data[3].ljust(15), data[4].ljust(15), 'Yes'.ljust(15), "{:.2f}".format(predicted[0]))
    elif predicted[1] >= 0.75:
        print(data[0].ljust(15), data[1].ljust(15), data[2].ljust(15), data[3].ljust(15), data[4].ljust(15), 'No'.ljust(15), "{:.2f}".format(predicted[1]))