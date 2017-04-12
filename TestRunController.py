from Configs.Config import TransformationTypes, Config, Algorithms, get_active_configs
from CsvImporter import Importer
from Algos.AlgoWrapper import AlgoWrapper
from FileWriter import FileWriter

importer = Importer()
configs = get_active_configs()

for config in configs:
    transformedFeatureArr = []
    transformedResultArr = []
    data = importer.get_data("Data/" + config.fileName)

    [transformedFeatureArr.append([]) for n in data]
    #[transformedResultArr.append([]) for n in data]

    for columnDef in config.columnDefs:
        transformation = TransformationTypes.get_transformation_by_type(columnDef.transformationType)
        featureArr, resultArr = transformation.transform_data(data, columnDef.columnIdentifier)
        if (featureArr is not None):
            for features, n in zip(featureArr, range(len(featureArr))):
                for feature in features:
                    transformedFeatureArr[n].append(feature)
            
            #transformedFeatureArr.append(featureArr)
        if (resultArr is not None):
            for result in resultArr:
                transformedResultArr.append(result)


        
    result = AlgoWrapper(transformedFeatureArr,transformedResultArr,Algorithms.get_algo_by_type(config.algorithm),config.testRuns,test_size = config.testSize).run()
    writer = FileWriter()
    writer.save_precision_recall_fscore(config.outputFilePrefix, result)