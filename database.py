#imports
import pandas as pd

import consts
import game_field
from consts import *
import csv
import os
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
datas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def create_new_file():
    """
    func that checks if a file named data.csv exists, if a file doesn't exist it creates it
    :return: writer
    """
    """with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'branch', 'year', 'cgpa']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        """

    if not os.path.exists(DATA):
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    else:
        pass

def write_to_file(datas, num):
    i = 0
    while i <= 9:
        file = open('data.csv', 'a', newline='')
        writer = csv.writer(file)
        writer.writerows(datas)
        i += 1

if __name__ == '__main__':
    writers = create_new_file()
    write_to_file(datas)

def extract_data(num):
    num = int(num)
    file = open('data.csv', 'r')
    reader = csv.reader(file)
    data = list(reader)
    index = num * consts.BOARD_ROWS
    try:
        soldier_coordinates = [data[index][-1], data[index+1][-1]]
        data = data[index:-1]
    except IndexError: # If there is no saved game in index, then does nothing
        return None
    game_field.change_field(data)
    return soldier_coordinates


# create_new_file()
# extract_data()
