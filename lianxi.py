'''while 循环
highchengji = {} #创建字典，存储分数>=60 的学员
lowchengji = {} #创建字典，存储分数<60 的学员
studentlist = ['亚瑟','妲己','庄周','白起','廉颇','伽罗','镜'] #创建学员数组
a = 0 #定义一个变量，用来控制数组的下标变化
while a < len(studentlist):
    chengji = int(input('请输入'+studentlist[a]+'的成绩'))
    if chengji >= 60:
        highchengji[studentlist[a]] = chengji
    else:
        lowchengji[studentlist[a]] = chengji 
    a = a+1 #控制下标变化，每次循环都自+1

print("成绩合格的学员有:",highchengji)
print("成绩不合格的学员有:",lowchengji)
'''

'''for循环遍历
highchengji = {} #创建字典，存储分数>=60 的学员
lowchengji = {} #创建字典，存储分数<60 的学员
studentlist = ['亚瑟','妲己','庄周','白起','廉颇','伽罗','镜'] #创建学员数组
for a in range(len(studentlist)):
    chengji = int(input('请输入'+studentlist[a]+'的成绩'))
    if chengji >= 60:
        highchengji[studentlist[a]] = chengji
    else:
        lowchengji[studentlist[a]] = chengji 

print("成绩合格的学员有:",highchengji)
print("成绩不合格的学员有:",lowchengji)
'''

''' 99乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print(b,'*',a,'=',a*b,end="   ")
    print
'''

'''信号灯
print('-------------红灯时间----------')
for a in range(1,31):
    print('现在是第',a,'次红灯')
    if a==30:
        print('-------------绿灯时间----------')
        for b in range(1,36):
            print('现在是第',b,'次绿灯')
            if b==35:
                print('-------------黄灯时间----------')
                for c in range(1,4):
                    print('现在是第',c,'次黄灯')
'''      

'''注册账号
user = {}
az = ['a','b','c','d']
username = input('请输入账号')
password = input('请输入密码')
user['username'] = username
user['password'] = password

#a = len(user['username'])
#print(a)

if len(user['username'])<5 or len(user['username'])>8:
    print('账号不合法')
if len(user['password'])<6 or len(user['password'])>12:
    print('密码不合法')

print('注册成功')
'''

print(1)