'''********************************************************************************
* 
* Imports for mill_report.py
*
********************************************************************************'''
import os
import glob
import csv
import sys
import math
import time

from pprint import pprint
from datetime import date

'''********************************************************************************
* 
* Global Variables
*
********************************************************************************'''
base_folder = '\\Users\\Administrator\\Desktop\\BlockCountReports\\'
base_tag = '.txt'
file_list = []
month_list = []

'''********************************************************************************
* 
* Global Functions
*
********************************************************************************'''

def file_load(base_folder):
	year = []
	month = []
	file_list = []

	print('\nSelect a number:\n')
	user_input = input('1. ALL REPORTS(ALL)\n2. YEARLY REPORTS(Y)\n3. MONTHLY REPORTS(M)\n')

	if user_input == '1':
		print('You selected ALL')
		print(f'Searching in {base_folder}...')
		file_list = glob.glob(base_folder+f"/**/*{base_tag}",recursive=True)
		#print('files: ', files)

	elif user_input == '2':
		print('You selected year')
		user_input = input('Enter a Year(YYYY): ')
		year = user_input
		search_folder = base_folder + f'{year:4}\\'
		print(f'Searching in {search_folder}...')
		
		file_list = glob.glob(search_folder+f"/**/*{base_tag}",recursive=True)
		#print('files:\n ', file_list)
	
	elif user_input == '3':
		print('You selected month')
		user_input = input('Enter a Year(YYYY): ')
		year = user_input
		user_input = input('Enter a Month(MM): ')
		month = user_input
		search_folder = base_folder + f'{year:4}\\{month:2}\\'
		print(f'Searching in {search_folder}...')
		file_list = glob.glob(search_folder+f"/**/*{base_tag}",recursive=True)
	return year,month,file_list


def report_dates(file_list, year, month):
	file_list.sort()
	#print(file_list)
	print(157*'*')
	today = date.today()
	print('\nSierra Pacific Industries\nCurrent Date:', today)
	start_date = file_list[0]
	end_date = file_list[-1]
	#print(start_date, end_date)
	start_date_total = start_date.split('_')
	end_date_total = end_date.split('_')
	start_date_day = list(start_date_total[0])
	end_date_day = list(end_date_total[0])
	print('Dates included in report:', start_date_day[-8]+start_date_day[-7]+start_date_day[-6]+start_date_day[-5]+'-'+\
		start_date_day[-4]+start_date_day[-3]+'-'+start_date_day[-2]+start_date_day[-1],'to',\
		end_date_day[-8]+end_date_day[-7]+end_date_day[-6]+end_date_day[-5]+'-'+end_date_day[-4]+end_date_day[-3]+'-'+\
		end_date_day[-2]+end_date_day[-1])


def count_getter(file_list, keyword):
	total_keyword_count = 0
	#print(f'\n*****{keyword.upper()}*****')
	for f in file_list:
		file_name = os.path.basename(f)
		#print(file_name)
		with open(f,'r+') as txtfile:
			for line in txtfile:
				if  keyword.lower() in line.lower():
					count_line = line
					words = count_line.split('=')
					keyword_count = float(words[-1])
					total_keyword_count += keyword_count
					'''if 'Day' in file_name:
						print(file_name, '---', keyword_count)
					elif 'Swing' in file_name:
						print(file_name, '-', keyword_count)'''							
	return total_keyword_count

def file_print(file_list):
	total_keyword_count = 0
	for f in file_list:
		for file_list in month_list:
			file_name = os.path.basename(f)
			#print(file_list[-1])
		print(f)

def main():

	year,month,file_list = file_load(base_folder)
	report_dates(file_list, year, month)
	#file_print(file_list)

	list_keywords = [\
					'stem count','block count ','0 block counts','1 block counts', '2 block counts','3 block counts',\
					'reduced length stem solution','no solution count', 'pass-thru to out-feed count' \
					]

	list_total_counts = [0 for _ in list_keywords]
	for index, keyword in enumerate(list_keywords):
		total_count = count_getter(file_list,keyword)
		list_total_counts[index] += total_count

	print('\n'+74*'*')

	for index, keyword in enumerate(list_keywords):
		print(f'TOTAL {keyword.upper()}: {list_total_counts[index]}')



'''********************************************************************************
* 
* Main Loop
*
********************************************************************************'''
if __name__ == '__main__':
	main()