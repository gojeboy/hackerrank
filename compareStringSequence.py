msg1 = "AA"
msg2="DDAA"


def createAsciSequence(str):

    arr = list(str)
    arrASCI =[]

    for i in arr:

        arrASCI.append(ord(i))


    return arrASCI


def getDiff(arr):


    diffArray= []
    for x in range(1, len(arr)):
        d = arr[x-1] - arr[x]
        diffArray.append(d)


    return diffArray


def checkSequence(a,b):
    asciArray1 = createAsciSequence(a)
    asciArray2 = createAsciSequence(b)

    diff1= getDiff(asciArray1)
    diff2= getDiff(asciArray2)


    return diff1==diff2


isSamePattern =checkSequence(msg1,msg2)

if isSamePattern:
    print("{},{}, has the same pattern".format(msg1,msg2))
else:
    print("{},{}, does not have the same pattern".format(msg1, msg2))