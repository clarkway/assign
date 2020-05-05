n=int(input("Please enter the limit: "))
prime=[]
for j in range(2,n+1):
  total=0
  for i in range(2, j+1):
    if j%i==0:
      total+=1
  if total==1:
    prime.append(j)
print(prime)


