import fun
n1=int(input("enter number1: "))
while True:
    op = input()
    if op == "=" :
          print("calculation is close:",n1)
          break
    
    n2=int(input("enter numer2: "))

    if  op == "+" :
         n1 = fun.add(n1, n2)
    elif op == "-" :
         n1 = fun.sub(n1, n2)
    elif op == "*" :
         n1 = fun.mul(n1, n2)
    elif op == "/" :
         n1 = fun.div(n1, n2)
    elif op == "%" :
         n1 = fun.mod (n1, n2)
    elif op == "**" :
         n1 ==fun.pow(n1,n2)       
    else:
         print("enter vaild operator")
    print(n1)