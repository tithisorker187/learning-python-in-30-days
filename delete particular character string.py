#delete particular character string
s=input("enter the string")
term=input("enter the character to delete")
result=""
for i in s:
  if i !=term:
    result=result+i
print(result)
