import urllib.request
import os, json, uuid,sys

with open('walldrops-bck.json', 'r') as f:
    data = json.load(f)

i=133
for item in data["Backgrounds"]:
    img_url = data["Backgrounds"][item]['imageLink']
    img_name = os.path.basename("walldrops"+str(i)+".jpg")
    print(json.dumps(data["Backgrounds"][item]['imageLink']))
    urllib.request.urlretrieve(img_url,'/home/iamharsh/Walldropsdatabase/wallpapers/'+img_name)
    newImageLink='https://raw.githubusercontent.com/theuitown/Walldropsdatabase/master/wallpapers/'+img_name
    data["Backgrounds"][item]['imageLink']=newImageLink
    tempfile = os.path.join(os.path.dirname('walldrops-bck.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(tempfile, 'walldrops-bck.json')
    i+=1
