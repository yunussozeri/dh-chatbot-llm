import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode

import pandas as pd
import matplotlib.pyplot as plt



def get_json_data():
    # set host, like http://localhost:8000, to where your Data Hub is running
    HOST = 'http://localhost:8000'
    # in case of basic auth set to HTTPBasicAuth('user', 'password')
    AUTH = None

    q = {
        'datalayer_key': 'koeppen_ds',

        # Optional filters to narrow down the returned data:
        #'shape_id': '',
        #'shape_type': '',
        #'start_date': '',
        #'end_date': '',
    }

    json_data = requests.get(f"{HOST}/api/datalayers/data/?{urlencode(q)}", auth=AUTH).json()

    #koeppen_ds_df = pd.DataFrame(d['data'])
    #koeppen_ds_df['year'] = pd.to_datetime(koeppen_ds_df['year'], format="%Y")
    #print(koeppen_ds_df['year'])

    return json_data['data']