# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
from PIL import Image,ImageDraw,ImageFont

def add_num( imgPath, color = "#ff0000", msg = '4'):
    try:
        img = Image.open(imgPath, 'r')
        draw = ImageDraw.Draw(img)
        imagefont = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 40)
        width, height = img.size

        draw.text( (width - 40, 0),msg, font=imagefont, fill=color) #左上角为原点，Y轴向下
        img.save('result.jpg', 'jpeg')

    except:
        print("can't load picture")

if __name__ == "__main__":
    add_num('D:/git/Project/picture/showcode/picture01.jpg',msg = '5')

