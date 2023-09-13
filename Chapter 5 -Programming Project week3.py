def merge(list1, list2):
    i = 0
    j = 0
    m = len(list1)
    n = len(list2)
    resultList = []
    while(i < m and j < n):
        if(list1[i] <= list1[j]):
            resultList.append(list1[i])
            i += 1
        else:
            resultList.append(list2[j])
            j += 1
    if i < m:
        while i < m:
            resultList.append(list1[i])
            i += 1
    else:
        while j < n:
            resultList.append(list2[j])
            j += 1
    return resultList

list1 = [1, 4, 7, 12, 16, 19]
list2 = [2, 3, 5, 8, 10]
print("list1 : ", list1)
print("list2 : ", list2)
print("after merging sorted list : ", merge(list1, list2))
