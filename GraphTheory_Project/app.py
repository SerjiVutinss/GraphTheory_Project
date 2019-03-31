from algorithms import regex_matcher as re_matcher
import plotter

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
            runMatchAllTest()
        elif(selection == '9'):
            print "You selected 9"
            plotter.testPlot()
        elif(selection == 'q'):
            keepRunning = False
        else:
            print "Invalid Selection, please try again"

def runMatchOneTest():
    infix = "(a.(b|d))*"
    stringToMatch = "abc"
    print re_matcher.match(infix, stringToMatch), infix, stringToMatch

    
def runMatchAllTest():

    #infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
    infixes = ["1.0.1*", "a.((b.c)|b)*", "a.(b.b)*.c"]
    strings = ["", "101", "abbc", "abcc", "abad", "abbbc"]

    for i in infixes:
        for s in strings:
            print re_matcher.match(i,s),i,s


if __name__ == "__main__":
    main()
