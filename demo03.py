
def jiafa (a,b):
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return '非法参数'

c = jiafa(1,2)
try:
    print(c+'5')
except Exception as e:
    print('代码写错啦',e)
