import datetime
import json
import os
import subprocess as sp
import time


REPO_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAT_FILE_PATH = os.path.join(REPO_ROOT_DIR, 'stats', 'total_pub_repo.json')


def main():
    print(f'DEBUG: REPO_ROOT_DIR : {repr(REPO_ROOT_DIR)}.')
    print(f'DEBUG: STAT_FILE_PATH: {repr(STAT_FILE_PATH)}.')
    
    with open(STAT_FILE_PATH) as f:
        stats = json.load(f)

    command = ['gh', 'repo', 'list', 'nvfp', '--visibility', 'public', '--json', 'name']
    output = sp.check_output(command, text=True)
    data = json.loads(output)
    print(data)
    print('---')
    print(type(data))
    print('---')
    print(repr(data))

    with open(STAT_FILE_PATH, 'w') as f:
        json.dump(stats, f, indent=4)


if __name__ == '__main__':
    main()