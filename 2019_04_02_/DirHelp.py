#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

class DirHelp(object):

    @staticmethod
    def checkDirExistsAndCreate(dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        return True

    @staticmethod
    def getDirPathFormFilepath(filepath):
        dir_name = os.path.dirname(filepath)
        return dir_name