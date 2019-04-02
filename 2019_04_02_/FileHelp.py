#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pickle
from DirHelp import DirHelp


class FileHelp(object):

    @staticmethod
    def writeDataToFile(data, filename, mode='a+'):
        try:
            with open(filename, mode, encoding='utf-8') as file:
                file.write(data)
            return True
        except FileNotFoundError as e:
            dir_name = DirHelp.getDirPathFormFilepath(filename)
            DirHelp.checkDirExistsAndCreate(dir_name)
            FileHelp.writeDataToFile(data, filename)

    @staticmethod
    def readDataFromFile(filename, mode='r'):
        with open(filename, mode, encoding='utf-8') as file:
            data = file.read()
        return data

    @staticmethod
    def pickleWriteDataToFile(data, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
            return True
        except FileNotFoundError as e:
            dir_name = DirHelp.getDirPathFormFilepath(filename)
            DirHelp.checkDirExistsAndCreate(dir_name)
            FileHelp.writeDataToFile(data, filename)

    @staticmethod
    def pickleReadDataFromFile(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data

if __name__ == '__main__':
    FileHelp.writeDataToFile('nih\nao', 'f/ggg/ll.txt')
    print(FileHelp.readDataFromFile('ll.txt'))
    FileHelp.pickleWriteDataToFile('nidd', 'f/ggg/ll.txt')
    print(FileHelp.pickleReadDataFromFile('dd.txt'))
