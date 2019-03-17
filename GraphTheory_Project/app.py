#from samples_ian import sample_runner
from models import State, Nfa

from algorithms import ThompsonsConstructor

def main():
    print "Starting..."
    #sample_runner.run()
    n =  Nfa(State(), State())
    s = State()

    t = ThompsonsConstructor("aa*")

if __name__ == "__main__":
    main()
