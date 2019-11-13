

def plusMinus(arr):

    n = len(arr)
    positives = list(filter(lambda x: x > 0, arr))

    negatives = list(filter(lambda x: x < 0, arr))

    zeros = list(filter(lambda x: x == 0, arr))


    pos_ratio = len(positives)/n
    neg_ratio = len(negatives)/n
    zero_ratio =len(zeros)/n



    print("{0:.6f}".format(pos_ratio))
    print("{0:.6f}".format(neg_ratio))
    print("{0:.6f}".format(zero_ratio))


ar =[1, 2, 3, -1, -2, -3, 0, 0]

plusMinus(ar)
