factors = []

from math import sqrt
from math import ceil


def getFactors(origNum):

	for i in range(2,origNum):
		if origNum%i == 0:
			factors.append(i)
	return factors

numerator = int(raw_input("Enter your numerator\n"))
denominator = int(raw_input("Enter your denominator\n"))

numeratorFactors = getFactors(numerator)
factors = []
denominatorFactors = getFactors(denominator)

print "The factors of the numerator are: "
print numeratorFactors
print
print "The factors of the denominator are: "
print denominatorFactors

print "Program has completed"
