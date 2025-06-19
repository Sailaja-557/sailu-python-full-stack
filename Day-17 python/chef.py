t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    p=0
    for i in range(n):
        if a[i]>= x:
            p+=b[i]
    print(p)
    #output...
#     4
#     2 20
#     20 67
#     10 90
#     100