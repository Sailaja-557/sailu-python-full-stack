post = [
    
    {"user":"aaa","post":"hey"},
    {"user":"bbb","post":"hi"},
    {"user":"ccc","post":"hello"},
    {"user":"aaa","post":"xxx"},
    {"user":"sss","post":"sailu"},
    {"user":"rrr","post":"rukku"},
    {"user":"ccc","post":"hey"}

]
ans={}
for i in post:
    if i["user"] in ans:
        ans[i["user"]]=ans[i["user"]] + 1
    else:
        ans[i["user"]] = 1
print(ans)
name=input()
if name in ans:
    print(f"{name}")


# post_count = {}

# for entry in post:
#     user = entry["user"]
#     post_count[user] = post_count.get(user, 0) + 1

# # Display the result
# for user, count in post_count.items():
#     print(f"{user}: {count} post(s)")