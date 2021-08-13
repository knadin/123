

import os

base_folder = '/Users/Administrator/Desktop/BlockCountReports/'
year        = 2021
month       = 7 

file_tag = '.txt'

if __name__ == '__main__':
    search_folder = base_folder + f"{year:04}/{month:02}/"
    print(f"Searching in {search_folder}")

    listofFiles = list()
    for subdir, dirs, files in os.walk(search_folder):
        for filepath in files:
            #if filepath.endswith(file_tag):
            print(filepath)