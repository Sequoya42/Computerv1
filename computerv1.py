# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computerv1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rbaum <rbaum@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/08/08 15:49:33 by rbaum             #+#    #+#              #
#    Updated: 2015/08/21 23:29:35 by rbaum            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0

import re
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getmax(y, y2):
	x = 0
	for i in y and y2:
		if i[2] > x:
			x = i[2]
	x = int(x) + 1
	return x

#------------------------#

def parse(str):
	for ch in[' ', '^', '*']:
		if ch in str:
			str = str.replace(ch, '')
	print str
	left = re.findall("(([+|-]?[0-9].?[0-9]*)[Xx]([0-9])*)", str.split(('='))[0])
	right = re.findall("(([+|-]?[0-9].?[0-9]*)X([0-9])*)", str.split(('='))[1]) 
	list = []
	for x in reversed(range(0, getmax(left, right))):
		list += [(float(i[1]), int(i[2])) for i in left if int(i[2]) == x]
		list += [(-float(i[1]), int(i[2])) for i in right if int(i[2]) == x]		
	list = sorted(list, key=lambda tup:tup[1], reverse=True)
	a = b = c = 0
	for i in list:
		if i[1] == 0: a += i[0];
		else if i[1] == 1: b += i[0];
		else if i[1] == 2: c += i[0];
	print list
	print (int(a), int(b), int(c))
# -----------------------------------------#

if __name__ == '__main__':
    if len(sys.argv) == 2:
        parse(sys.argv[1])
    else:
        print ("please enter your string in one argument in this form: \n\t"
        + bcolors.OKGREEN + "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" + bcolors.ENDC)




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
