#!/usr/bin/env	python
# -*-coding: utf-8 -*-

import collections
import math
import copy

def main():
    source = open('source.txt','r')
    outf = open('result.txt','w')

    str = source.read()
    text = str.replace('\n','')

    count_dict = collections.Counter(text)
    count_dict = collections.OrderedDict(sorted(count_dict.items(),key=lambda x:x[1],reverse=True))

    length = len(text)
    element = len(count_dict)
    char_list = count_dict.keys()
    num_list = count_dict.values()

    p = [0] * element
    log = [0] * element
    l = [0] * element
    psum = [0] * element
    binary_list = [0] * element
    result = [0] * element

    for i in range(element):
        p[i] = round(num_list[i] * 1.0 / length,3)

        log[i] = round(math.log(1/p[i],2),3)
        l[i] = int(math.ceil(log[i]))
        lmax = max(l)
        if i != 0:
            psum[i] = round(psum[i-1] + p[i-1],3)
        else:
            psum[i] = 0.0
        result[i] = convert_binary(psum,i,lmax)
        outf.write(char_list[i]+"-->"+result[i]+"\n")

    #print result

    outf.close()
    source.close()

def convert_binary(psum,i,lmax):
    digit = [0] * lmax
    copy_psum = copy.deepcopy(psum)
    for j in range(lmax):
        if copy_psum[i] * 2 >= 1:
            out = 1
            copy_psum[i] = copy_psum[i] * 2 - 1
        else:
            out = 0
            copy_psum[i] = copy_psum[i] * 2
        digit[j] = out
    binary = ''.join([str(n) for n in digit])
    return binary

if __name__ == '__main__':
    main()

