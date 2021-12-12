#!/usr/bin/python

"""
File: main.py
Description: Program to find prime Numbers using Sieve of Eratosthese
"""


class Sieve():

    """Program's Main Class. """

    def __init__(self):
        """ Initial Method. """
        n = int(input("Enter a Number to get Prime numbers below it: "))
        self.arrayOfPrime = self.generatePrime(n)
        i = 0
        while(i < len(self.arrayOfPrime)):
            if self.arrayOfPrime[i]:
                print(i)
            i += 1

    def generatePrime(self, n):
        """ Class Method to Generate Boolean Array of based on User input."""
        primeNumbers = [None]*n

        count = 2
        while(count < len(primeNumbers)):
            primeNumbers[count] = True
            count += 1

        # Creating a List of Numbers below n
        multiplier = 2
        multiple = None

        while(multiplier * multiplier <= n):

            if primeNumbers[multiplier]:
                multiple = multiplier * multiplier

                while multiple < n:
                    primeNumbers[multiple] = False
                    multiple += multiplier

            multiplier += 1

        return primeNumbers


if __name__ == "__main__":
    program = Sieve()
