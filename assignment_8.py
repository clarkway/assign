leap=int(input("write a year :"))

if leap%100==0:
  if leap%400==0 and leap%4==0:
    print(leap, " is a leap year")
  else:
    print(leap, " is NOT a leap year")
else:
  if leap%4==0:
    print(leap, " is a leap year")
  else:
    print(leap, " is NOT a leap year")

