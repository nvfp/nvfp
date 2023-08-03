import json
import os


GH_WORKSPACE = os.environ['GITHUB_WORKSPACE']
PAYLOAD = os.path.abspath(os.path.join(GH_WORKSPACE, '..', '__archive_stats__', 'payload.json'))
print(f'DEBUG: GH_WORKSPACE: {repr(GH_WORKSPACE)}.')
print(f'DEBUG: PAYLOAD: {repr(PAYLOAD)}.')


def main():
    
    ## Loading
    with open(PAYLOAD, 'r') as f:
        _load = json.load(f)
        print(f'DEBUG: _load: {_load}.')
        name = _load['name']
        data = _load['data']

    ## Stats dir
    NAME = os.path.join(GH_WORKSPACE, name)
    if not os.path.isdir(NAME):
        raise NotADirectoryError(f'Invalid `name` value: {repr(name)}.')

    NUM_ARCHIVES = len(os.listdir(NAME))
    print(f'DEBUG: NUM_ARCHIVES: {NUM_ARCHIVES}.')

    ## Target db
    TARGET = os.path.join(NAME, f'archive-{NUM_ARCHIVES}.json')
    print(f'DEBUG: TARGET: {repr(TARGET)}.')

    with open(TARGET, 'r') as f:
        db = json.load(f)
        num_data = len(db)
        print(f'DEBUG: num_data: {num_data}.')

        if num_data == 7:  # Testing purposes
        # if num_data == 1000:
            TARGET = os.path.join(NAME, f'archive-{NUM_ARCHIVES + 1}.json')
            print(f'DEBUG: New target: TARGET: {repr(TARGET)}.')
            db = []

    ## New data
    db.append(data)

    ## Save
    with open(TARGET, 'w') as f:
        json.dump(db, f, indent=2)

    print('INFO: Done.')


if __name__ == '__main__':
    main()