print ("if you want to quit, press '0' ")
while True:
  go_on=True
  num=input("Please enter an integer number: ")
  if not num.isdecimal():
    print("This is not an integer number, enter an integer number!")
    go_on=False
  if go_on!=False:
    output= {
     1:  f"{int(num)} is a prime number" ,
     2:  f"{int(num)} is NOT a prime number"
    }
    total=0
    for i in range(2, int(num)+1):
     if int(num)%i==0:
      total+=1
    if total==1:
      print(output[1])
    elif int(num)==0:
      break
    else:
      print(output[2])