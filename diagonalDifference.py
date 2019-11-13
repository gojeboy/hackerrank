arr =[[11,2,4],
      [4,5,6],
      [10,8,-12]]




def diagonalDifference(arr):

    primary_idx =0
    secondary_idx =len(arr)-1

    primary_sum = 0
    secondary_sum = 0

    print(len(arr))

    for x in arr:

        primary_number =x[primary_idx]
        secondary_number =x[secondary_idx]

        primary_sum +=primary_number
        secondary_sum +=secondary_number

        primary_idx +=1
        secondary_idx -=1



    if primary_sum >= secondary_sum:
       return primary_sum - secondary_sum
    else:
       return secondary_sum-primary_sum

print(diagonalDifference(arr))