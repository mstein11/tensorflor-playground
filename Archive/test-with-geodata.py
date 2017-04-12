import csv
from decimal import Decimal
from CsvImporter import Importer
from Svm import Svm
from DbScan import DbScan
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_digits
from sklearn import svm

arr = []
cellCounter = 0
rowCounter = 0

_pleasantArr = []
_activationArr = []
_geoIndexArr = []
_geoArrNoNulls = []
_longitudeArr = []
_latitudeArr = []
_geoArrWithNull = []
importer = Importer()
arr = importer.get_data("data/peters-data-geo.csv")
#herwix-data-geo.csv
#we remove the Features needing preprocessing and the classification columns from arr
for row, n in zip(arr, range(len(arr))):
    #remove classifications
    _pleasantArr.append(row.pop())
    _activationArr.append(row.pop())
    #remove unprocessed geodata and save them for processing
    lat = row.pop(1)
    lng = row.pop(1)
    tmp = []
    tmp.append(lat)##lat
    tmp.append(lng)##long
    _geoArrWithNull.append(tmp)
    
    #if lat und longitude is set, process them later
    if (lat is not None):
        #the index of the feature vector in the dataset (arr)
        _geoIndexArr.append(n)
        _geoArrNoNulls.append(tmp)


#find places your are around a lot (an area where at least 10% of your gps coords stem from)
dbScanAlgo = DbScan()
algoResult = dbScanAlgo.run(_geoArrNoNulls)
geoPointsFeatures = set(algoResult)   

dbScanAlgo.run_and_prepare_data(_geoArrWithNull)

#add one new feature to each feature vector for each common location
for row, n in zip(arr, range(len(arr))):
    if (n in _geoIndexArr and algoResult[_geoIndexArr.index(n)] == -1 or n not in _geoIndexArr):
        row.append(1)
    else:
        row.append(0)
    
    for feature in geoPointsFeatures:
        if (feature == -1):
            continue
        if (n in _geoIndexArr and feature == algoResult[_geoIndexArr.index(n)]):
            row.append(1)
        else:
            row.append(0)
        



print("number of features in array:" + str(len(arr[0])))


def train_and_test(data, samples, test_size):
    X_train, X_test, y_train, y_test = train_test_split(data, samples,test_size=test_size)

    algo2 = Svm()
    algo2.train(X_train, y_train)
    predictions_activation = algo2.predict(X_test)

    from sklearn.metrics import confusion_matrix, classification_report
    print(classification_report(y_test, predictions_activation))
    trueIfPredicted = [pred==actual for pred, actual in zip(y_test, predictions_activation)]
    accuracy = float(len(list(filter(lambda x: x, trueIfPredicted)))) / float(len(y_test))
    print("accuracy: " + str(accuracy))
    return accuracy

activation_accuracy = train_and_test(arr,_activationArr, 0.1)
pleasant_accuracy = train_and_test(arr,_pleasantArr, 0.1)

combined = [str(int(x)) + str(int(y)) for x, y in zip(_activationArr, _pleasantArr)]
combined_accuracy = train_and_test(arr,combined, 0.1)

print("When using one svm classifier to classify in both dimensions. accuracy: "+ str(combined_accuracy))
print("When classifying each dimension seperately. accuracy: "+ str(activation_accuracy * pleasant_accuracy))

def run_model(dataArr, locationArr, activationArr, pleasantArr):
    return ""
