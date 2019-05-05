import os
from PIL import Image

path = 'D:\git\Project\picture\showcode'

def change_picSize(fileName,width = 1136,hight = 640):
    img = Image.open(fileName)

    img.thumbnail((width, hight))#只能变小
    img.save(fileName)
    print (fileName + ' DONE!')

PHONE = {'iPhone5':(1136,640), 'iPhone6':(1134,750), 'iPhone6P':(2208,1242)}
files = os.listdir(path)
width,height = PHONE['iPhone6P']
for fileName in files:
    portion = os.path.splitext(fileName)
    if portion[1] == ".jpg" or portion[1] == ".png":
        change_picSize(fileName,width,height)

