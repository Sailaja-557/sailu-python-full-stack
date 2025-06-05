try:
    n1 = int(input())
    n2 = int(input())
    res = n1/n2
    print(f"result is :{res}")
except Exception as error:
    print(f"error is happend {error}")
else:
    print("no error")
finally:
    print("program is done")