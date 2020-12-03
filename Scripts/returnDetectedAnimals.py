from qgis.PyQt.QtCore import QCoreApplication;

from qgis.core import (QgsCoordinateTransformContext,
QgsProcessing, 
QgsProcessingAlgorithm, 
QgsProcessingParameterFeatureSource, 
QgsProcessingParameterFolderDestination,
QgsVectorFileWriter);

from pathlib import Path;

class ReturnDetectedAnimalsAlgorithm(QgsProcessingAlgorithm):
    
    INPUT_CENTROIDS = 'INPUT_CENTROIDS';
    INPUT_CLASSIFICATION = 'INPUT_CLASSIFICATION';
    INPUT_CONFUSIONMATRIX = 'INPUT_CONFUSIONMATRIX';
    OUTPUT = 'OUTPUT';
    
    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT_CENTROIDS,
                self.tr('INPUT: Centroids Vector Layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        );
        
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUT,
                self.tr('Output Directory'),
            )
        );
        
    def processAlgorithm(self, parameters, context, feedback):
        centroids = self.parameterAsVectorLayer(parameters, self.INPUT_CENTROIDS, context);
        outputFolder = self.parameterAsFileOutput(parameters, self.OUTPUT, context);
        
        featureCount = centroids.featureCount();
        features = centroids.getFeatures();
        
        textfilePath = outputFolder+'/DetectionResults.txt';
        
        with open(textfilePath, 'w') as file:
            file.write("Es wurden insgesamt "+str(featureCount)+" Individuen detektiert.\n");
            file.write("Die detektierten Tiere befinden sich an folgenden Positionen:\n\n");
            x = 1;
            for feature in features:
                coordinates = "["+feature.geometry().asPoint().toString()+"]";
                file.write(str(x)+" "+coordinates+"\n");
                x += 1;
        
        return {self.OUTPUT: outputFolder}; 
    
    def tr(self, string):
        return QCoreApplication.translate('Processing', string);
    
    def createInstance(self):
        return ReturnDetectedAnimalsAlgorithm();
    
    def name(self):
        return 'returndetectedanimals';
        
    def displayName(self):
        return self.tr('Return Detected Animals');
    