import math
import stats_calculator
from binomial import BinomialCalc
from counting import CountingOutcomes
import sys


class StartUp(BinomialCalc, CountingOutcomes):

    def  __init__ (self):
        subjectList = ['binomial', 'counting']
        

        while True:
            self.subject = input("Hello, welcome to the stats calculator. What topic are you looking for? (binomial, counting): ")
            if self.subject not in subjectList:
                print('Please select an available topic')
            else:
                 break

        if 'binomial' in self.subject:
            BinomialCalc.__init__(self)

        if 'counting' in self.subject:
            CountingOutcomes.__init__(self)
        

        while True:
            quitProgram = input('Would you like to quit (y/n): ')
            if quitProgram == 'y':
                sys.exit()
            else: 
                 main()
        
        
def main():
     StartUp()


if __name__ == '__main__':
    main()
    


