from models import State, Nfa
from algorithms import regex_matcher as re_matcher

def main():
    print "Starting..."
    n = Nfa(State(), State())
    s = State()

    infix = "a.a"
    stringToMatch = "aa"

    infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
    strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

    for i in infixes:
        for s in strings:
            print re_matcher.match(i,s),i,s

if __name__ == "__main__":
    main()
