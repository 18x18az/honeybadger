import csv
import os

BASE_DIR = '/home/tm/.wine/drive_c/users/tm/AppData/Roaming/VEX Tournament Manager/'

def readCsv(filename):
    with open(os.path.join(BASE_DIR, filename), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        return list(reader)