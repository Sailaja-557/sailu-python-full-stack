# s = "hello sandy"
# p = list(s)  # ['h', 'e', 'l', 'l', 'o', ' ', 's', 'a', 'n', 'd', 'y']
# print(p)

# numbers = (1, 2, 3)
# numbers_list = list(numbers)  # [1, 2, 3]
# print(numbers_list)

# data = {"a", "b", "c"}
# data_list = list(data)  # Order not guaranteed: ['a', 'c', 'b']





# a = "cherry"
# b= list(a) # change the datatype string to list 
# print(b)

# l1=[10,20,30,20,50,40]
# l2=[70,90,100,12]
# l1.append(300)
# print(l1)
# l1.remove(20)
# print(l1)
# l2.append(50)
# print(l2)
# l2.remove(90)
# print(l2)

# a = ["apple","girl","cherry"]
# a.append("boy")
# print("after append:",a)
# a.remove("girl")
# print("after remove:",a)
# a.insert(2,"boom")
# print("after insert:",a)
# a.pop()
# print("after pop:",a)
# a.pop(1)
# print("particular value pop:",a)
# a.append([1,2,3])
# print("append list in list:",a)
# a[2].append(50)
# print(a)
# a[2].pop(1)
# print(a)

# Create List of Even Numbers (Using Loop)
# Create a list that stores all even numbers from 1 to 20.
even_number=[]
for i in range(1,21):
    if i%2==0:
        even_number.append(i)
print("even numbers:",even_number)