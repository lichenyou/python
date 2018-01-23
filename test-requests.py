#!/usr/bin/python
# -*- coding: utf-8 -*-


def fact(n):
    if n==1:
    	print ('haha')
        return 1

    else:
    	return n * fact(n - 1)

print (fact(5))