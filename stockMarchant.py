arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9


def stockMarchant(m, ar):
    # ar.sort()
    matches = {}
    total_pairs = 0

    non_pairs = []

    for a in ar:

        if str(a) in matches:
            # current_count = matches.get(str(a))
            matches[str(a)] += 1

        else:

            matches.update({str(a): 1})

        print(matches)

    for match in matches:
        total_pairs += matches[match] // 2


    for m in matches:
        if matches[m] % 2 == 1:
            non_pairs.append(m)


    print(non_pairs)

    return total_pairs


total = stockMarchant(n, arr)

print(arr)

print(total)
