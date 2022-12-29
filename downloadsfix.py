#!/usr/bin/env python3

# Module Import
import os
import time
import shutil

# Getting all files and folders in downloads folder
filesandfolders = os.listdir("/Users/ranisujith/Downloads")

#Sorting out only the files in the downloads folder
files = []
for f in filesandfolders:
    if os.path.isfile("/Users/ranisujith/Downloads"+'/'+f):
        files.append(f)
        


# Getting all the file types available in the downloads folder
ext = []
for i in files:
    extensions = os.path.splitext(i.replace(" ", ""))
    ext.append(extensions[1])

# Making a folder for each file type inside the downloads folder
for e in ext:
    try:
        os.mkdir("/Users/ranisujith/Downloads/" + e.replace(".", ""))
    except:
        continue

# Moving files from downloads folder to their respective file type folders for easy viewing
for i in files:
    n, e = os.path.splitext(i.replace(" ", ""))
    src = "/Users/ranisujith/Downloads/" + i
    dest = "/Users/ranisujith/Downloads/" + e.replace(".", "") + "/" + i
    if i == ".DS_Store":
        continue
    else:
        shutil.move(src, dest)

# Final beautification commands
os.system("clear")
print("Files Sorted...")
time.sleep(2)
os.system("clear")
