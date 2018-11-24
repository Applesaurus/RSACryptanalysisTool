## Written by Michael Harrison
## November 24, 2018
##
## The functions contained within this file are written
## to solve the Diophantine equation ax + by = g,
## where g is the greatest common factor of a and b.
## In the case g = 1, this provides a means for calculating
## the multiplicative inverse of a, modulo b (and vice-versa).

## inversionGCD implements the Euclidean algorithm on two integers.
## Unlike the gcd function included with most programming languages,
## inversionGCD returns the coefficients and remainders for each step;
## this information is needed by modInverter.
## @input firstInt, secondInt
## @output remainder, coeff
def inversionGCD(firstInt, secondInt):
    if abs(firstInt) == abs(secondInt):
        return [0], [firstInt//secondInt]
    if firstInt * secondInt == 0:
        return [0], [0]
    divisor = firstInt
    quotient = secondInt
    remainder = list()
    coeff = list()
    testValue = divisor%quotient
    remainder.append(testValue)
    coeff.append(divisor//quotient)
    divisor = quotient
    quotient = testValue

    while testValue != 0:
        testValue = divisor%quotient
        remainder.append(testValue)
        coeff.append(divisor//quotient)
        divisor = quotient
        quotient = testValue

#    firstInv, secondInv = modInverter(remainder, coeff)
#    return u%max(firstInt, secondInt), v%min(firstInt, secondInt)
    return remainder, coeff
#    return firstInv%secondInt, secondInv%firstInt

## modInverter uses the arrays from inversionGCD
## to express each value of remainder as a linear combination
## of the inputs to inversionGCD, down to the final remainder,
## which is the greatest common factor of inversionGCD's inputs.
## The remainder array is also used to terminate the algorithm.
## The values from the coeff array are used to determine
## the coefficients for this linear combination.
## @input remainder, coeff
## @output divCoeffNew, quotCoeffNew
def modInverter(remainder, coeff):
    if(remainder[0] == 0):
        return 0, 1

    else:

        divCoeffOld = 1
        divCoeffNew = -coeff[1]
        quotCoeffOld = -coeff[0]
        quotCoeffNew = 1 + coeff[0] * coeff[1]

        counter = 1

        while remainder[counter+1] != 0:
            counter += 1
            temp = divCoeffOld - coeff[counter] * divCoeffNew
            divCoeffOld = divCoeffNew
            divCoeffNew = temp

            temp = quotCoeffOld - coeff[counter] * quotCoeffNew
            quotCoeffOld = quotCoeffNew
            quotCoeffNew = temp

        return divCoeffNew, quotCoeffNew
