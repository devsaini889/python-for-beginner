# A Simple program to determine the HCF of the number

def HCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller =x
    
    for i in range(1 , smaller+1):
        if x % i == 0 and y % i ==0 :
            HCF = i
        
    return HCF


print("The value of HCF is:", HCF(12,30))