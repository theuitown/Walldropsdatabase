import urllib.request
import os, json, uuid,sys

with open('walldrops-d3df3-export.json', 'r') as f:
    data = json.load(f)

for item in data["Backgrounds"]:
    img_url = data["Backgrounds"][item]['imageLink']
    img_name = os.path.basename(img_url)
    urllib.request.urlretrieve(img_url,'/home/iamharsh/Projects/Downloads_walls/wallpapers/'+img_name)