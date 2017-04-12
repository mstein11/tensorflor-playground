class ResultTransformer:
    def transform_data(self, dataArr, columnDef):        
        tmp = [str(int(row[int(columnDef)] / 2))  for row in dataArr]
        return None, tmp
