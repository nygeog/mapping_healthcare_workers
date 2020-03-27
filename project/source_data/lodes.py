from pathlib import Path
import urllib.request
import glob
import time
import us


def get_lodes(data_directory='../data/input/lodes'):
    '''
    https://lehd.ces.census.gov/data/lodes/LODES7/ny/od/ny_od_aux_JT00_2017.csv.gz

    main part includes jobs with both workplace and residence in the
    state and the aux part includes jobs with the workplace in the
    state and the residence outside of the state.

    2017 for alaska and south dakota don't seem to exist,
    maybe try 2016

    :return:
    '''
    pre_url = 'https://lehd.ces.census.gov/data/lodes/LODES7'

    non_collected = []

    collected_lodes = {}

    for year in ['2016']:  # '2017']:
        for state in us.states.STATES:
            sa = state.abbr.lower()
            for f in ['aux', 'main']:

                url = f'{pre_url}/{sa}/od/{sa}_od_{f}_JT00_{year}.csv.gz'

                if not Path(
                    f'{data_directory}/{sa}_od_{f}_JT00_{year}.csv.gz'
                ).is_file():

                    print(url)

                    try:
                        urllib.request.urlretrieve(
                            url,
                            f'{data_directory}/{sa}_od_{f}_JT00_{year}.csv.gz',
                        )

                        time.sleep(1)

                    except ConnectionError:
                        print(f'{url} not collected')
                        non_collected.append(url)



            if not Path(f'{data_directory}/{sa}_xwalk.csv.gz').is_file():
                urllib.request.urlretrieve(
                    f'{pre_url}/{sa}/{sa}_xwalk.csv.gz',
                    f'{data_directory}/{sa}_xwalk.csv.gz',
                )

    cross_walk_files = glob.glob(f"{data_directory}/*_xwalk.csv.gz")

    collected_lodes[year] = glob.glob(f"{data_directory}/*{year}.csv.gz")

    return collected_lodes, cross_walk_files

