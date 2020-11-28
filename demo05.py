'''
class 声明类 类的首字母必须大写
类里的所有方法，都需要传一个参数，叫self
'''

class GirlFriend():
    '''
    女朋友
    '''
    '''
    def __init__(self):  #默认值
        self.sex = '女'
        self.hight = '170cm'
        self.weight = '55kg'
        self.haif = '大波浪'
        self.age = '18岁'
    '''
    
    def __init__(self,sex,hight,weight,haif,age):  #默认值
        self.sex = sex
        self.hight = hight
        self.weight = weight
        self.haif = haif
        self.age = age
    
    def caiyi(self,num):
        print(self.sex,self.hight,self.weight)
        if num == 1:
            print('跳舞')
        elif  num == 2:
            print('化妆')
        else:
            print('唱歌')
    
    def chuyi(self):
        print('下面和奶子')
    
    def work(self):
        print('秘书')

'''类的实例化
linyuner = GirlFriend('女','167cm','48kg','黑长直','21')
linyuner.chuyi()
linyuner.caiyi(1)
print(linyuner.sex)
'''

#继承
class Nvpengy(GirlFriend): #子类继承父类
    def chuyi(self): #类的重写
        print('少女时代')

linyuner = Nvpengy('女','171cm','55kg','直发','20')
linyuner.chuyi()
        