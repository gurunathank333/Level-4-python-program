print ("Prime number generation")
print(".........................")
sn=int (input("Enter the starting number:"))
en=int (input("Enter the ending number:"))
print("Result")
count=0
for n in range(sn,en):
    for i in range(2,n):
        if(n%i)==0:
            count+=1
if count==0:
      print(n,"prime")
else:
    print(n,"not prime")
