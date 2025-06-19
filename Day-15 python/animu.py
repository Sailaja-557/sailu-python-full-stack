# for i in range(3):
#     print(i,"rey")
#     for j in range(2):
#         print("macha",j)
#     print(i,"tata")

# sentences = ["please wait", "continue to fight", "continue to win"]
# for i in range(len(sentences)):
#     wor=sentences[i]
#     print(wor)
#     for j in wor:
            
#      print(j, end="")

s = "one  problem  a  day"
temp = 0
for i in range(len(s)):
   val=s[i]
   if val == " ":
    temp=temp+1
print(temp-2)