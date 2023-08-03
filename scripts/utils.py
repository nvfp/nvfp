import json
import os


def shipping(name, data):
    
    DIR = os.path.abspath(os.path.join(os.environ['GITHUB_WORKSPACE'], '..', '__archive_stats__'))
    print(f'DEBUG: DIR: {repr(DIR)}.')
    if os.path.exists(DIR): raise AssertionError(f'Already exists: {repr(DIR)}.')

    print(f'INFO: Creating dir {repr(DIR)}.')
    os.mkdir(DIR)

    FILE = os.path.join(DIR, 'payload.json')

    with open(FILE, 'w') as f:
        load = {
            'name': name,
            'data': data,
        }
        json.dump(load, f)

    print('INFO: Shipped!')