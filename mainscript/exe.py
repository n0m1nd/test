#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from git import Git
from git.repo.base import Repo
import glob, os
import shutil
import subprocess
import time

# repodir - var to name directory that will be created, used and deleted
repodir = "clonedrepo"
# script, giturl, branch, number - args that passed to script
script, giturl, branch, number = argv

print ("Script " + script + " started with paramaters:" + "\nURL: " + giturl + "\nBranch: "+ branch + "\nNumber: " + number)

def git_clone(repo_url, ref):
    # repo_url - URL of git repo to clone
    # ref - branch, commit or reference in the repo to clone
    if repo_url == '':
        print("No repo URL")
    try:
        # Entering remote git URL and folder to save
        repo = Repo.clone_from(repo_url, repodir)
        # Getting selected branch files
        repo.remotes.origin.fetch(ref)
        # Working dir of Git
        g = Git(repo.working_dir)
        # Getting latest fetch
        g.checkout('FETCH_HEAD')
    except Exception:
        print("Git clone failed.")
        
def filejob(repodir):
    # filename - var of the 1st *.py script found to be executed
    filename = glob.glob(repodir + '/*.py')[0]
    # changing parameter to get access to file if any
    os.chmod(filename, 0o775)
    print("------------------------------")
    # executing file and printing his output
    output = subprocess.check_output(filename + " " + number, shell=True)
    print (output)
    # deleting folder that was downloaded with some time to cancel deletion in case of wrong folder
    print("Folder to delete: "+ repodir + "\nWaiting for possible interruption...")
    time.sleep(10)
    shutil.rmtree(repodir, ignore_errors=True)
    print(repodir + " deleted")     
    
git_clone(giturl, branch)
filejob(repodir)
