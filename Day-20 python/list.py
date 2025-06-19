#ques...ram sam da dum ee hui
# ['ram', 'sam', 'da', 'dum', 'ee', 'hui']
# m
# ['ram', 'sam', 'dum']

lt=input().split(" ")
print(lt)
keyword=input()
list=[]                      #captial or small letters are different
for i in lt:
    if keyword in i:
        list.append(i)
print(list)

# #................
# lt=input().split(" ")
# print(lt)
# keyword=input()      
# list=[]
# for i in lt:
#     if keyword.lower() in i.lower():      #captial or small letters are same
#         list.append(i)  
# print(list)