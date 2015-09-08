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

import re, sys

class bclr:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#------------------------#

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
	lst = []
	for ch in[' ', '^', '*']:
		if ch in str:
			str = str.replace(ch, '')
	test = re.search("(([+|-]?[0-9]?[0-9]*)[Xx]([0-9])*)", str.split(('='))[0])
	test2 = re.search("(([+|-]?[0-9]?[0-9]*)[Xx]([0-9])*)", str.split(('='))[0])
	print test
	print test2
	if not test or not test2:	
		return lst, -17
	left = re.findall("(([+|-]?[0-9]?[0-9]*)[Xx]([0-9]*))", str.split(('='))[0])
	right = re.findall("(([+|-]?[0-9]?[0-9]*)[Xx]([0-9]*))", str.split(('='))[1]) 
	print left
	print right
	m = getmax(left, right)
	for x in reversed(range(0, m)):
		lst += [(float(i[1]), int(i[2])) for i in left if int(i[2]) == x]
		lst += [(-float(i[1]), int(i[2])) for i in right if int(i[2]) == x]
	lst = sorted(lst, key=lambda tup:tup[1], reverse=True)
	return lst, m

# -----------------------------------------#

def alpha_bet(str):
	lst, m = parse(str)
	if m == -17 and lst == []:
		return 0, 0, 0, "because the input is invalid"
	a = b = c = t = tt = 0
	for n in reversed(range(0, m)):
		for i in lst:
			if i[1] == n == 2:
				a += i[0]
				print a, i[0]
			elif i[1] == n == 1:
				b += i[0]
				print b, i[0], n, i[1], i
			elif i[1] == n == 0:
				c += i[0]
			elif i[1] == n:
				t += i[0]
		if t != 0:
			if n > 2:
				return 0, 0, 0, n
		else:
			t = 0
	return a,b,c, lst

# -----------------------------------------#

def solve_one(b, c):
	r = (- c) / b
	print "Polynomial degree one. Unique solution"
	print bclr.GREEN + "Reduced form:" ,
	print bclr.WARNING + "\t\t %0.2f * X^1 (+) %0.2f = 0" % (b, c) + bclr.ENDC
	print bclr.BLUE + "\t\t\t %dX + %d = 0" % (b, c) + bclr.ENDC
	print "result for x is : %0.3f" % r


# -----------------------------------------#
def base_form(a,b,c):
	print bclr.GREEN + "\nEquation sous la forme de:" ,
	print bclr.WARNING + "\t\t %0.2f * X^2 + %0.2f * X^1 + %0.2f = 0" % (a, b, c) + bclr.ENDC
	print bclr.BLUE + "\t\t\t\t\t %dX2 + %dX + %d = 0" % (a, b, c) + bclr.ENDC

# -----------------------------------------#

def solve_none(c):
	print "Every real number is solution"

# -----------------------------------------#

def complex_solution(a, b, c, d):
	both = -b / (2 * a)
	print bclr.GREEN +  "\n Negative delta, complex solution (i where sqrt(i) = -1)" +  bclr.ENDC
	x1 =  sqrt(d) / (2 * a)
	print "\nx1 is %0.2f + i * %.2f" % (both , x1)
	print "x2 is %0.2f - i * %.2f" % (both , x1)
	print "x1 can also be written as : \t ( %.2f + (i * %.2f)) / %.2f" % (-b, sqrt(d), 2*a)
	print "x2 can also be written as : \t ( %.2f - (i * %.2f)) / %.2f" % (-b, sqrt(d), 2*a)


# -----------------------------------------#

def solve_two(b, d, a):
	x1 = ((- b) + sqrt(d)) / (2 * a)
	x2 = ((-b) - sqrt(d)) / (2 * a)
	print "x1 is :\t %f" % (x1)
	print "x2 is :\t %f" % (x2)

# -----------------------------------------#

def solve(str):
	a,b,c, lst = alpha_bet(str)
	if a == b == c == 0:
		print "cannot solve polynomial degree" ,  lst
		return 
	if b == a == 0:
		return solve_none(c)
	elif a == 0:
		return solve_one(b, c)
	base_form(a,b,c)
	d = (b**2) - (4 * a * c)
	if d < 0:
		return complex_solution(a, b, c, d)
	elif d == 0:
		r = (- b) / (2 * a)
		print "x is %d" % (r)
		return
	solve_two(b,d,a)

# -----------------------------------------#
# -----------------------------------------#

if __name__ == '__main__':
    if len(sys.argv) == 2:
    	solve(sys.argv[1])
    else:
        print ("please enter your string in one argument in this format: \nexample:\t"
        + bclr.GREEN + "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" + bclr.ENDC)




















