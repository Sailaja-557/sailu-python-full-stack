# def is_leap(year):
#     if (year%100==0):
#        leap = False
#     if (year % 4 == 0) or (year % 400 == 0):
#       leap = True
#     else:
#        leap = False
#     return leap
# year = int(input())
# print(is_leap(year))
    #write your logic here

#method 2
def is_leap(year):
    if(year%100==0):
            leap = False
    if (year % 4 == 0) and (year % 400 == 0):
        leap = True
    else:
         leap = False
         return leap
year = int(input())
print(is_leap(year))