name = "sailu"
age = 20
price = 50.99

print(type(name))
print(type(age))            # display the data type
print(type(price))


a = 2
b = 4.25
sum = a + b # python automatically perform typeconvesion    then take values 2.0 + 4.25 
print(sum) # 6.25

p = "2"
k = 4.25       # in this case don't perform typeconversion method
print(type(p))
print(p+k) # display TypeError reason is can't add the string and float value

#Typecasting
d = int("2")
c = 4.25       
print(type(d))
print(d+c)
