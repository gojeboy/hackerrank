a = [5,6,7]
b = [3,6,10]


def compareTriplets(a, b):
    a_score =0
    b_score =0

    for x in range(3):

        if (a[x] > b[x]):
            a_score +=1

        elif (a[x] <b[x]):
            b_score +=1



    return [a_score,b_score]





print(compareTriplets(a, b))
