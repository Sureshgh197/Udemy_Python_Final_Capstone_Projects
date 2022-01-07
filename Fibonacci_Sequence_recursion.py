def generateFibonacciReccursion(n):
    a=0
    b=1
    if(n==0):
        return a
    elif(n==1):
        return b
    else:
        return generateFibonacciReccursion(n-1)+generateFibonacciReccursion(n-2)
print('enter number of fibonacci terms need to generate')
n=int(input())
for i in range(n):
    print(generateFibonacciReccursion(i))
