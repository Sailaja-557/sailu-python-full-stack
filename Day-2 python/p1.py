a = int(input("enter a number1:"))
op = input("enter operator:")
b = int(input("enter a number2:"))
if op == "+" :
    print( a + b  )
elif op == "-" :
    print( a - b )
elif op == "*" :
    print( a * b )
elif op == "/" :
    print( a / b )
else:
    print("enter only integers")