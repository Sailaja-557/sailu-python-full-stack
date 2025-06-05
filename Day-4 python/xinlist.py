l1=int(input("entr value:"))
list = [2,3,5,7,9,11,14]

for i in range(0,len(list)):
    if list[i] == l1:
        print("found")
        break
else:
    print("not found")
print("done")