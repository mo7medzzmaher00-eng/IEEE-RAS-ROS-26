def sets_common(set1,set2):
    result = set()
    for common in set1:
        if common in set2:
            result.add(common)

    return result

a= input("enter set1:")
b= input("enter set2:")
print(sets_common(a,b))


## def sets_common(set1,set2):
#     return set1 & set2
