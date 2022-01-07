import math
def findE(n):
    E = math.e #2.718281828459045
    stringE = str(E)
    if n>15:
        return "max limit of decimals is 15"
    elif n<=0:
        return "2"
    else:
        return stringE[:n+2]

print('enter the value of decimal number to know E value: ')
n = int(input())
o = findE(n)
print(o)
