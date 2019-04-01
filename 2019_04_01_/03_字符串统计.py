#!/usr/bin/python3
# -*- coding: utf-8 -*-

class StrHelp(object):
    def __init__(self, s):
        self.str = s

    def count(self):
        str_list = list(self.str)
        str_set = set(str_list)
        str_dict = dict()
        for word in str_set:
            str_dict.update({word:str_list.count(word)})
        return str_dict

if __name__ == '__main__':
    s = 'abdfdgarrytyiuiouikghnstys==='
    print(StrHelp(s).count())
