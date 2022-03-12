def mySearch(lst, cond):
    result = []
    for i in range(0, len(lst)):
        if cond(lst[i]):
            result.append(lst[i])
    return result

def mySort(lst, relation):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if (not relation(lst[i], lst[j])):
                lst[i], lst[j] = lst[j], lst[i]
    return lst
