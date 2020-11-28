'''
print("Hello World")
print(2) #整数
print(2.333) #小数
print(False)  #布尔值
print(()) #元组
print([]) #数组
print({}) #字典

举头望明月
低头思故乡

print("哈哈"+"嘻嘻")
print("女人"*50)
'''

"""
a = input("请输入：")
print("吃饭了吗:",a)

print(type(123))
print(type({}))

print(type(int("233333")))
print(type(str(333333)))


a = input("请输入：")
b = input("请再输入：")
print(int(a)+int(b))


a = '我是谁'
b = '憨憨龟'
print(len(a)+len(b))
print(123)


#元组
a = (1,2,3,4,5,5,5)
#print(a[4])
#print(a.index(3)) #位置
#print(a.count(5)) #计数

#二维元组
#b = (a,'哈哈','嘻嘻') 
#print(b[0][1]) 

#切片
#print(a[0:4])
print(a[0:])


#数组
#a = [1,2,3,4,5,5,5]
#a[0] = 0 修改
#a.append('append') 添加
#a.insert(0,'insert') 往固定位置插入
#b = a.pop(6) 剪切数据
#a.clear() 清空
#xx = ['蒜头王八','憨憨龟']
#a.extend(xx) 合并其他数组
#a.remove(5) 删除某个值
#print(a[0:])

#字典
a = {
    "name":"蒜头王八",
    'sex':'未知',
    'age':'10'}

a["hight"] = '183cm' #新增
a["sex"] = 'man' #修改
#a.update(sex='woman') 修改
print(a["name"],a['hight'],a['sex']) #取值

#数组和字典的删除
del a["hight"]
print(a)
"""

a = input('请输入姓名:')
b = input('请输入年纪:')
c = input('请输入性别:')

d = {'姓名':a,'年纪':b,'性别':c}
print(d)
