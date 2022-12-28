import os
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
    print(i)
    e = os.path.splitext(i.replace(" ", ""))[1]
    print(e)
    if e in ext:
        os.system(f"cp /Users/ranisujith/Downloads/\"{i}\" /Users/ranisujith/Downloads/" + e.replace(".", ""))
for f in files:
    os.remove("/Users/ranisujith/Downloads/" + f)
