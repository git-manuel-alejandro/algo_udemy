array = [1, 2, 3, 4, 5, 6, 7]
missing = [3, 7, 2, 1, 4, 6]


def finder(array, missing):
    missing.sort()

    for i in range(len(array)):
        if array[i] == missing[i]:
            continue
        else:
            print(array[i])
            break


finder(array, missing)
