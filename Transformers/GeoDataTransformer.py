from DbScan import DbScan
import numpy as np

class GeoDataTransformer:
    def transform_data(self, dataArr, columnDef):
        columns = columnDef.split(":")

        npMatrix = np.matrix(dataArr)
        latAndLngArr = npMatrix[:, [int(columns[0]),int(columns[1])]].tolist()
        #latAndLngArr = [list(zip(row[int(columns[0])], row[int(columns[1])])) for row in dataArr]
        algo = DbScan()
        featureArr = algo.run_and_prepare_data(latAndLngArr)

        return featureArr, None