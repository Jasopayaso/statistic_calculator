import math
import numpy as np
from matplotlib import pyplot as plt


class Frequency():
    """conducts multiple operations regarding frequency such as relative frequency, class width, histograms"""

    def __init__(self):
        """initialization of the frequency class"""
        #getting the smallest and largest value
        smallestValue = float(input('What is the smallest value: '))
        largestValue = float(input('What is the largest value: '))

        amountOfValues = int(input('How many data points do you have? :'))
        temp = 0
        dataPointList = []
        while True:
            groupedCheck = input('Is the data grouped (y/n): ')
            if groupedCheck not in ('y', 'n'):
                print('Please select y or n')
            else:
                break
        
        while temp < amountOfValues:
            value = input("Enter your data point: ")
            dataPointList.append(value)
            temp += 1

       

        if groupedCheck == 'n':
            self.indvData()
        rFrequencyCheck = input('Do you want to calculate relative frequency (y/n): ')



        #checks if the user wants to see a visual of the data
        histogramCheck = input('Do you want to see a histogram (y/n): ')
        


    def relativeFrequency(self):
        pass

    def indvData(self):
        valueCount = int(input('How many values do you have: '))

        freqDict = {}

        for _ in range(valueCount):
            value = input('What is your value (one value): ' )
            freq = input(f"What is {value}'s frequency: ")
            tempDict = {value: freq}
            freqDict.update(tempDict)

        print(freqDict[0][1])

def main():
    Frequency()

if __name__ == '__main__':
    main()

