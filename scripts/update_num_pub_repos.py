import json
import os
import subprocess as sp
import sys
from datetime import datetime, timezone

sys.path.append(os.environ['GITHUB_WORKSPACE'])

from scripts.utils import get_stats_name, shipping


def main():

    cmd = ['gh', 'repo', 'list', 'nvfp', '--visibility', 'public', '--json', 'name']
    output = sp.check_output(cmd, text=True)

    parsed = json.loads(output)
    num_pub_repos = len(parsed)
    print(f'DEBUG: parsed: {parsed}')
    print(f'DEBUG: num_pub_repos: {num_pub_repos}')

    NAME = get_stats_name(os.path.basename(__file__))
    TIME = datetime.now(timezone.utc).isoformat()    

    data = [TIME, num_pub_repos]
    shipping(NAME, data)


if __name__ == '__main__':
    main()