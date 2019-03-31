from algorithms import regex_matcher as re_matcher
from plotter import plot

import utils

def main():
    print "Starting..."
    #runMatchTest()
    menuLoop()

def menuLoop():
    keepRunning = True
    while(keepRunning):
        print "Please make a selection:"
        print "\t1) Manually input a reg-ex and string to be matched"
        print "\t2) Run test suite of strings and infixes"
        print "\t9) Load strings and infixes from sample files"
        print  "\tq)uit"
        selection = raw_input('Please choose: ')

        if(selection == '1'):
            print "You selected 1"

        elif(selection == '2'):
            print "You selected 2"
            infixes = ["1.0.1*", "a.((b.c)|b)*", "a.(b.b)*.c"]
            strings = ["", "101", "abbc", "abcc", "abad", "abbbc"]
            results = matchMany(infixes, strings)
            displayResults(results)
            plotResults(results)

        elif(selection == '8'):
            print "You selected 8"
            plotter.testPlot()

        elif(selection == '9'):
            print "You selected 9"
            testFileReader()

        elif(selection == 'q'):
            keepRunning = False

        else:
            print "Invalid Selection, please try again"

def testFileReader():
    infixes = utils.fr.readLinesToList("infixes.txt")
    strings = utils.fr.readLinesToList("strings.txt")

    results = matchMany(infixes, strings)
    #displayResults(results)
    plotResults(results)

def runMatchOneTest():
    infix = "(a.(b|d))*"
    stringToMatch = "abc"
    print re_matcher.match(infix, stringToMatch), infix, stringToMatch

    
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

def saveResultsToCsv(results_list):
    utils.fr.writeToCsv(result_list)

def plotResults(result_list):
    for r in result_list:
        plot(r.thompsonsConstruction)

def displayResults(result_list):
    """Displays a list of results to the console"""
    for r in result_list:
        r.printResult()

if __name__ == "__main__":
    main()
