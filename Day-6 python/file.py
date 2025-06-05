#....read() files...
#book = open("./boom.txt","r")
# print(book.read()) # read the all data

# print(book.readline()) # read only single line

#data= book.readlines() # read all line in list format
#print(data)

#....append lines files....
# book = open("./boom.txt","a")
# book.write("\n This is append line") #append the data
# book = open("./boom.txt","r")
# print(book.read())

#....write files....
book=open("./boom.txt","w")        # okkasari manam file ni write mode lo open chesthe anthaku mundhu manam file lo read chesina data antha clear ayyipoyi
book.write("python python python") # new ga write mode lo open chesamu kabatti kottaga data enter avvutundhi
book.write("\n java java java")
book.writelines(["\n apple","\n cherry","\n banana"])