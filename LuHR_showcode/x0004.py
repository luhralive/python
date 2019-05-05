#coding:utf-8
#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

def readFile(file = 'input.txt'):
    try:
        with open(file,'r',encoding='UTF-8') as f:
            txts = f.read()
    except BaseException as e:
        print(e)
    return txts


def getEwordsCount(txts):
    words = re.compile('([a-zA-Z]+)')
    dic = {}
    for x in words.findall(txts):
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    L = []
    for k,v in dic.items(): #items以列表返回可遍历的(键, 值) 元组数组
        L.append((k, v))

    # return L.sort( key = lambda t:t[0])
    L.sort( key = lambda t:t[0])
    return L

if __name__ == '__main__':
    txts = readFile()
    list1 = getEwordsCount(txts)
    print(list1)











