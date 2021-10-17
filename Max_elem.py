# 1
def max_elem(a):
    max0 = a[0]
    for elem in a:
        if elem > max0:
            max0 = elem

    return max0

list0 = [2,3,4,5,6,7,1,2,3]
result = max_elem(list0)
print("#1 :",result) # return 7

# 2
list1 = [10,12,3,14,20,7,6,5]
list1.sort()
print("#2 :",list1[-1])

# 3
list2 = [3,5,9,7,1,5,8,8,7,5,6]
max_num = max(list2)
print("#3 :", max_num)

#4 
from functools import reduce

list3 = [-5,-6,-7,-99,-67,-3,-4,-9]
print("#4 :",reduce(max, list3))