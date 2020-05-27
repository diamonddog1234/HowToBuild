import xlrd
import datetime
from models import House

rb = xlrd.open_workbook('excel1.xls')
sheet = rb.sheet_by_index(0)

addresses = []

for rownum in range(1, sheet.nrows):
    row = sheet.row_values(rownum)
    row_clear = list(filter(None, row))
    if len(row_clear) == 1:
        addresses.append(rownum)

for addr_index in range(0, len(addresses) - 1):
    row_addr = list(filter(None, sheet.row_values(addresses[addr_index])))
    print(row_addr[0]) #адрес дома
    tube = ''
    for rownum in range(addresses[addr_index] + 1, addresses[addr_index + 1] - 1):
        row = sheet.row_values(rownum)
        row_clear = list(filter(None, row))
        if len(row_clear) != 0:
            if row_clear[0]: tube = row_clear[0]
            date = datetime.datetime(*xlrd.xldate_as_tuple(row_clear[1], rb.datemode))
            samples = sheet.row_values(rownum, 2)
            print(tube) #название трубки
            print(date) #дата замера
            print(samples) #массив замеров за одну дату

