# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computerv1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rbaum <rbaum@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/08/08 15:49:33 by rbaum             #+#    #+#              #
#    Updated: 2015/08/28 22:57:34 by rbaum            ###   ########.fr        #
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
        r = t/2.0
        t = float(t)
        i = 0
        while i < 10:
                r = ((r + t) / r) / 2.0
                i += 1
        return r
#------------------------#

def parse(str):
	for ch in[' ', '^', '*']:
		if ch in str:
			str = str.replace(ch, '')
	left = re.findall("(([+|-]?[0-9].?[0-9]*)[Xx]([0-9])*)", str.split(('='))[0])
	right = re.findall("(([+|-]?[0-9].?[0-9]*)[Xx]([0-9])*)", str.split(('='))[1]) 
	print left
	print right
	lst = []
	for x in reversed(range(0, getmax(left, right))):
		lst += [(float(i[1]), int(i[2])) for i in left if int(i[2]) == x]
		lst += [(-float(i[1]), int(i[2])) for i in right if int(i[2]) == x]
	lst = sorted(lst, key=lambda tup:tup[1], reverse=True)
	return lst

# -----------------------------------------#

def alpha_bet(str):
	lst = parse(str)
	a = b = c = 0
	for i in lst:
		if i[1] == 0:
			c += i[0]
		if i[1] == 1:
			b += i[0]
		if i[1] == 2:
			a += i[0]
	return a,b,c, lst

# -----------------------------------------#


def solve_one(b, c):
	r = (- c) / b
	print bclr.GREEN + "Reduced form:" ,
	print bclr.WARNING + "\t\t %0.2f * X^1 (+) %0.2f = 0" % (b, c) + bclr.ENDC
	print "result for x is : %0.3f" % r


# -----------------------------------------#

def solve_none(c):
	print "Every real number is solution"

# -----------------------------------------#
def get_degree(lst):
	x = 0
	return x
# -----------------------------------------#

def solve(str):
	a,b,c, lst = alpha_bet(str)
	if b == 0 and a == 0:
		return solve_none(c)
	elif a == 0:
		return solve_one(b, c)
	print bclr.GREEN + "Equation sous la forme de:" ,
	print bclr.WARNING + "\t\t %0.2f * X^2 + %0.2f * X^1 + %0.2f = 0" % (a, b, c) + bclr.ENDC
	print bclr.BLUE + "\t\t\t\t\t %dX2 + %dX + %d = 0" % (a, b, c) + bclr.ENDC
	d = (b**2) - (4 * a * c)
	if d < 0:
		print "No solution"
		return
	elif d == 0:
		r = (- b) / (2 * a)
		print "x is %d" % (r)
		return
	x1 = ((- b) + sqrt(d)) / (2 * a)
	x2 = ((-b) - sqrt(d)) / (2 * a)
	print "x1 is :\t %f" % (x1)
	print "x2 is :\t %f" % (x2)
# -----------------------------------------#


if __name__ == '__main__':
    if len(sys.argv) == 2:
    	solve(sys.argv[1])
    else:
        print ("please enter your string in one argument in this form: \n\t"
        + bclr.GREEN + "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" + bclr.ENDC)
