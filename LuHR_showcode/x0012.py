#敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'

import x0011
#txts = readFile()
def readFile():
    try:
        with open('filtered_words.txt',encoding='gbk') as f:
            fWordsList = f.read().split('\n')
            return  fWordsList
    except BaseException as e:
        print(e)

def changeWords(inputWords):
    fWordsList = readFile()
    for word in fWordsList:
        if word in inputWords:
            inputWords = inputWords.replace(word, '*'*len(word))
    print(inputWords)

while True:
    inputWords = input("Please input:")
    changeWords(inputWords)