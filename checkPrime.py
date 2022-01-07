def checkPrime(n):
    flag=0
    if(n>1):
        
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                flag=1
                break
        if(flag==1):
            return False
        else:
            return True       
            
    else:
        return 
 