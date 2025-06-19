#input format:"ramm@gmail.com" 
#input format:"ram@jfhig.jrj"
#output format: ramm@gmail.com
#output format: ram@jfhig.jrj
p=input()
s=p[1:len(p)-1]
print(s)
if  "@" and "." in s:
    print("True")
else:
    print("False")



