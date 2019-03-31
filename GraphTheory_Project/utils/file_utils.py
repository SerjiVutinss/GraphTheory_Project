import csv

def readLinesToList(file_name):
    """
        Read a list of strings from a file, removing any whitepace

        @param file_name - file to be read

        @returns line_list - a list of the lines in the file as strings
    """

    file = open(file_name, "r")
    line_list = list()
    for s in file.readlines():
        line_list.append(s.strip())
    return line_list

def writeToCsv(result_list, file_name):
    """
        Write a list of results to a CSV file
    """
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        for r in result_list:
            writer.writerow([r.string, r.infix, r.isAccepted, r.postfix])
