"""
This is script to read from command line and store into files
"""
import sys
import time

contents = []
while True:
    line = input()
    if line == "EXIT":
        sys.exit()
    elif line == "SORT":
        contents.sort()
        for content in contents:
            c = content.split()
            with open('file_first.txt', "a") as file:
                file.write(c[4] +',' + c[2] + c[0] + c[1].strip(',') + '\n')
            with open('file_second.txt', "a") as file:
                file.write(str(int(c[2].strip(','))/int(c[3].strip(','))*12) + ',' + c[4] + '\n')
            with open('file_third.txt', "a") as file:
                file.write(content + '\n')
        time.sleep(5)
        contents = []
    else:
        contents.append(line)