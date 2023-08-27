from osgeo import gdal

# Open the GRIB file
filename = 'download.grib'
dataset = gdal.Open(filename)

if dataset is None:
    print("Failed to open the file.")
    exit(1)

# Get the number of raster bands (messages in the GRIB file)
num_bands = dataset.RasterCount

# Create a set to store the unique variables and their metadata
unique_variables = set()
variable_metadata = {}

# Loop through the messages and extract the variable names and metadata
for band_index in range(1, num_bands + 1):
    band = dataset.GetRasterBand(band_index)
    metadata = band.GetMetadata()

    # Extract the variable name from the metadata
    variable = metadata.get('GRIB_ELEMENT', 'Unknown')

    # If the variable is not in the set, add it to the set and store its metadata
    if variable not in unique_variables:
        units = metadata.get('GRIB_UNIT', 'Unknown')
        description = metadata.get('GRIB_COMMENT', 'Unknown')
        long_name = metadata.get('GRIB_LONG_NAME', 'Unknown')

        unique_variables.add(variable)
        variable_metadata[variable] = {
            'long_name': long_name,
            'units': units,
            'description': description
        }

# Close the file
dataset = None

# Print the questions about distinct variables and their metadata
num_distinct_variables = len(unique_variables)
distinct_variable_names = ', '.join(unique_variables)

print(f"Q: How many distinct variables are there in the GRIB file?")
print(f"A: There are {num_distinct_variables} distinct variables.")
print(f"Q: What are the names of the distinct variables?")
print(f"A: The names of the distinct variables are: {distinct_variable_names}\n")

# Print metadata for each distinct variable
for variable, metadata in variable_metadata.items():
    long_name = metadata['long_name']
    units = metadata['units']
    description = metadata['description']
    print(f"Q: What is the unit, and description of the variable '{variable}'?")
    print(f" A:  The units of the variable '{variable}' are '{units}'.")
    print(f"   The description of the variable '{variable}' is '{description}'.\n")


