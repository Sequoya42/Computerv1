# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computerv1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rbaum <rbaum@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/08/08 15:49:33 by rbaum             #+#    #+#              #
#    Updated: 2015/08/28 18:00:39 by rbaum            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0

import re
import sys

class bclr:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getmax(y, y2):
	x = 0
	for i in y:
		if i[2] > x:
			x = i[2]
	for i in y2:
		if i[2] > x:
			x = i[2]
	x = int(x) + 1
	return x

#------------------------#
def sqrt(t):
        r = t/2.0; t = float(t)
        i = 0
        while i < 10:
                r = (r+t/r)/2.0
                i += 1
        return r
#------------------------#

def parse(str):
	for ch in[' ', '^', '*']:
		if ch in str:
			str = str.replace(ch, '')
	left = re.findall("(([+|-]?[0-9].?[0-9]*)[Xx]([0-9])*)", str.split(('='))[0])
	right = re.findall("(([+|-]?[0-9].?[0-9]*)X([0-9])*)", str.split(('='))[1]) 
	list = []
	for x in reversed(range(0, getmax(left, right))):
		list += [(float(i[1]), int(i[2])) for i in left if int(i[2]) == x]
		list += [(-float(i[1]), int(i[2])) for i in right if int(i[2]) == x]
	list = sorted(list, key=lambda tup:tup[1], reverse=True)
	a = b = c = 0
	for i in list:
		if i[1] == 0:
			c += i[0]
		if i[1] == 1:
			b += i[0]
		if i[1] == 2:
			a += i[0]
	return a,b,c
# -----------------------------------------#

def solve(str):
	a,b,c = parse(str)
	print bclr.GREEN + "Equation sous la forme de:" ,
	print bclr.WARNING + "\t\t %dX2 (+) %dX (+) %d = 0" % (a, b, c) + bclr.ENDC
	d = (b**2) - (4 * a * c)
	if d < 0:
		print "No solution"
		return
	if d == 0:
		r = (- b) / (2 * a)
		print "result is %d" % (r)
		return
	x1 = ((- b) + sqrt(d)) / (2 * a)
	x2 = ((-b) - sqrt(d)) / (2 * a)
	print "x1 is :\t %f" % (x1)
	print "x2 is :\t %f" % (x2)
	# print "%dX2 (+) %dX (+) %d = 0" % (a, b, c)
	# print "delta is %f" % (d)
# -----------------------------------------#


if __name__ == '__main__':
    if len(sys.argv) == 2:
    	solve(sys.argv[1])
        # parse(sys.argv[1])
    else:
        print ("please enter your string in one argument in this form: \n\t"
        + bclr.GREEN + "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" + bclr.ENDC)




# -----------------------------------------## -----------------------------------------#

#         yolo = re.findall("(([+|-]?[0-9].?[0-9]*)X[0-9]*)", str)
#         print yolo[0]
# 	str = str.split(('='))
# 	left = str[0]
# 	right = str[1]
#         yolo = left + right
#         print yolo

# -----------------------------------------#

# def clean_data(data):
#     data_iter = iter(data)
#     for item in data_iter:
#         if item in {'+', '-'}:
#             yield item + next(data_iter)
#         else:
#             yield item

# -----------------------------------------#
