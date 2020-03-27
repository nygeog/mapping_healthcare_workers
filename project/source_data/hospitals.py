import geopandas as gpd
from pathlib import Path


def get_hospitals(data_directory='../data/input/hospitals'):
    '''
    This feature class/shapefile contains locations of Hospitals for 50 US
    states, Washington D.C., US territories of Puerto Rico, Guam, American
    Samoa, Northern Mariana Islands, Palau, and Virgin Islands. The dataset only
    includes hospital facilities based on data acquired from various state
    departments or federal sources which has been referenced in the SOURCE
    field. Hospital facilities which do not occur in these sources will be not
    present in the database. The source data was available in a variety of
    formats (pdfs, tables, webpages, etc.) which was cleaned and geocoded and
    then converted into a spatial database. The database does not contain
    nursing homes or health centers. Hospitals have been categorized into
    children, chronic disease, critical access, general acute care, long term
    care, military, psychiatric, rehabilitation, special, and women based on
    the range of the available values from the various sources after removing
    similarities. In this update the TRAUMA field was populated for 172
    additional hospitals and helipad presence were verified for all hospitals.

    https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals
    website also includes pharmacies

    another source is here: or https://data.hrsa.gov/geo
    '''

    if not Path(f"{data_directory}/hospitals.gpkg").is_file():
        hospitals = gpd.read_file(
            '{}/{}'.format(
                'https://opendata.arcgis.com/datasets',
                '6ac5e325468c4cb9b905f1728d6fbf0f_0.geojson',
            )
        )

        hospitals.to_file(
            f"{data_directory}/hospitals.gpkg",
            # layer="hospitals",
            driver="GPKG",
        )

        return hospitals

    else:
        return gpd.read_file(f"{data_directory}/hospitals.gpkg")
