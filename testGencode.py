# -*- coding: utf-8 -*-

import csv
from getVeriCode import get_check_code

with open('./data/citycode.csv', newline='') as csvfile:
    codereader = csv.DictReader(csvfile)
    for row in codereader:
        print(row['code'])

ini = 1
ini = str(ini)
ini.zfill(7)
print(ini.zfill(7))

for i in range(10):
    print(i)

fcode = '11010801266042'
ccode = get_check_code(fcode)
code = fcode + ccode
