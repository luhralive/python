#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os
from collections import Counter


def AnalyseCode(file):
    with open( file,'r',encoding='UTF-8') as f:
        txts =f.readlines()
        dicTemp = {"codeNum":0, "commentsNum":0, "EmptylineNum":0}
        it = iter(txts)
        incomment = False
        for line in it:#迭代器
            if line in ['\n','\r\n']:
                dicTemp['EmptylineNum'] += 1
            elif line.startswith("#") :
                dicTemp['commentsNum'] +=1
            elif line.startswith("'''") or line.startswith('"""'):
                dicTemp['commentsNum'] += 1
                incomment = not incomment
            else:
                if incomment == False:
                    dicTemp['codeNum'] += 1
                else:
                    dicTemp['commentsNum'] += 1
    return  dicTemp

def AnylyseFileAllCode(dir, fileType = ['.py', '.html']):

    dicTotal = {"codeNum":0, "commentsNum":0, "EmptylineNum":0}
    for file in os.listdir(dir):
        portion = os.path.splitext(file)
        if portion[1] in fileType:
            dicTemp = AnalyseCode(dir + '/' + file )
            dicTotal =dict( Counter(dicTotal) + Counter(dicTemp) )
    return dicTotal



if __name__=='__main__':
    dir = r'D:\git\Project\picture\showcode\test'
    dicTotal = AnylyseFileAllCode(dir)
    print(dicTotal)




