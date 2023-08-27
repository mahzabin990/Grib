# Code to convert grib to tiff


from osgeo import gdal

src_filename = "download.grib" 
dst_filename = "download.tiff"

#Open existing dataset
src_ds = gdal.Open(src_filename)

#Open output format driver, see gdal_translate --formats for list
format = "GTiff"
driver = gdal.GetDriverByName( format )

#Output to new format
dst_file = driver.CreateCopy( dst_filename, src_ds, 0 )

#Properly close the datasets to flush to disk
dst_ds = None
src_ds = None
