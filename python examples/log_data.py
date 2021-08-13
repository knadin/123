import os
import csv
import sys
import math
import time
import pylab

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#f = open('00007.LSD')
#text = f.read()
#f.close()

left_side = []
right_side = []
side = []
line_value = []
line_number = []
zero = []
zero_count = 0
one = []
one_count = 0
two = []
two_count = 0
three = []
three_count = 0
#row_value = []
#countlines = []
#countslices = []
with open('00006.LSD', 'r+') as txtfile:
	for row in txtfile:
		if 'Side Left' in row:
			left_side.append(row)
			side.append(row)
		elif 'Side Right' in row:
			right_side.append(row)
			side.append(row)
		elif 'Line_' in row:
			line = row.split('=')
			line_value.append(line[-1])
			line_number.append(line[0])
		if 'CountLines' in row:
			row_value = row.split('=')
			countlines_value = row_value[-1]
			print('countlines:',countlines_value)
		if 'CountSlices' in row:
			row_value = row.split('=')
			countslices_value = row_value[-1]
			print('countslices:',countslices_value)
	#print(left_side)
	#print(line_value)
	#print(line_number)

	countlines_value_int = int(countlines_value)
	countslices_value_int = int(countslices_value)

	line_number_array = np.array(line_number)
	#print(line_number_array)
	line_value_array = np.array(line_value)
	#print(line_value_array)

	num1 = 0
	num2 = 0
	num3 = countlines_value_int
	while(num1 < len(side)):
		print(side[num1])
		s = pd.Series(line_value_array, index = line_number_array)
		print(s[num2:num3], '\n')
		num1 = num1 + 1
		num2 = num2 + countlines_value_int
		num3 = num3 + countlines_value_int


	'''int_side = [int(i) for i in side]
	side_value = []
	for element in side:
		side_num = side.split('Slice')
		side_value.append(side_num[-1])
		print(side_value)'''

	side_value = len(side)
	#x = np.linspace(0, 140, len(side))
	#y = np.linspace(0, line_number_array, line_value_array)
	plt.plot(line_value_array, line_number_array, 'sy')
	#plt.plot(line_number_array, side_value, 'sg')
	plt.show()

	#df = pd.dataframe()


	'''for element in line_value:
		if '0' in element:
			zero_count = zero_count+1
			zero.append(element)
		elif '1' in element:
			one_count = one_count+1
			one.append(element)
		elif '2' in element:
			two_count = two_count+1
			two.append(element)
		elif '3' in element:
			three_count = three_count+1
			three.append(element)
	zero_array = np.array(zero)
	one_array = np.array(one)
	two_array = np.array(two)
	three_array = np.array(three)

	number_lines = 0
	num_of_slices = 0
	while(number_lines < countlines_value_int):
		#print(number_lines)
		number_lines = number_lines + 1
	while(num_of_slices < countslices_value_int):
		#print(num_of_slices)
		num_of_slices = num_of_slices + 1

	#print(line_value)
	#print('Zero Count:', zero_count, 'One Count:', one_count, 'Two Count:', two_count, 'Three Count:', three_count)

	#print(left_side)
	#print(right_side)'''
