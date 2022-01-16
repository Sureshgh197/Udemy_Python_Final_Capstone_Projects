import re
import sys
# initializing string
ini=0
while True:
    if ini!=0:
        print('Your previous solution is : ',ini)
        
    test_str = input("enter ur expression \n")
     
    
    fn1=re.findall(r'^[\+\-\*\/]\d+',test_str)
    fn2=re.findall(r'^\d+',test_str)
    
    if len(fn1) == 0:
        fn=int(fn2[0])
        fnum=ini+fn
    else:
        fnum=ini
    
    p=re.findall(r'[\+\-\*\/]\d+', test_str)
    
    for i in p:
        if(i[0]=='+'):
            fnum=fnum+int(i[1:])
        elif(i[0]=='-'):
            fnum-=int(i[1:])
        elif(i[0]=='*'):
            fnum*=int(i[1:])
        elif(i[0]=='/'):
            if(int(i[1:])==0):
                print('Devide by Zero not possible')
            else:
                fnum/=int(i[1:])
    print('solu..',fnum)
    ini=fnum
    a=input('Do you want to continue calculation yes/no [y/n]: ')
    if a=='n':
        sys.exit()