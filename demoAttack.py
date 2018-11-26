from math import gcd

## Written by Michael Harrison
##
## This file contains a simple decryption algorithm,
## as well as support functions.


## demo implements one of the simplest algorithms in Hinek's text:
## In the special case of a public key exponent of 3,
## if we know that two unencrypted messages have a linear relation,
## then we can find one of the messages by plugging into a formula of the form
## P * Q^(-1) mod N, where Q^(-1) is that value such that
## Q^(-1) * Q = 1 mod N.
## If Q happens to not invertible mod N, then gcd(Q, N) is a factor of N,
## and the encryption can be completely cracked.
## @input cypherOne, cypherTwo

def demo(cypherOne, cypherTwo):
    testViable = input("Is there a known linear relationship between your plaintext messages? ")
    if(testViable[0] == 'y' or testViable[0] == 'Y'):
        linCoeff = int(input("Input linear coefficient: "))
        linAffine = int(input("Input constant term: "))
        rsaModulus = getMod()
        modDenom = linCoeff*(cypherTwo - (linCoeff**3) * cypherOne + 2*(linAffine**3))
        commonFactor = gcd(modDenom, rsaModulus%modDenom)
        if(commonFactor != 1):
            print("The modulus has been factored: ")
            print("%d = %d * %d" % (rsaModulus, commonFactor, rsaModulus // commonFactor))
        else:
            modDenomInverse, _ = inversionGCD(modDenom, rsaModulus)
            integerOne = cypherTwo + 2 * (linCoeff**3)*cypherOne - linAffine**3
            integerOne = (integerOne * linAffine * modDenomInverse) % rsaModulus
            integerTwo = linCoeff * integerOne + linAffine
            print("First message: %s; Second message: %s" % (intToString(integerOne), intToString(integerTwo)))

## getMod provides the RSA modulus being used for the encryption under attack.
## The particular value used here is RSA-100
def getMod():
    return 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139

## stringToInt takes a character string
## and returns an integer in an invertible way.
## It is this integer that is encrypted with the RSA algorithm.
## @input inputString
## @output a decimal concatenation of the integer values
##         of the characters of inputString
def stringToInt(inputString):
    digitList = ''
    for i in inputString:
        if ord(i) < 100:
            digitList = digitList+('0'+str(ord(i)))
        else:
            digitList = digitList+(str(ord(i)))
#    digitString = (''.join(c) for c in digitList)
    return int(digitList)

## Given an integer encoding resulting from stringToInt,
## intToString returns the original character string.
## @input inputInt
## @output the string that initially produced inputInt
def intToString(inputInt):
    digitList = []
#    listSize = len(str(inputInt))//3
    while inputInt > 0:
        digitList.insert(0, inputInt%1000)
        inputInt = inputInt//1000
#        print(*digitList)
    return ''.join(chr(i) for i in digitList)

## inversionGCD implements the extended Euclidean Algorithm,
## which along with finding the greatest common factor of two numbers,
## also keeps a record of the computations made at each step.
## @input firstInt, secondInt
## @output integers u and v such that, if firstInt and secondInt
##         are relatively prime, then u * firstInt = 1 mod secondInt
##                                    v * secondInt = 1 mod firstInt
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

    firstInv, secondInv = modInverter(remainder, coeff)
    return firstInv%secondInt, secondInv%firstInt

## modInverter is called by inversionGCD;
## this is where the results of the Euclidean Algorithm
## are actually used to find the multiplicative inverses.
## Technically, this algorithm solves the Diophantine equation
## firstInt * x + secondInt * y = gcd(firstInt, secondInt)
## @input remainder, coeff the remainder and coefficient arrays
##                         obtained from the extended Euclidean Algorithm
## @output values for x and y that solve the above Diophantine equation
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
