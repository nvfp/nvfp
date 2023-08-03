import json
import os
import subprocess as sp
import sys
from datetime import datetime, timezone

sys.path.append(os.environ['GITHUB_WORKSPACE'])

from scripts.utils import get_stats_name, shipping


def main():

    cmd = ['gh', 'repo', 'list', 'nvfp', '--visibility', 'public', '--json', 'stargazerCount']
    output = sp.check_output(cmd, text=True)

    parsed = json.loads(output)
    num_stargazers = sum([d['stargazerCount'] for d in parsed])
    print(f'DEBUG: parsed: {parsed}')
    print(f'DEBUG: num_stargazers: {num_stargazers}')

    NAME = get_stats_name(os.path.basename(__file__))
    TIME = datetime.now(timezone.utc).isoformat()    

    data = [TIME, num_stargazers]
    shipping(NAME, data)


if __name__ == '__main__':
    main()