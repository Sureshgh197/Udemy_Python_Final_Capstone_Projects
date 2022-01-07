import math
def findPI(n):
    PI = math.pi #3.141592653589793
    stringPI = str(PI)
    if n>15:
        return "max limit of decimals is 15"
    elif n<=0:
        return "3"
    else:
        return stringPI[:n+2]

print('enter the value of decimal number to know PI value: ')
n = int(input())
o = findPI(n)
print(o)





