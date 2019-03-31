from algorithms import regex_matcher as re_matcher
from plotter import plot

import utils

def main():
    print "Starting..."
    menuLoop()

def menuLoop():
    keepRunning = True
    isPlotting = False
    isWriteToFile = False

    infix_file_name = None
    string_file_name = None
    output_file_name = None

    # run the menu
    while(keepRunning):
        print ""
        print "------------------------"
        print "Plotting: " + str(isPlotting)
        print "Write to file: " + str(isWriteToFile)
        print "------------------------"

        print "Please make a selection:"
        print "\t1) Manually input a reg-ex and string to be matched"
        print "\t2) Specify a file containing infixes and a file containing strings"
        print "\t3) Run test suite of strings and infixes"
        print "Options:"
        print "\tp) Toggle plot graph for each result"
        print "\tw) Toggle write to CSV file for result set"
        print  "\tq)uit\n"
        selection = raw_input('Please choose: ')

        print ""
        if(selection == '1'):
            print "You selected 1 - manually input regex and string"
            infix = raw_input("Please enter the infix regex: ")
            string = raw_input("Please enter the string to match: ")
            print "\nResult"
            if len(infix) == 0:
                print "Infix cannot be empty!"
            else:
                if len(string) == 0:
                    string = ""
                results = matchMany([infix], [string])
                processResults(results, isPlotting, isWriteToFile, output_file_name)

        elif(selection == '2'):
            print "You selected 2 - Specify a file containing infixes and a file containing strings"
            infix_file_name = raw_input("Please enter Infix file name: ")
            string_file_name = raw_input("Please enter String file name: ")
            
            if(len(infix_file_name) > 0 and len(string_file_name) > 0):
                infixes = utils.fr.readLinesToList(infix_file_name)
                strings = utils.fr.readLinesToList(string_file_name)

                results = matchMany(infixes, strings)
                processResults(results, isPlotting, isWriteToFile, output_file_name)
            else:
                print "Neither Infix filename nor String filename can be empty!"

        elif(selection == '3'):
            print "You selected 3"
            infixes = ["a*", "a.b.c*", "a.((b.c)|b)*", "a.(b.b)*.c"]
            strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]
            results = matchMany(infixes, strings)
            processResults(results, isPlotting, isWriteToFile, output_file_name)


        # Options

        ## toggle plotting chart
        elif(selection == 'p'):
            print "You selected 'p' - toggle Plotting"
            isPlotting = not isPlotting
            print "Write To File = " + str(isPlotting)

        ## toggle writing to file
        elif(selection == 'w'):
            print "You selected 'w' - output to csv file"
            isWriteToFile = not isWriteToFile
            if(isWriteToFile):
                output_file_name = raw_input('Please enter the output file name: ')
                if len(output_file_name) != 0:
                    print "New output file: " + output_file_name
                else:
                    print "Output file name cannot be empty!"
                    # disable writing to CSV since output filename was empty
                    isWriteToFile = not isWriteToFile
            else:
                output_file_name = None
            print "Write To File = " + str(isWriteToFile)

        # quit application
        elif(selection == 'q'):
            keepRunning = False

        else:
            print "Invalid Selection, please try again"
    
def matchMany(infix_list, string_list):
    """Generate Results for a list of strings against a list of infixes"""
    result_list = list()
    # process all infixes and strings then add to list
    for i in infix_list:
        for s in string_list:
            # NOTE: returns a result object
            r = re_matcher.match(i, s)
            result_list.append(r)
    return result_list

def processResults(result_list, isPlotting, isWriteToFile, output_file_name):
    """Decide what to do with the results based on the menu options toggled"""
    displayResults(result_list)
    if(isPlotting):
        plotResults(result_list)
    if(isWriteToFile):
        saveResultsToCsv(result_list, output_file_name)

def saveResultsToCsv(result_list, output_file_name):
    """Output the results to a CSV file"""
    utils.fr.writeToCsv(result_list, output_file_name)

def plotResults(result_list):
    """Creates a chart for each result"""
    for r in result_list:
        plot(r.thompsonsConstruction)

def displayResults(result_list):
    """Displays each result to the console"""
    for r in result_list:
        r.printResult()

# call main
if __name__ == "__main__":
    main()