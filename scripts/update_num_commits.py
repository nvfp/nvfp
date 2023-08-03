import json
import os
import subprocess as sp
import sys
from datetime import datetime, timezone

GH_WORKSPACE = os.environ['GITHUB_WORKSPACE']
sys.path.append(GH_WORKSPACE)  # To make subdirs under repo root importable

from scripts.utils import get_stats_name, shipping


def main():

    ## Create a working dir for cloning
    CLONE_DIR = os.path.abspath(os.path.join(GH_WORKSPACE, '..', '__clone_dir__'))
    print(f'DEBUG: CLONE_DIR: {repr(CLONE_DIR)}.')
    if os.path.exists(CLONE_DIR): raise AssertionError(f'Already exists: {repr(CLONE_DIR)}.')
    print(f'INFO: Creating dir {repr(CLONE_DIR)}.')
    os.mkdir(CLONE_DIR)

    ## Get clone URLs
    cmd = ['gh', 'repo', 'list', 'nvfp', '--visibility', 'public', '--json', 'url']
    parsed = json.loads( sp.check_output(cmd, text=True) )
    print(f'DEBUG: parsed: {parsed}')

    ## Cloning
    print(f'DEBUG: os.listdir(CLONE_DIR): {os.listdir(CLONE_DIR)}')
    for url_in_dict in parsed:
        URL = url_in_dict['url'] + '.git'
        sp.run(['git', 'clone', URL], cwd=CLONE_DIR, check=True)
    print(f'DEBUG: os.listdir(CLONE_DIR): {os.listdir(CLONE_DIR)}')
    
    ## Count
    num_commits = 0
    for repo in os.listdir(CLONE_DIR):
        CWD = os.path.join(CLONE_DIR, repo)
        repo_commits = int(sp.check_output(['git', 'rev-list', '--count', 'HEAD'], cwd=CWD, text=True).strip())
        num_commits += repo_commits
        print(f'INFO: Repo {repr(repo)} has {repo_commits:,} commits.')
    print(f'DEBUG: num_commits: {num_commits}')

    NAME = get_stats_name(os.path.basename(__file__))
    TIME = datetime.now(timezone.utc).isoformat()
    data = [TIME, num_commits]
    shipping(NAME, data)


if __name__ == '__main__':
    main()