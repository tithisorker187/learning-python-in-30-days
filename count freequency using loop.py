#count the frequency using loop
s=input("enter the email")
word=input("enter the letter")
counter=0
for i in s:
  if i==word:
    counter+=1
print(counter)
