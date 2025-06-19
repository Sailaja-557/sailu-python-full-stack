# question explanation...
# value dict format lo evvali next dict disply chestham ..next manam echina oka character esthe aa latter ki sambandhinchina details print avvali
# sailu
# 23
# rukku
# 46
# ram
# 8
# baby
# 43
# [{'name': 'sailu', 'id': 23}, {'name': 'rukku', 'id': 46}, {'name': 'ram', 'id': 8}, {'name': 'baby', 'id': 43}]
# r
# {'name': 'rukku', 'id': 46}
# {'name': 'ram', 'id': 8}

n=int(input())
list=[]
for i in range(n):
    user_dict= {}
    user_dict["name"] = input()
    user_dict["id"] = int(input())
    list.append(user_dict)
print(list)
keyword= input()
for j in list:
    if keyword.lower() in j['name'].lower():
        print(j)