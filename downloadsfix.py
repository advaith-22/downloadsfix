#!/usr/bin/env python3
import os
import time
files = os.listdir("/Users/ranisujith/Downloads")
files = [f for f in files if os.path.isfile("/Users/ranisujith/Downloads"+'/'+f)]
ext = []

for i in files:
    extensions = os.path.splitext(i.replace(" ", ""))
    ext.append(extensions[1])

for e in ext:
    try:
        os.mkdir("/Users/ranisujith/Downloads/" + e.replace(".", ""))
    except:
        continue

for i in files:
    e = os.path.splitext(i.replace(" ", ""))[1]
    if e in ext:
        try:
            os.system(f"mv /Users/ranisujith/Downloads/\"{i}\" /Users/ranisujith/Downloads/" + e.replace(".", ""))
        except:
            continue


print("Files Sorted ... ")
time.sleep(2)
os.system("clear")

