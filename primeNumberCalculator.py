import time

def prime(x):
    for psbileprime in range(3,x,2):
        isPrime= True
        for num in range(3,psbileprime,2):
            if psbileprime%num==0:
                isPrime=False
        if isPrime:
            print(psbileprime)
    
startt=time.time()
prime(50000)
end=strt=time.time()

print(end-startt)

        




            
