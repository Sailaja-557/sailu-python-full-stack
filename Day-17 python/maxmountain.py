# Given a list of N integers, representing height of mountains. Find the height of the tallest mountain.
# Read number of test cases
T = int(input())
for i in range(T):
    # Read N (number of mountains)
    N = int(input())
    
    # Read the heights of the mountains
    heights = list(map(int,input().split()))
    
    # Find and print the maximum height
    print(max(heights))
  
 