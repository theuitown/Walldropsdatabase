import urllib.request
import os, json, uuid,sys

with open('walldrops-d3df3-export.json', 'r') as f:
    data = json.load(f)

for item in data["Backgrounds"]:
    img_url = data["Backgrounds"][item]['imageLink']
    img_name = os.path.basename(img_url)
    urllib.request.urlretrieve(img_url,'/home/iamharsh/Walldropsdatabase/wallpapers/'+img_name)
    # newImageLink=
    # tempfile = os.path.join(os.path.dirname('walldrops-d3df3-export.json'), str(uuid.uuid4()))
    # with open(tempfile, 'w') as f:
    #     json.dump(data, f, indent=4)
    #               # rename temporary file replacing old file
    # os.rename(tempfile, 'hotels.json')