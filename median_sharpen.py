##averaging the inputs sharpened sentinel 2 data

from osgeo import gdal
import numpy
### open the raster
gdalData1 = gdal.Open("...red.tif")
gdalData2 = gdal.Open("...green.tif")
gdalData3 = gdal.Open("...blue")
### read into array
raster1 = gdalData1.ReadAsArray()
raster2 = gdalData2.ReadAsArray()
raster3 = gdalData3.ReadAsArray()

#reclassify raster values using Numpy! in this case less and greater functions


d = numpy.array([raster1,raster2,raster3])

raster = numpy.median(d, axis=0)

# write results to file (lets set it to tif)
format = "GTiff"
driver = gdal.GetDriverByName(format)

# CreateCopy() to save outraster
outDataRaster = driver.CreateCopy("...outMedian_sharpened", gdalData1, 0)
outDataRaster.GetRasterBand(0).WriteArray(raster)
