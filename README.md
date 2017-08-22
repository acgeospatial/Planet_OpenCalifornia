# Planet_OpenCalifornia
Series of Posts/Scripts on using data from Open California dataset by Planet


Gdal to sharpen
Raster files cover the SAME area!
blue_band_planet.tif = clipped blue band from Planet
sentinel2a.tif = Clipped RGB Sentinel2a data of any combination you like

gdal_pansharpen -w 0.52 -w 0.25 -w 0.23 -co PHOTOMETRIC=RGB blue_band_planet.tif sentinel2a.tif blue_sharpened.tif

repeat from Red and Green

Use outputs in 
