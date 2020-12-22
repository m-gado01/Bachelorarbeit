from qgis.PyQt.QtCore import QCoreApplication;

from qgis.core import (QgsProcessing, 
QgsProcessingAlgorithm,
QgsProcessingParameterFolderDestination,
QgsProcessingParameterRasterLayer);

from osgeo import gdal;

class ExtractRasterBandsFromLayer(QgsProcessingAlgorithm):
    
    INPUT = 'INPUT';
    OUTPUT = 'OUTPUT';
    
    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT,
                self.tr('INPUT: Raster Layer'),
            )
        );
        
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUT,
                self.tr('OUTPUT: Directory'),
            )
        );
        
    def processAlgorithm(self, parameters, context, feedback):
        rasterLayer = self.parameterAsRasterLayer(parameters, self.INPUT, context);
        outputFolder = self.parameterAsFileOutput(parameters, self.OUTPUT, context);
        
        filePath = rasterLayer.dataProvider().dataSourceUri();
        dataSource = gdal.Open(filePath, gdal.GA_ReadOnly);
        numberOfBands = dataSource.RasterCount;
        
        print(numberOfBands);
        
        return {self.OUTPUT: outputFolder}; 
    
    def tr(self, string):
        return QCoreApplication.translate('Processing', string);
    
    def createInstance(self):
        return ExtractRasterBandsFromLayer();
    
    def name(self):
        return 'extractRasterBandsFromLayer';
        
    def displayName(self):
        return self.tr('Extract Raster Bands From Layer');
    