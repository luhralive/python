#使用 Python 生成类似于下图中的字母验证码图片
import x0001
import random
from PIL import ImageDraw,Image,ImageFont,ImageFilter

width = 400
height = 200

def randonColor():
    return ( random.randint(0,255),random.randint(0,255),random.randint(0,255) )

def drawBackground(noiseRate = 50):
    img = Image.new('RGB', (width, height), (0,0,0))
    imgDraw = ImageDraw.Draw(img)
    for i in range(width):
        for j in range(height):
            if ( random.randint(1,100) < noiseRate ):
                imgDraw.point((i,j),randonColor())
    #draw font
    fontsize = 80
    imagefont = ImageFont.truetype('arial.ttf', fontsize)
    fontcolor = "#ff0000"
    msg = x0001.get_ACCode(4, 1)[0]

    font_width, font_height = imagefont.getsize(msg)
    x = 0
    y = 60
    i = 0
    for ch in msg:
        i+=1
        x = 16 *i+ (i -1)* 80
        imgDraw.text((x, y), ch, fontcolor,imagefont)
    img = img.filter(ImageFilter.BLUR)
    img.save('backpic.jpg')

drawBackground()