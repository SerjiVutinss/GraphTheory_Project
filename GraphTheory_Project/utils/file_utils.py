import csv

def readLinesToList(file_name):

    file = open(file_name, "r")
    line_list = list()
    for s in file.readlines():
        line_list.append(s)

def writeToCsv(result_list):

    with open('results.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        for r in result_list:
            writer.writerow(result_list[0], result_list[1], result_list[2])

