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

for numOne in numeratorFactors:
	for numTwo in denominatorFactors:
		if numOne == numTwo:
			GCF = numOne

numerator = numerator/GCF
denominator = denominator/GCF

print "The simplified fraction is:"

numLength = len(str(numerator))
denomLength = len(str(denominator))

dashes = ""


if numLength == denomLength:
	for i in range(0,numLength):
		dashes = dashes + "-"
elif numLength > denomLength:
	for i in range(0,numLength):
		dashes = dashes + "-"
else:
	for i in range(0,denomLength):
		dashes = dashes + "-"
print

print "    ",
print numerator

print "    ",
print dashes

print "    ",
print denominator

print
