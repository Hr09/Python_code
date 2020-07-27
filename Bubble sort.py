import random as r
num_list=[]
for i in range(5):
    num_list.append(r.randrange(1,9))
i =len(num_list)-1
for k in num_list:
    print(k, end="")
print()

while i>1:
    j=0
    while j<i:
        print(":\n Is {}>{}".format(num_list[j],num_list[j+1]))
        print()
        if num_list[j]>num_list[j+1]:
            print("Switch")
            temp=num_list[j]
            num_list[j]=num_list[j+1]
            num_list[j+1]=temp
        else:
            print("Dont Switch")
        j+=1
        for k in num_list:
            print(k,end="")
        print()
        i-=1
print("Sorted Value is :")
for k in num_list:
    print(k, end="")
print()