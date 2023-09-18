from counting import CountingOutcomes
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as stats
class BinomialCalc():
     
    def __init__(self):
        #runs the binomial attributes function that asks the user for the inputs
        binomialQuestions = self.binomial_attributes()
        #runs the binomial distribution function and returns the output
        binomialAnswers = self.binomial_distribution(binomialQuestions[0], binomialQuestions [1], binomialQuestions[2], iterationCheck= self.iterationCheck)
        print(
            f'The binomial mean is {binomialAnswers[0]} \n'
            f'The standard deviation is {binomialAnswers[1]}\n'
            f'The binomial probability of x {self.iterationCheck} {binomialQuestions[2]} is {binomialAnswers[2]}'
            )  
        #while True:
            #plotQuestion = input('Would you like to see a visual represenation? (y/n): ')
            #if plotQuestion not in ('y', 'n'):
                #print('Please select y or n')
            #elif plotQuestion == 'y':
                #plt.style.use('ggplot')
                #mean = 0
                #std = 1
                #x = np.linspace(mean - 3 *std, mean + 3*std, 1000)
                #prob = stats.norm(mean, std)
                #plt.plot(x,prob.pdf(x), 'b')

                #px = np.arange(-3, 0, .01)
                #plt.fill_between(px, prob.pdf(px), color = 'r')
                #plt.show()
            #else:
                #break
                
    #if the user wants to use the counting calculator
    

    def binomial_attributes(self):
        #asking the users for the values
        successProbability = float(input('What is the success probability of the binomial distribution (input in decimal form):'))
        fixedTrials = int(input('What is the numbers of fixed trials: '))

        #user validation to see if iteration is needed for the binomial probability
        while True:
            self.iterationCheck = str(input('Select one of the following for your binomial distrubution (< , <= , = , >= , >): '))
            if self.iterationCheck not in ('<', '<=', '=', '>=', '>'):
                print('Please select an available option')
            else:
                break

        numberOfSuccess = int(input('What is the number of successes you want to compute: '))

        #returns the outputs in a tuple
        return successProbability, fixedTrials, numberOfSuccess

    def binomial_distribution(self, successProbability, fixedTrials, numberOfSuccess, iterationCheck):
        
        zeroValue = 0
        binomialProbability = 0

        #initialize the permutationCheck to be 'n' to run the combination formula
        permutationCheck = 'n'
       
        #binomial distribution calculations

        binomialMean = float(fixedTrials * successProbability)
        binomialStandardDeviation = float(math.sqrt(binomialMean * (1 - successProbability)))

        if iterationCheck == '<':
            #binomial probability for everything less than the number of successes
            while zeroValue < numberOfSuccess:
                binomialProbability += CountingOutcomes.counting_techniques(self, fixedTrials, zeroValue, permutationCheck) * (successProbability ** \
                                                                                                    (zeroValue)) * ((1 - successProbability) ** (fixedTrials - zeroValue))
                zeroValue += 1
        
        elif iterationCheck == '<=':
            #binomial probability for everything less than or equal to the number of successes
            while zeroValue <= numberOfSuccess:
                binomialProbability += CountingOutcomes.counting_techniques(self, fixedTrials, zeroValue, permutationCheck) * (successProbability ** \
                                                                                                    (zeroValue)) * ((1 - successProbability) ** (fixedTrials - zeroValue))
                zeroValue += 1

        elif iterationCheck == '=':
            binomialProbability = CountingOutcomes.counting_techniques(self, fixedTrials, numberOfSuccess, permutationCheck) * (successProbability ** \
                                                                                                    (numberOfSuccess)) * ((1 - successProbability) ** (fixedTrials - numberOfSuccess))
            
        elif iterationCheck == '>=':
            while zeroValue < numberOfSuccess:
                binomialProbability += CountingOutcomes.counting_techniques(self, fixedTrials, zeroValue, permutationCheck) * (successProbability ** \
                                                                                                    (zeroValue)) * ((1 - successProbability) ** (fixedTrials - zeroValue))
                zeroValue += 1
            
            binomialProbability = 1 - binomialProbability

        elif iterationCheck == '>':
            while zeroValue <= numberOfSuccess:
                binomialProbability += CountingOutcomes.counting_techniques(self, fixedTrials, zeroValue, permutationCheck) * (successProbability ** \
                                                                                                    (zeroValue)) * ((1 - successProbability) ** (fixedTrials - zeroValue))
                zeroValue += 1
            
            binomialProbability = 1 - binomialProbability
        #binomialProbability = CountingOutcomes.counting_techniques(self, fixedTrials, numberOfSuccess, permutationCheck) * (successProbability ** \
                                                                                                    #(numberOfSuccess)) * ((1 - successProbability) ** (fixedTrials - numberOfSuccess))

        #output
        return "%.2f" % binomialMean, "%.2f" % binomialStandardDeviation, "%.3f" % binomialProbability
    
  