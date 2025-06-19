# method-1

def slug_generator(string):
    result = ""
    string = string.lower()
    
    for char in string:
        if char.isalnum():
            result += char
        elif char == " ":
            result += "-"
        
    return result

title=input()
result = slug_generator(title)
print(result)

#method-2
def slug_generator(s):
  # t=string.replace(' ','-')
  # t.lower()
  # return t
  s=s.lower()
  s=list(s)
  result=""
  for i in range(0,len(s)):
    if s[i].isalnum():
      result+=s[i]
    elif s[i]==" ":
      result+="-"
    else:
      continue
  return result
title=input()
result=slug_generator(title)
print(result)