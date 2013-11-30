#!/usr/bin/env python

import math
def sqrt(x):
	if x < 0:
		neg = True
		x = math.fabs(x)
	else: 
		neg = False
	if x == 0 or x == 1:
		return x

	res = 0.0
	low = 1.0
	high = x
	while low < high:
		mid = (high + low) / 2
		if mid > 46340:
			mid = 46341
			continue
		if math.fabs(mid ** 2 - x) < 0.01:
			res = mid
			break;
		if mid ** 2 > x:
			high = mid
		else:
			low = mid
	if not neg:
		return res
	else: 
		return "i" + str(res)


if __name__ == '__main__':
	print sqrt(2)
	print sqrt(-9)
	print sqrt(256)
	print sqrt(512)
