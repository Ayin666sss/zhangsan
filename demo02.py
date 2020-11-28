#判断
'''
a = 1
b = 2

if a==1:
    print('嘻嘻嘻')

if a>b:
    print('a大于b')
else:
    print('b大于a')

age = int(input("请输入年龄:"))

if age>60 and age<=70:
    print('该退休了')
elif age>30:
    print('想上不同的女人')
elif age>20:
    print('努力学习')
else:
    print('好好学习')
'''

'''
a = '憨憨龟'

if a in '蒜头王八和憨憨龟':
    print('yes,OK!')
else:
    print('No')
'''

'''
a = input('请输入:')

if a is int:
    print('是数字')
else:
    print('不是数字')
'''

'''
a = 1
while a<10:
    print('哈哈')
    a = a+1
'''

''' 练习题
a = int(input('蒜头王八的成绩是:'))
b = int(input('憨憨龟的成绩是:'))
c = int(input('皮卡丘的成绩是:'))
d = {'蒜头王八':a,'憨憨龟':b,'皮卡丘':c}
e = [] #60分以上
f = [] #60分以下

if  d['蒜头王八']>=60:
    e.append(d['蒜头王八'])
else:
    f.append(d['蒜头王八'])

if  d['憨憨龟']>=60:
    e.append(d['憨憨龟'])
else:
    f.append(d['憨憨龟'])

if  d['皮卡丘']>=60:
    e.append(d['皮卡丘'])
else:
    f.append(d['皮卡丘'])

print('合格分数有:',e)
print('不合格分数有:',f)
'''

'''
a = '今天吃饭了吗'
for i in a:
    print(i)
'''

#b = list(range(0,100,2)) #自动生成了一个数列，步进/步长
#print(b)

for i in range(100):
    print(i)


print(1)