# set={1,2,3,4,50,7,6,12,}
# set.add("boom")
# print(set)
# # set.add(21)
# # print("after add:",set) # add the values in unorder like randam way [set perform unorder way]

# set.remove("boom")
# print(set)

# list_1=[1,2,6,7,2,8]
# p=set(list_1)  #typecasting list to set
# print(p)

# ss = {"sailu","sandhya","ramya","sneha","sailu"}  # set remove the duplicate words
# print(ss)

# colors = {'red', 'green', 'blue',}  #discard the particular value
# colors.discard('yellow')  # No error
# print(colors)  # Output: {'red', 'green', 'blue'}

# items = {10, 20, 30}
# item = items.pop()
# print(item)    # Output: (could be 10 or 20 or 30)
# print(items)   # Remaining items

s1={1,2,3,4,5,6,9}
s2={1,2,3,5,89,84}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))  # print only different values in s1 and s2
# s.clear()
# print(s)
