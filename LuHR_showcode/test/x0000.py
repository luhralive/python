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

