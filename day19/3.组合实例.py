# 圆形类
# 写一个圆环类 组合 圆形类 去完成 计算圆环的面积和周长
# 一个类的对象作为另一个类对象的属性
# 圆环中有圆

# 圆形类 ： 计算圆形面积 和 周长
# 圆环类 :
    # 圆环的周长 ： 大圆周长加小圆周长
    # 圆环的面积 :  大圆的面积 - 小圆的面积

# class Ring1:
#     def __init__(self,out_r,in_r):
#         self.out_r = out_r
#         self.in_r = in_r
#     def cal_area(self):
#         return abs(pi*self.out_r**2 - pi*self.in_r**2)
#     def cal_perimeter(self):
#         return pi * self.out_r * 2 + pi * self.in_r * 2

# from math import pi
# class Circle:   # 圆形的面积公式不会变
#     def __init__(self,r):
#         self.r = r
#     def cal_area(self):
#         return pi*self.r**2
#     def cal_perimeter(self):
#         return pi * self.r * 2

#
# class Ring2:  # 圆环
#     def __init__(self,out_r,in_r):
#         c1_obj = Circle(out_r)
#         self.out_circle = c1_obj
#         self.in_circle = Circle(in_r)
#     def area(self):
#         return self.out_circle.cal_area() - self.in_circle.cal_area()
#     def cal_perimeter(self):
#         return self.out_circle.cal_perimeter() + self.in_circle.cal_perimeter()
#
#
# r1 = Ring2(10,5)
# print(r1.area())
# print(r1.cal_perimeter())

# 老师
# 姓名 年龄 性别 班级 ： s11

# 班级
# 班级名 班级人数 科目 性质

class Clas:
    def __init__(self,name,num,course,type):
        self.name = name
        self.num = num
        self.course = course
        self.type = type

class Teacher:
    def __init__(self,name,sex,age,py11):
        self.name = name
        self.sex = sex
        self.age = age
        self.cls = py11

py11 = Clas('超级无敌s11',89,'python','脱产全栈')
print(py11.course)

boss_jin = Teacher('太白','？',40,py11)
print(py11.course)          # 11期的课程
print(boss_jin.cls.course)  # 金老板所带的班级的课程
print(boss_jin.cls.name)  # 金老板所带的班级的课程
print(boss_jin.cls.num)  # 金老板所带的班级的课程

