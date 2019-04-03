#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
'''
可以切换上下级目录
可以增删改查本目录中的文件或目录
'''
class FileHelper(object):
    def __init__(self):
        self.present_dir = os.getcwd()
        self.parent = os.path.dirname(self.present_dir)

    def changeDirToParent(self):
        self.present_dir = self.parent
        self.parent = os.path.dirname(self.present_dir)
        print(self.present_dir, self.parent)
        return self

    def gainFilelist(self):
        all_file_list = os.listdir(self.present_dir)
        file_list = []
        dir_list = []
        print(all_file_list)
        for path in all_file_list:
            file_list.append(FileHelper.judgeTypeIsFile(self.present_dir, path))
            dir_list.append(FileHelper.judgeTypeIsDir(self.present_dir, path))
        return file_list, dir_list

    @staticmethod
    def judgeTypeIsFile(parent_path, file_path):
        path = os.path.join(parent_path, file_path)
        if os.path.isfile(path):
            return file_path
        return

    @staticmethod
    def judgeTypeIsDir(parent_path, dir_path):
        path = os.path.join(parent_path, dir_path)
        if os.path.isdir(path):
            return dir_path
        return

if __name__ == '__main__':
    f = FileHelper()
    file, dir = f.gainFilelist()
    print(file, dir)
    f.changeDirToParent()
    file, dir = f.gainFilelist()
    print(file, dir)

