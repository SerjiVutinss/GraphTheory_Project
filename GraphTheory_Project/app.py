from algorithms import regex_matcher as re_matcher
import plotter

import utils

def main():
    print "Starting..."
    #runMatchTest()
    appLoop()

def appLoop():
    keepRunning = True
    while(keepRunning):
        print "Please make a selection:"
        print "\t1) Manually input a reg-ex and string to be matched"
        print "\t2) Run test suite of strings and infixes"
        print  "\tq)uit"
        selection = raw_input('Please choose: ')

        if(selection == '1'):
            print "You selected 1"

        elif(selection == '2'):
            print "You selected 2"
            infixes = ["1.0.1*", "a.((b.c)|b)*", "a.(b.b)*.c"]
            strings = ["", "101", "abbc", "abcc", "abad", "abbbc"]
            runMatchAllTest(infixes, strings)

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

    runMatchAllTest(infixes, strings)

def runMatchOneTest():
    infix = "(a.(b|d))*"
    stringToMatch = "abc"
    print re_matcher.match(infix, stringToMatch), infix, stringToMatch

    
def runMatchAllTest(infix_list, string_list):

    #strings = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]

    result_list = list()
    for i in infix_list:
        for s in string_list:
            # NOTE: match() returns an array of the form
            # [string, infix, accepted, postfix]
            r = re_matcher.match(i, s)

            result_list.append(r)

    for r in result_list:
        printResult(r)
    utils.fr.writeToCsv(result_list)

def printResult(r):
    if(r[0] == ""):
        r[0] = "Empty"
    print r[0] + " in " + r[1] + " = " + str(r[2]) + " (postfix = " + r[3] + ")"

if __name__ == "__main__":
    main()
