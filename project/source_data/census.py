import us
from pathlib import Path
import zipfile
import urllib.request
import glob


def get_census(data_directory='../data/input/census'):
    """
    https://www2.census.gov/geo/tiger/TIGER2017/TABBLOCK/tl_2017_36_tabblock10.zip
    """

    pre_url = 'https://www2.census.gov/geo/tiger/TIGER2017/TABBLOCK'

    not_collected = []

    for state in us.states.STATES:
        fips = state.fips

        url = f'{pre_url}/tl_2017_{fips}_tabblock10.zip'

        if not Path(
            f'{data_directory}/tl_2017_{fips}_tabblock10.zip'
        ).is_file():

            try:
                urllib.request.urlretrieve(
                    url,
                    f'{data_directory}/tl_2017_{fips}_tabblock10.zip',
                )

                with zipfile.ZipFile(
                    f'{data_directory}/tl_2017_{fips}_tabblock10.zip',
                    "r"
                ) as zip_ref:
                    zip_ref.extractall(data_directory)

            except ConnectionError:
                print(f'{url} not collected')
                not_collected.append(url)

    return glob.glob(f"{data_directory}/*/*.shp")