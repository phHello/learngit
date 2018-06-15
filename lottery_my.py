#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

# 判断一个数是否在一个list中
def inList(n,list01):
	x = 0
	while x < len(list01):
		if list01[x] == n:
			return True
			break
		x = x + 1
	
	return False

#[star,end]中随机num个不重复的随机数
def lottery_my(stat,end,num):
	
	number = [random.randint(stat,end)]
	
	x = 0
	while x < num - 1:
		b = random.randint(stat,end)
		#if b in number: （可以直接使用in）
		if (inList(b,number)):
			x = x - 1
		else:
			number.append(b)
		
		x = x + 1
	return number	


#1~35中\，5个不重复的随机数
#print  lottery_my(1,35,5) +lottery_my(1,12,2)
print lottery_my(1,33,6)+lottery_my(1,16,1)

