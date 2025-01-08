from pyproj import CRS, Transformer

def convert_eeacellcode_to_latlon(eeacellcode, from_epsg=3035, to_epsg=4326):
    """
    Convert EEA cell code to latitude and longitude.

    Parameters:
    eeacellcode (str): The EEA cell code.
    from_epsg (int): EPSG code of the source coordinate system (default is 3035).
    to_epsg (int): EPSG code of the target coordinate system (default is 4326).

    Returns:
    tuple: (longitude, latitude)
    """
    # Define coordinate systems
    proj_from = CRS.from_epsg(from_epsg)
    proj_to = CRS.from_epsg(to_epsg)

    # Create a transformer
    transformer = Transformer.from_crs(proj_from, proj_to)

    # Function to convert ETRS89-LAEA coordinates to latitude and longitude
    def ETRS89_LAEA_to_latlon(easting, northing):
        lon, lat = transformer.transform(northing, easting)
        return lat,lon 

    # Function to convert EEA cell code to ETRS89-LAEA coordinates
    def eeacellcode_to_ETRS89_LAEA(eeacellcode):
        if 'km' in eeacellcode:
            cell_size = int(eeacellcode.split('km')[0]) * 1000
        else:
            cell_size = int(eeacellcode.split('m')[0])
        
        if 'N' in eeacellcode:
            northing_str = eeacellcode.split('N')[1]
            letter = 'N'
        else:
            northing_str = eeacellcode.split('S')[1]
            letter = 'S'
        
        if 'E' in eeacellcode:
            easting_str = eeacellcode.split('E')[1].split(letter)[0]
        else:
            easting_str = eeacellcode.split('W')[1].split(letter)[0]
        
        easting = int(easting_str) * cell_size
        northing = int(northing_str) * cell_size
        
        if 'S' in eeacellcode:
            northing = -northing
        if 'W' in eeacellcode:
            easting = -easting
        
        return easting, northing

    # Convert EEA cell code to ETRS89-LAEA coordinates
    easting, northing = eeacellcode_to_ETRS89_LAEA(eeacellcode)
    # Convert ETRS89-LAEA coordinates to latitude and longitude
    lat,lon = ETRS89_LAEA_to_latlon(easting, northing)
    return lat,lon
