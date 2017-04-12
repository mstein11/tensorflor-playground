from Algos import Regression
from Transformers import GeoDataTransformer, FloatTransformer, ResultTransformer
from sklearn import svm
from sklearn import dummy
from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from enum import Enum

class ColumnDef:
    def __init__(self, columnIdentifier, transformationType):
        #e.g. "0" for the first column, or "0:1" for column 1 and 2
        self.columnIdentifier = columnIdentifier
        self.transformationType = transformationType


class TransformationTypes(Enum):
    NONE = 0
    GEO = 1
    REMOVE = 2
    RESULT = 3
    FLOAT = 4

    @staticmethod
    def get_transformation_by_type(type):
        if (type == TransformationTypes.GEO):
            return GeoDataTransformer.GeoDataTransformer()
        if (type == TransformationTypes.FLOAT):
            return FloatTransformer.FloatTransformer()
        if (type == TransformationTypes.RESULT):
            return ResultTransformer.ResultTransformer()

class Algorithms(Enum):
    SVM = 0
    RANDOM = 1
    TREE = 2
    SGD = 3 #Stochastic Gradient Descent
    ADABOOST = 4
    COINSMODEL = 5
    RANDOMFOREST = 6

    @staticmethod
    def get_algo_by_type(type):
        if (type == Algorithms.SVM):
            return svm.SVC()
        if (type == Algorithms.RANDOM):
            return dummy.DummyClassifier()
        if (type == Algorithms.TREE):
            return tree.DecisionTreeClassifier()
        if (type == Algorithms.SGD):
            return SGDClassifier(shuffle=True)
        if (type == Algorithms.ADABOOST):
            return AdaBoostClassifier()
        if (type == Algorithms.COINSMODEL):
            return Regression.CoinsRegressionClassifier()
        if (type == Algorithms.RANDOMFOREST):
            return RandomForestClassifier()

class Config:
    columnDefs = []
    algorithm = Algorithms.SVM

    def __init__(self, fileName, columnDefs,algorithm, testRuns = 1, testSize = 0.1, outputFilePrefix = ""):
        self.fileName = fileName
        self.columnDefs = columnDefs
        self.algorithm = algorithm
        self.testRuns = testRuns
        self.testSize = testSize
        if (outputFilePrefix == ""):
            self.outputFilePrefix = fileName
        else:
            self.outputFilePrefix = outputFilePrefix
        


