# a simple program to tranpose a matrix


# solution 1: using loop 


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b= [[0,0,0],
    [0,0,0],
    [0,0,0]]


for i in range(len(a)):
    for j in range(len(a[0])):

       b[j][i]= a[i][j]

for r in b:

    print(r)



# solution 2 : using list compreansion

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]


b=[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


for r in b:
    print(r)