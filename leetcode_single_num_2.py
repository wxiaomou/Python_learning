#! /usr/bin/env python

def singleNumber(num):
	if not len(num):
		return 0
	x = 0
	y = 0
	z = 0
	for i in num:
		y |= x & i
		x ^= i
		z = y & x
		y &= ~z
		x &= ~z
	return y

num = [1, 2, 3, 5, 123, 32, 5, 123, 123, 2, 3, 1, 32, 2, 3, 32, 1]
print singleNumber(num)
