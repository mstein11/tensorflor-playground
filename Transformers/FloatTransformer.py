class FloatTransformer:
    def transform_data(self, dataArr, columnDef):
        columnRange = None
        if ":" in columnDef:
            columns = columnDef.split(":")
            start = int(columns[0])
            end = int(columns[1])
            columnRange = range(start, end + 1)#range does not add the last element so we have to increment
        else:
            columnRange = range(int(columnDef), int(columnDef) + 1)
        
        featureArr = []
        for dataVector in dataArr:
            tmp = []
            for columnId in columnRange:
                tmp.append(dataVector[columnId])
            featureArr.append(tmp)
        return featureArr, None
