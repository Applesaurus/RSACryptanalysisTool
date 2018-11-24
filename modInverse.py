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
