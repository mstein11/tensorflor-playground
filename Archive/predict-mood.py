import csv
from decimal import Decimal
from CsvImporter import Importer
arr = []
cellCounter = 0
rowCounter = 0
salaryArr = []


importer = Importer()
arr = importer.get_data("XXX")

for row in arr:
    row.pop(-2)
    print (str(row))
    salaryArr.append(row.pop())

for row in salaryArr:
    print (str(row))

from sklearn.datasets import load_digits
from matplotlib import pyplot as plt

from sklearn import svm
classifier = svm.SVC(probability=True)
classifier.fit(arr, salaryArr)
predicted = classifier.predict(arr)

import numpy as np


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(arr, salaryArr,test_size=0.2)

classifier.fit(X_train, y_train)
predicted2 = classifier.predict(X_test)
print("model " + str(np.mean(y_test == predicted2)))
from sklearn.metrics import confusion_matrix, classification_report
print(classification_report(y_test, predicted2))
