# Search an element in an array You are given an array A of size N and an element X. Your task is to find whether the array 
# A contains the element X or not.
  # method-1......
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if X in A:
        print("YES")
        break
    else:
        print("NO")
        break

#method-2....
N, X = map(int, input().split())
A = list(map(int, input().split()))
if X in A:
    print("YES")
        
else:
    print("NO")


