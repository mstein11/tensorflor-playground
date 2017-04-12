class CoinsRegressionClassifier:
    def fit(self, X_train, Y_train):
        return

    def predict(self, X_test):
        resultArr = []
        for row in X_test:
            predictedPleasant = (2.4702 + 
                0.2778 * row[4] + #lightlevel min
                -0.2374 * row[6] +
                0.208 * row[9] + 
                -0.1715 * row[10] +
                -0.1123 * row[11] +
                0.0002 * row[16] +
                -0.0003 * row[21] +
                0.0004 * row[22]) 
            
            if (predictedPleasant < 0.75):
                predictedPleasant = 0
            elif (predictedPleasant < 1.5):
                predictedPleasant = 1
            elif (predictedPleasant < 2.25):
                predictedPleasant = 2
            else:
                predictedPleasant = 3

            predictedActivation = (1.8725 + 
                0.0286 * row[0] +
                0.0074 * row[1] + 
                -0.0367 * row[2] + 
                -0.0823 * row[5] +
                -0.1241 * row[7] +
                0.2367 * row[8] + 
                -0.146 * row[9] + 
                -0.3783 * row[10] + 
                0.0003 * row[13] + 
                0.0004 * row[16] +
                0.0006 * row[17] + 
                -0.0007 * row[20] +
                0.0009 *  row[21]) 
            
            if (predictedActivation < 0.75):
                predictedActivation = 0
            elif (predictedActivation < 1.5):
                predictedActivation = 1
            elif (predictedActivation < 2.25):
                predictedActivation = 2
            else:
                predictedActivation = 3

            resultArr.append(str(predictedPleasant) + str(predictedActivation))
        print(resultArr)
        return resultArr
