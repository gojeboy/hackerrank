# msg =input("Please enter your msg: ")

# print(msg)
#Questiion 2
def reverceString(input):
    strList = input.split(' ')
    print(strList)
    strList.reverse()

    rervesed = ' '.join(strList)
    return rervesed


# print(reverceString(msg))

#Question 3
def someOf3and5multiple(maxRange):
    numbers = range(maxRange)
    # print(numbers)

    sum = 0

    for number in numbers:

        if number % 3 == 0 or number % 5 == 0:
            sum += number

    return sum


# print(someOf3and5multiple(1000))


def isPrime(number):
    isPrime = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                isPrime=False
                break
    else:
        isPrime =False

    return  isPrime


# print(isPrime(73939133))

#Question 4
def getTheNthPrime(n):
    primeNumbers =[]
    count =0

    while(len(primeNumbers) < n):
        if(isPrime(count)):
            primeNumbers.append(count)

        count +=1

    return primeNumbers[n-1]

# print(getTheNthPrime(10001))

#Question 5
def fibonacciUnder4Million():
    fibSeq = [1,2]

    max =4000000
    sumOfEven=2

    while(fibSeq[len(fibSeq) -1] < max):
        prev = fibSeq[len(fibSeq) -1]
        prev2 = fibSeq[len(fibSeq) -2]
        new = prev+prev2

        if new % 2 == 0:
            sumOfEven += new

        fibSeq.append(new)

    return sumOfEven

print(fibonacciUnder4Million())