def get_active_configs():
    columnDefinitions1 = []
    '''
    columnDefinitions1.append(ColumnDef("0",TransformationTypes.FLOAT))
    #columnDefinitions1.append(ColumnDef("1:2",TransformationTypes.GEO))
    columnDefinitions1.append(ColumnDef("3:6",TransformationTypes.FLOAT))
    columnDefinitions1.append(ColumnDef("7",TransformationTypes.RESULT))
    '''
    columnDefinitions1.append(ColumnDef("0:2",TransformationTypes.FLOAT))
    #columnDefinitions1.append(ColumnDef("3:4",TransformationTypes.GEO))
    columnDefinitions1.append(ColumnDef("6:13",TransformationTypes.FLOAT))
    columnDefinitions1.append(ColumnDef("14",TransformationTypes.RESULT))
    '''
    columnDefinitions2 = []
    columnDefinitions2.append(ColumnDef("0",TransformationTypes.FLOAT))
    columnDefinitions2.append(ColumnDef("1:2",TransformationTypes.GEO))
    columnDefinitions2.append(ColumnDef("5:12",TransformationTypes.FLOAT))
    columnDefinitions2.append(ColumnDef("14",TransformationTypes.RESULT))

    columnDefinitions3 = []
    columnDefinitions3.append(ColumnDef("0",TransformationTypes.FLOAT))
    columnDefinitions3.append(ColumnDef("1:2",TransformationTypes.GEO))
    columnDefinitions3.append(ColumnDef("5:12",TransformationTypes.FLOAT))
    columnDefinitions3.append(ColumnDef("13",TransformationTypes.RESULT))

    columnDefinitions4 = []
    columnDefinitions4.append(ColumnDef("0:39",TransformationTypes.FLOAT))
    columnDefinitions4.append(ColumnDef("42",TransformationTypes.RESULT))
    '''

    
    config2 = Config("Mappe1.csv", columnDefinitions1, Algorithms.RANDOM, testRuns = 5,testSize = 0.3, outputFilePrefix = "0-3random")
    config3 = Config("Mappe1.csv", columnDefinitions1, Algorithms.TREE, testRuns = 5,testSize = 0.3, outputFilePrefix = "0-3tree")
    config1 = Config("Mappe1.csv", columnDefinitions1, Algorithms.RANDOMFOREST, testRuns = 5,testSize = 0.3, outputFilePrefix = "0-3randomforrest")
    #config4 = Config("Mappe1.csv", columnDefinitions1, Algorithms.SGD, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1sgd")
    #config5 = Config("Mappe1.csv", columnDefinitions1, Algorithms.ADABOOST, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1ada")

    '''
    config1 = Config("herwix-model-coins.csv", columnDefinitions4, Algorithms.SVM, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1svm")
    config2 = Config("herwix-model-coins.csv", columnDefinitions4, Algorithms.RANDOM, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1random")
    config3 = Config("herwix-model-coins.csv", columnDefinitions4, Algorithms.TREE, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1tree")
    config4 = Config("herwix-model-coins.csv", columnDefinitions4, Algorithms.COINSMODEL, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1coins")
    config5 = Config("herwix-model-coins.csv", columnDefinitions4, Algorithms.ADABOOST, testRuns = 20,testSize = 0.1, outputFilePrefix = "0-1ada")


    config6 = Config("herwix-geodata-distinct-var.csv", columnDefinitions2, Algorithms.SVM, testRuns = 20,testSize = 0.1, outputFilePrefix = "nooo0-1avgsvm")
    config7 = Config("herwix-geodata-distinct-var.csv", columnDefinitions2, Algorithms.RANDOM, testRuns = 20,testSize = 0.1, outputFilePrefix = "nooo0-1avgrandom")
    config8 = Config("herwix-geodata-distinct-var.csv", columnDefinitions2, Algorithms.TREE, testRuns = 20,testSize = 0.1, outputFilePrefix = "nooo0-1avgtree")
    config9 = Config("herwix-geodata-distinct-var.csv", columnDefinitions2, Algorithms.SGD, testRuns = 20,testSize = 0.1, outputFilePrefix = "nooo0-1avgsgd")
    config10 = Config("herwix-geodata-distinct-var.csv", columnDefinitions2, Algorithms.ADABOOST, testRuns = 20,testSize = 0.1, outputFilePrefix = "nooo0-1avgada")
    config11 = Config("herwix-geodata-distinct-var2.csv", columnDefinitions3, Algorithms.SVM, testRuns = 20,testSize = 0.1, outputFilePrefix = "my-data-0-1cuedsvm")
    config12 = Config("herwix-geodata-distinct-var2.csv", columnDefinitions3, Algorithms.RANDOM, testRuns = 20,testSize = 0.1, outputFilePrefix = "my-data-0-1cuedrandom")
    config13 = Config("herwix-geodata-distinct-var2.csv", columnDefinitions3, Algorithms.TREE, testRuns = 20,testSize = 0.1, outputFilePrefix = "my-data0-1cuedtree")
    config14 = Config("herwix-geodata-distinct-var2.csv", columnDefinitions3, Algorithms.SGD, testRuns = 20,testSize = 0.1, outputFilePrefix = "my-data-0-1cuedsgd")
    config15 = Config("herwix-geodata-distinct-var2.csv", columnDefinitions3, Algorithms.ADABOOST, testRuns = 20,testSize = 0.1, outputFilePrefix = "my-data-0-1cuedada")
    '''
    configs = []
    configs.append(config1)
    configs.append(config2)
    configs.append(config3)
    #configs.append(config4)
    #configs.append(config5)
    '''
    configs.append(config6)
    configs.append(config7)
    configs.append(config8)
    configs.append(config9)
    configs.append(config10)
    configs.append(config11)
    configs.append(config12)
    configs.append(config13)
    configs.append(config14)
    configs.append(config15)
    '''
    return configs