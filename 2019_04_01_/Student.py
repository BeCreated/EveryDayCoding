#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Person import Person

class Student(Person):
    def __init__(self, name, age, school):
        # 父类同步初始化
        super(Student, self).__init__(name, age)
        self.school = school

    def learn(self):
        # 调用父类方法
        super().work('{}开始上学了'.format(self.name))
        print('{}正在学习...'.format(self.name))

    def get_school(self):
        print('{0}就读于{1}'.format(self.name, self.school))