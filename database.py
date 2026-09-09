#imports
import pandas as pd
from consts import *
import csv
import os

def create_new_file():
    """
    func that checks if a file named data.csv exists, if a file doesn't exist it creates it
    :return: none
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
    else:
        pass

create_new_file()