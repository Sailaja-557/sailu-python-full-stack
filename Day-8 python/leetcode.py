# s = ["--X","X++","++X"]
# x=0
# for i in range(len(s)):
#     temp = s[i]
#     if temp == "--X":
#         x=x-1
#     if temp == "X--":
#         x=x-1
#     if temp == "++X":
#         x=x+1
#     if temp == "X++":
#         x = x+1
# print(x)

#method-2
# s=["--X","X++","++X"]
# x=0
# for i in range(len(s)):
#     temp=s[i]
#     if temp == "--X" or temp == "X--":
#         x=x-1
#     if temp == "++X" or temp == "X++":
#         x=x+1
# print(x)

#method-3
li = ["--X","X++","++X"]
x=0
for i in li:
    temp=i
    if temp == "--X" or temp == "X--":
        x=x-1
    else:
        x=x+1
print(x)

#method-4
li = ["--X","X++","++X"]
x=0
for i in li:
    if i == "--X" or i == "X--":
        x=x-1
    else:
        x=x+1
print(x)