import urllib.request
import os, json, uuid,sys

with open('walldropswalls.json', 'r') as f:
    data = json.load(f)

i=-1
for item in data["Backgrounds"]:
    data["Backgrounds"][item].update({'timestamp':i})
    tempfile = os.path.join(os.path.dirname('walldropswalls.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(tempfile, 'walldropswalls.json')
    i-=1
