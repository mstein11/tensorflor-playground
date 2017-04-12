from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_fscore_support
class AlgoWrapper:

    def __init__(self,X, Y, classifier, numbers_to_run = 1, test_size=0.1):
        self.numbers_to_run = numbers_to_run
        self.test_size = test_size
        self.X = X
        self.Y = Y
        self.classifier = classifier

    def run(self):
        resultArr = []
        for n in range(0,self.numbers_to_run):
            lenth = len(self.X)
            delimiter = int(lenth * (1 -  self.test_size))
            positiveDelimiter = int(delimiter -1)
            negativeDelimiter = len(self.X) - delimiter

            X_train = self.X[0:positiveDelimiter]
            Y_train = self.Y[0:positiveDelimiter] 
            X_test = self.X[-negativeDelimiter:]
            Y_test = self.Y[-negativeDelimiter:] 

            #X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y,test_size=self.test_size)

            self.classifier.fit(X_train, Y_train)
            predictions = self.classifier.predict(X_test)

            test_results = precision_recall_fscore_support(Y_test,predictions,average='macro')
            test_results_with_sizes = test_results + (len(X_train), len(X_test))
            resultArr.append(test_results_with_sizes)
            
        return resultArr
    
