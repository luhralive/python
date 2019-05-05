#做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
import string
import random

def get_ACCode(length=20,number= 200):

    chars =string.ascii_letters + string.digits
    AC_list = []
    for i in range(number):
        str = ''
        for j in range(length):
            str += random.choice(chars)
        AC_list.append(str)
    return AC_list
if __name__=='__main__':
    list = get_ACCode()
    print (list[1:200])