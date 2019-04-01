#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == '__main__':
    head = None
    for data in range(10):
        head = Node('第{}次入栈'.format(data), head)
    probe = head
    # 遍历栈
    while head != None:
        print('{}'.format(head.data))
        head = head.next

