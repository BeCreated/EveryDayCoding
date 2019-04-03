#!/usr/bin/python3
# -*- coding: utf-8 -*-
import jieba
import numpy

def readStopwords(filepath):
    # 加载停用词
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def sepString(str):
    cut_list = jieba.cut(str)
    stop_words = readStopwords('stopword.txt')

    word_list = []
    for str in cut_list:
        if str not in stop_words:
            word_list.append(str)

    return word_list



if __name__ == '__main__':
    print(sepString('好好学习，天天向上'))