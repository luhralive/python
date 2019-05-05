#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
def readFile(file = 'filtered_words.txt'):
    try:
        with open(file,'r',encoding='gbk') as f:
            txts = f.readlines()
            return txts
    except BaseException as e:
        print(e)

def checkWords(input_words):
    flag = False
    txts = readFile()
    for ch in txts:
        ch1 = ch.replace('\n', '')
        if ch1 == input_words:
            flag = True
            break
    return flag
if __name__ == '__main__':

    while True:
        input_words = input("Please input:")
        if checkWords(input_words): #敏感
            print('Freedom')
        else:
            print('Human Rights')
