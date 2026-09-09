#imports
import pandas as pd

import consts
import game_field
from consts import *
import csv
import os
# data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    data = []
    for i in range(consts.BOARD_ROWS * 9):
        row = []
        for j in range(consts.BOARD_COLS + 1):
            row.append(0)
        data.append(row)

    if not os.path.exists(DATA):
        with open(DATA, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    else:
        pass

def write_to_file(data, soldier_coordinates, num):
    file = open('data.csv', 'r')
    reader = csv.reader(file)
    file_info = list(reader)
    index = (num-1) * consts.BOARD_ROWS

    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            file_info[index + i][j] = data[i][j]

    file_info[index][-1] = soldier_coordinates[0]
    file_info[index + 1][-1] = soldier_coordinates[1]

    with open(DATA, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(file_info)


def extract_data(num):
    file = open('data.csv', 'r')
    reader = csv.reader(file)
    data = list(reader)
    index = (num-1) * consts.BOARD_ROWS
    is_game = False
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if data[i + index][j] != '0':
                is_game = True
                break
        if is_game:
            break

    if is_game:
        soldier_coordinates = [data[index][-1], data[index+1][-1]]
        print(soldier_coordinates)
        data = data[index:index + consts.BOARD_ROWS + 1]
        game_field.change_field(data)
        return soldier_coordinates
    else:
        return None
