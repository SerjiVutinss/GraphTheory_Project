import csv

def readLinesToList(file_name):

    file = open(file_name, "r")
    line_list = list()
    for s in file.readlines():
        line_list.append(s.strip())
    return line_list

def writeToCsv(result_list, file_name):

    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        for r in result_list:
            writer.writerow([r.string, r.infix, r.isAccepted, r.postfix])
