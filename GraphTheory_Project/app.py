from algorithms import regex_matcher as re_matcher

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
            runMatchTest()
        elif(selection == 'q'):
            keepRunning = False
        else:
            print "Invalid Selection, please try again"
    
def runMatchTest():
    infix = "a.a"
    stringToMatch = "aa"

    infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
    strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

    for i in infixes:
        for s in strings:
            print re_matcher.match(i,s),i,s


if __name__ == "__main__":
    main()
