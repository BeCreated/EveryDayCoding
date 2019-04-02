#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time

class TimeHelp(object):
    @staticmethod
    def getTimestamp(retain=None):
        timestamp = time.time()
        timestamp = round(timestamp, retain) if retain else round(timestamp)
        return timestamp

    @staticmethod
    def timestampToFormattime(timestamp=time.time(), format_pattern='%Y_%m_%d'):
        format_time = time.strftime(format_pattern, time.localtime(timestamp))
        return format_time

    @staticmethod
    def getFormatTime(format_pattern='%Y_%m_%d'):
        timestamp = time.time()
        todaytime = TimeHelp.timestampToFormattime(timestamp, format_pattern)
        return todaytime

if __name__ == '__main__':
    print(TimeHelp.getTimestamp())
    print(TimeHelp.getFormatTime('%Y_%m_%d'))
    print(TimeHelp.timestampToFormattime(1354200523))