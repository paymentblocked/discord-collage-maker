import requests
import json

def runPictures(pictures):
    lengthPic = len(pictures)-1
    links = []
    while lengthPic >= 0:
        links.append(pictures[lengthPic][0])
        lengthPic = lengthPic-1
    return links

def requestPics(arrays):
    count = len(arrays)-1
    for r in arrays:
        myfile = requests.get(r).content
        with open(f"pictures/{count}_image.jpg", "wb") as handler:
            handler.write(myfile)
        count = count-1

def checkDupes():
    with open('checkLinks.json') as user_file:
        contents = user_file.read()

    parsed = json.loads(contents)
    newList = []

    for i in parsed["links"]:
        if i not in newList:
            newList.append(i)

    parsed["links"] = newList

    with open('checkLinks.json', 'w') as user_file:
        json.dump(parsed, user_file,indent = 4)
