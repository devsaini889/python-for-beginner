# A simple program to multiply two martrix

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[1,2,3,1],
     [4,5,6,1],
     [7,8,9,1]]

result =[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]+= a[i][k] * b[k][j]


for results in result:
    print(results)

