num=int(input())
i=2
count=0
while(i<=num//2):
    if(num%i==0):
      print(num,"is not prime number") 
    
      break
    i=i+1
    
else:
    print(num,"is a prime number")      
