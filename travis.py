import json
import sys


def set_date(string):
    date_year = string[0:4]
    date_month = string[5:7]
    date_day = string[8:10]
    return date_day + '/' + date_month + '/' + date_year


def import_file(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data


def set_row(date, value):
    return date + ";" + value + ";\n"


json_data = import_file(sys.argv[1])
builds = json_data['builds']


csv_file = open(sys.argv[2], 'w')
header = 'date;state;\n'
csv_file.write(header)

for build in builds:
    date_build = build['started_at']
    date = set_date(date_build)
    state = build['state']
    if (state == "passed"):
        csv_file.write(set_row(date, "1"))
    else:
        csv_file.write(set_row(date, "0"))

csv_file.close()
