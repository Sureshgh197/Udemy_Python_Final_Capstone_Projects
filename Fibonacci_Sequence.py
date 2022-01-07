def generateFibonacci(n):
    a=0
    b=1
    if(n<=0):
        print("Please enter a number greater than 0")
    for i in range(n):
        if(i==0):
            print(a,end="   ")
        elif(i==1):
            print(b,end="   ")
        else:
            c = a+b
            print(c,end="   ")
            a,b=b,c

print('enter the value of number to see fibonacci series: ')
n = int(input())

generateFibonacci(n)
