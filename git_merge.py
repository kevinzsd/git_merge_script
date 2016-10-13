# create by Shida Zhong
# python script for merging branch to master and then push it to remote repository in GitHub
# please make sure the change in branch is committed and pushed
# usage: python git_merge.py -m "message for merging" -n branch_name

import os
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--message", required=True, type=str, help="Description for the update of branch")
ap.add_argument("-n", "--name", required=True, help="Name of the branch")
args = vars(ap.parse_args())

merge_comm = "git merge -m \"" + args["message"] + "\" " + args["name"]

os.system("git checkout master")
os.system("git pull origin master")
os.system(merge_comm)
os.system("git push -u origin master")
