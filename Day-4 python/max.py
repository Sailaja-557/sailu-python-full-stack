# find the max value in the list
# method 1
# brain=0
# l=[1,2,15,20,90,5]
# for i in range(0,len(l)):
#     if l[i] > brain:
#         brain = l[i]
# print(brain)

# method 2
brain = 0 
l=[1,2,15,20,90,5]
for i in l:
    if brain < i:
        brain = i
print(brain)