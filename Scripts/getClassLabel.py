from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingOutputString)

class GetClassLabelAlgorithm(QgsProcessingAlgorithm):
    
    INPUT='INPUT'
    OUTPUT='OUTPUT'
    
    def tr(self, string):
        return QCoreApplication.translate('Processing', string);
    
    def createInstance(self):
        return GetClassLabelAlgorithm();
    
    def name(self):
        return 'getclasslabel';
        
    def displayName(self):
        return self.tr('Get Class Label From Vector Layer');
    
    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input vector layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        );
        
        self.addOutput(
            QgsProcessingOutputString(
                self.OUTPUT,
                self.tr('Output Class Label')
            )
        );
        
    def processAlgorithm(self, parameters, context, feedback):
        vectorLayer = self.parameterAsVectorLayer(parameters, 'INPUT', context);
        classLabel = vectorLayer.attributeDisplayName(vectorLayer.attributeList()[-1]);
        
        print(type(classLabel));
        
        return {self.OUTPUT: classLabel}; 
    