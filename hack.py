s="baab"
#you can use input fuction insted
s=[s[i] for i in range(len(s))]
i=1
sr=''
while i<len(s):
    print(len(s))
    if s[i-1]== s[i]:
        s.pop(i)
        s.pop(i-1)
        i=0
        continue
    i+=1
if s==[]:
    print("Empty")
else:
    for i in range(len(s)):
        sr+=s[i]
print(sr)
