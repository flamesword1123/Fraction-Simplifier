from math import sqrt
from math import ceil


def getFactors(origNum):
	factors = []
	for i in range(1,origNum+1):
		if origNum%i == 0:
			factors.append(i)
	return factors

numerator = int(raw_input("Enter your numerator\n"))
denominator = int(raw_input("Enter your denominator\n"))

numeratorFactors = getFactors(numerator)
denominatorFactors = getFactors(denominator)

print "The factors of the numerator are: "
print numeratorFactors
print
print "The factors of the denominator are: "
print denominatorFactors

for numOne in numeratorFactors:
	for numTwo in denominatorFactors:
		if numOne == numTwo:
			GCF = numOne

print GCF

numerator = numerator/GCF
denominator = denominator/GCF

print "The simplified fraction is:"
print numerator
print "----"
print denominator
