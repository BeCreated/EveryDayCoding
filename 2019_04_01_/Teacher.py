#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Person import Person

class Teacher(Person):
    def __init__(self, name, age, school):
        super(Teacher, self).__init__(name, age)
        self.school = school

    def teach(self):
        super().work('{}开始上班了'.format(self.name))
        print('{}正在教课'.format(self.name))

    def get_school(self):
        print('{0}就职于{1}'.format(self.name, self.school))