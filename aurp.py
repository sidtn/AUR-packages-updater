#!/usr/bin/python3

import os
import sys


def find_aur_packages(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == "PKGBUILD":
                os.chdir(root)
                pull_result = os.popen('git pull').read().strip()
                if pull_result == "Already up to date.":
                    print(f"[INFO] Package {root} has no updates")
                    continue
                else:
                    ask = input(f"[INFO] Package {root} has new version. Update? y/n")
                    if ask == "y" or ask == "Y":
                        os.system("makepkg -si")
                    else:
                        continue


if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        path = os.path.abspath(os.getcwd())
    try:
        print(f"[INFO] Search in {os.path.abspath(path)}")
        find_aur_packages(path)
    except OSError:
        print(f"[Error] {path} is not valid path")
