import random

# from numpy.core import half

TheNumbers = list(range(1,1001))

selectedNumber = int(input())

count =1

def findNumber(num, numbers):

    half = len(numbers) // 2
    mid_index = len(numbers)//2

    if num == numbers[mid_index]:
        numbers = [num]

    elif num > numbers[mid_index]:
        numbers = numbers[half:]

    elif num < numbers[mid_index]:
        numbers = numbers[:half]


    if len(numbers)==1:
        return numbers[0]
    else:
        return findNumber(num, numbers)

print("You selected : ", findNumber(selectedNumber, TheNumbers))

