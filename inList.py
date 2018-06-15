#!/usr/bin/env python
# -*- coding: utf-8 -*-

number = range(5)
#a = input("plz input a number:")

def inList(n,list01):
	c = 0
	while c < len(list01):
		if list01[c] == n:
			return True
			break
		c = c + 1
	
	return False

print inList(0,range(1,559))