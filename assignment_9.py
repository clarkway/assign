text=input("write a sentence : ")
nmbrs={}
for i in text:
  if i in nmbrs:
    nmbrs[i]=nmbrs[i]+1
  else:
    nmbrs[i]=1
print(nmbrs)
