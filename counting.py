import math


class CountingOutcomes():

    def __init__(self):
        #checking if factorial is needed
        while True:
             factorialCheck = input('Are you selecting a specific amount from a larger sample? (y/n): ')
             if factorialCheck.lower() not in ('y' , 'n'):
                print('Please pick y or n')
             else:
                break
        #factorial of a number
        if factorialCheck == 'n':
            factorialNumber = int(input("What's the number that you want to count from: "))
            print(math.factorial(factorialNumber))
        else:
            #runs the other counting techniques
            countingQuestions = self.counting_attributes()
            countingAnswers = self.counting_techniques(countingQuestions[0], countingQuestions[1], countingQuestions[2])
            print(f'There are {countingAnswers} possible outcomes')

    def counting_attributes(self):
        """Asks the user for the attributes for the current problem"""
        totalObjects = int(input('What is the total amount of objects being counted: '))
        sampleChosen = int(input('What is the amount you want from the total: '))
        while True:
            permutationCheck = input('Does the order matter (y/n): ')
            if permutationCheck.lower() not in ('y' , 'n'):
                print('Please pick y or n')
            else:
                break
        
        return totalObjects, sampleChosen, permutationCheck
    
    def counting_techniques(self, totalObjects , sampleChosen, permutationCheck):
        """Runs the permutations and combinations formula depending on the situation"""

        #the permutation formula 
        def permutation(totalObjects, sampleChosen):
            """the permuation formula used in statistics"""
            permutationsCalculator = math.factorial(totalObjects) / math.factorial(totalObjects - sampleChosen)
            return permutationsCalculator
        
        #the combination formula   
        def combination(totalObjects, sampleChosen):
            """the combination formula used in statistics"""
            combinationsCalculator = permutation(totalObjects, sampleChosen) / math.factorial(sampleChosen)
            return combinationsCalculator
        
        if permutationCheck == 'y':
            return permutation(totalObjects, sampleChosen)
        elif permutationCheck == 'n':
            return combination(totalObjects, sampleChosen)

        return totalObjects , sampleChosen, permutationCheck

    