#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Student import Student
from Teacher import Teacher

if __name__ == '__main__':
    s = Student('Tom', 17, '一高')
    s.sleep()
    s.learn()
    s.get_school()

    t = Teacher('Jack', 32, '一中')
    t.sleep()
    t.teach()
    t.get_school()

