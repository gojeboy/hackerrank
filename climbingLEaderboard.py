everyone =[100, 100, 50, 40, 40, 20, 10]
alice =[5, 25, 50, 120]



def getPosision(score, all_score):

    all_score.append(score)

    all_score.sort(reverse=True)

    postions=[1]




    for i in range(1,len(all_score)-2):
        if all_score[i] == all_score[i-1]:
            postions.append(postions[i])

    return postions

positions = getPosision(3, everyone)

print(positions)

