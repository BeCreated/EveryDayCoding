#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('{}正在睡觉...'.format(self.name))

    def work(self, msg):
        print(msg)