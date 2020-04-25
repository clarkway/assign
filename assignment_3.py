rpt=True
given=input("write an integer number  :")
num=list(given)
if num[0]=="-":
  print ("Please enter a positive number")
flt=True
for i in num:
  if i=="," or i==".":
    print("Please enter an integer number")
    flt=False
    rpt=False
while not given.isdecimal() and flt:
  print("Do not use any entries other than numeric values")
  rpt=False
  break
if rpt==True:
  total=0
  for j in num:
    total+=int(j)**len(num) 
  if int(given)==total:
    print(given, "is an Armstrong number")
  else:
    print(given, "is NOT an Armstrong number")
    print("deneme")
