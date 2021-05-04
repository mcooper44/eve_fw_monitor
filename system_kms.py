#!/usr/bin/python3.8

import requests
import yaml

# LOAD PROJECT NAME AND CONTACT INFORMATION FOR THE HEADER
config_source = open("config_files/config.yaml", "r")
config = yaml.load(config_source, Loader=yaml.SafeLoader)
USER_AGENT =  f"{config['AGENT_PROJ']} Maintainer: {config['AGENT_NAME']}"

def get_zk_response(ID=None, ID_type='system', u_agent=USER_AGENT):
    '''
    Form an Url to GET a json response from zkill of
    kill data from an ID_type which could be any one of the fetch
    modifiers listed in the ID_types dictionary and which are laid out
    in the zkill api docs at
    https://github.com/zKillboard/zKillboard/wiki/API-(Killmails)

    this function returns a dictionary with the
    response
    ID param fed to the fuction
    ID_type param fed to the function
    URL composed by the function and used in the GET request
    '''

    # these are fetch modifiers.  they are  applied 
    # in the following format /ID_type/#/
    # example https://zkillboard.com/api/kills/regionID/10000002/ 

    ID_types = {'character' : 'characterID',
                'corp': 'corporationID',
                'alliance' : 'allianceID',
                'faction': 'factionID',
                'ship' : 'shipTypeID',
                'group' : 'groupID',
                'system' : 'solarSystemID',
                'region' : 'regionID',
                'war' : 'warID',
                'value': 'iskValue'}

    base = 'https://zkillboard.com/api/kills'
    fetch_mod = ID_types.get(ID_type, False)
    URL = None

    if fetch_mod and ID:
        URL = f'{base}/{fetch_mod}/{ID}/'
        print(URL)

    payload = {}
    headers = {'User-Agent': USER_AGENT,
               'Accept-Encoding': 'gzip'}

    response = requests.request("GET", URL, headers=headers, data=payload)

    return {'response':response, 'ID': ID, 'ID_type': ID_type, 'URL': URL}

if __name__ == '__main__':
    zk_response = get_zk_response(ID=10000002, ID_type='region')
    if zk_response['response']:
        try:
            print('printing the first few results from the response json')
            zk_resp = zk_response['response']
            zk_json = zk_resp.json()
            print(f'{zk_json}')
        except Exception as error:
            print('an error was raised!')
            print(f'by: {zk_response["ID"]} + {zk_response["ID_type"]}')
            print(error)
    else:
        print('failed to get response in main')
