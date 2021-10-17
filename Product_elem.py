# product of elements
def product_elem(a):
    if a == []:
        return 0
    res = 1
    for elem in a:
        res *= elem
    return res

list0 = [5,2,10,35]
print(product_elem(list0))