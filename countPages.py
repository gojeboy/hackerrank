nn = 6
pg = 5

def countPages(n, p):
    distace_from_beg = p //2
    distace_from_end = (n -p)//2

    if n % 2 ==0:

        if p ==n:

            return 0
        elif n == 2:
            return 0
        elif n -p ==1:
            return 1

        else:
            if distace_from_beg < distace_from_end:
                return distace_from_beg
            else:
                return distace_from_end

    else:


        if distace_from_beg < distace_from_end:
            return distace_from_beg
        else:
            return distace_from_end



pgs = countPages(nn,pg)

print(pgs)