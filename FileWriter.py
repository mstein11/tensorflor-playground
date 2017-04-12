import datetime
class FileWriter:
    FOLDER_TO_SAVE_TO = "reports"

    def save_to_file(self, filename, data):
        with open(self.FOLDER_TO_SAVE_TO + "/" + filename, 'a') as file:
            for row in data:
                for cell in row:
                    file.write(str(cell) + ",")
                file.write('\n')

    '''
    Expects a 2 Dimensional Arr. The inner Dimension should have 3 entries (precision, recall, f1-score)
    '''
    def save_precision_recall_fscore(self, filename, data):
        formatedArr = []
        headerArr = []
        headerArr.append("precision")
        headerArr.append("recall")
        headerArr.append("f1-score")
        headerArr.append("support")
        formatedArr.append(headerArr)
        [formatedArr.append(n) for n in data]
        self.save_to_file(filename + str(datetime.datetime.utcnow()), formatedArr)


#fileWriter = FileWriter()
#fileWriter.save_to_file('test' + str(datetime.datetime.utcnow()), [])