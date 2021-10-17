# create element in matrix
arr = [ [1,2,4,29],
        [3,4,6,19] ]

print(arr)

# create matrix of set size
N = 3
M = 2
A = []
for i in range(N):
    A.append([0]*M)

print(A)

# with generate nums
import random
N = 3
M = 2
A = [[0]*M for i in range(N)]

# fill in with random num
for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(0,20)

print(A)

print("# - - - #")
# output matrix
for row in A:
    for elem in row:
        print(elem, end = ' ')
    print()

print("# - - - #")
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()

# input manualy
A = []
for i in range(3):
    A.append(list(map(int, input().split())))


A = []
for i in range(3):
    row = input().split()

    for i in range(len(row)):
        row[i] - int(row[i])
    A.append(row)


