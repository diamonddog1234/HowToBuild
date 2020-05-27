import xlrd
import datetime
import re

def parse_house_text(text):
    firstNumberIndex = re.search(r"\d", text).start()
    street = text[0:firstNumberIndex]
    number = text[firstNumberIndex :]
    number = number.replace('-',' корпус ')
    return  'Норильск ' + street + number

rb = xlrd.open_workbook('excel1.xls')
sheet = rb.sheet_by_index(0)

addresses = []

for rownum in range(1, sheet.nrows):
    row = sheet.row_values(rownum)
    row_clear = list(filter(None, row))
    if len(row_clear) == 1:
        addresses.append(rownum)

addresses.append(sheet.nrows)

for addr_index in range(len(addresses) - 1):
    row_addr = list(filter(None, sheet.row_values(addresses[addr_index])))
    print(parse_house_text(row_addr[0])) #адрес дома
    tube = ''
    for rownum in range(addresses[addr_index] + 1, addresses[addr_index + 1]):
        row = sheet.row_values(rownum)
        row_clear = list(filter(None, row))
        if len(row_clear) != 0:
            if row[0]: tube = row[0]
            date = datetime.datetime(*xlrd.xldate_as_tuple(row[1], rb.datemode))
            samples = row[2:]
            #print(tube) #название трубки
            #print(date) #дата замера
            #print(samples) #массив замеров за одну дату