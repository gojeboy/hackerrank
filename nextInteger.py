Thenumbers = [1, 3, 10, 4, 1, 2, 5, 12, 59, 3]


def getNextInt(A):
    number_set = set(A)

    numbers = list(number_set)

    numbers.sort()

    nextInt = 0


    if numbers[len(numbers) - 1] <= 0:
        nextInt = 1

    else:
        for i in range(len(numbers) - 1):

            if numbers[i + 1] - numbers[i] > 1:
                nextInt = numbers[i] + 1
                break;

    if nextInt == 0:
        nextInt = numbers[len(numbers) - 1] + 1

    return nextInt


nextInteger = getNextInt(Thenumbers)

print("The next in is :", nextInteger)
