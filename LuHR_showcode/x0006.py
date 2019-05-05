import os
import x0004

# 获取列表的第二个元素
def takesecond(e):
    return  e[1]

path = 'D:\git\Project\picture\showcode'

files = os.listdir(path)

txts = ''
for fileName in files:
    portion = os.path.splitext(fileName)
    if portion[1] == '.txt':
        txts += x0004.readFile(fileName)

listAll = x0004.getEwordsCount(txts)
# listAll.sort( key = lambda t:t[1],reverse=True)
listAll.sort(key=takesecond,reverse=True)

print (listAll)




