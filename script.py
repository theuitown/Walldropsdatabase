import urllib.request
import os, json, uuid,sys

with open('done.json', 'r') as f:
    data = json.load(f)

for item in data["CategoryBackground"]:
    img_url = data["CategoryBackground"][item]['imageUrl']
    img_name = os.path.basename(img_url)
    print(json.dumps(data["CategoryBackground"][item]['imageUrl']))
    urllib.request.urlretrieve(img_url,'/home/iamharsh/Walldropsdatabase/wallpapers/categories/'+img_name)
    newImageLink='https://raw.githubusercontent.com/theuitown/Walldropsdatabase/master/wallpapers/categories/'+img_name
    data["CategoryBackground"][item]['imageUrl']=newImageLink
    tempfile = os.path.join(os.path.dirname('done.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(tempfile, 'done.json')
