#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib

class EncryptHelp(object):

    @staticmethod
    def _getHexdigest(data, mode, coding):
        mode.update(data.encode(coding))
        return mode.hexdigest()

    @staticmethod
    def privDataSha1(data, coding='utf-8'):
        mode = hashlib.sha1()
        return EncryptHelp._getHexdigest(data, mode, coding)

    @staticmethod
    def privDataSha224(data, coding='utf-8'):
        mode = hashlib.sha3_224()
        return EncryptHelp._getHexdigest(data, mode, coding)

    @staticmethod
    def privDataMD5(data, coding='utf-8'):
        mode = hashlib.md5()
        return EncryptHelp._getHexdigest(data, mode, coding)

    @staticmethod
    def privDatasha256(data, coding='utf-8'):
        mode = hashlib.sha256()
        return EncryptHelp._getHexdigest(data, mode, coding)

if __name__ == '__main__':
    print(EncryptHelp.privDataSha1('nihao'))