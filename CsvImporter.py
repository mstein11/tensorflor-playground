import csv

class Importer:
    def get_data(self, filename):
        arr = []
        rowCounter = 0
        with open(filename, 'rU') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if (rowCounter == 0):
                    rowCounter += 1
                    continue
                arr.append([])
                for cell in row:
                    if (cell != "NULL"):
                        arr[rowCounter - 1].append(float(cell.strip('$').replace(',','.')))
                    else:
                        arr[rowCounter - 1].append(None)
                rowCounter += 1
            
        return arr
                
