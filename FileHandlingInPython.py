#File Handling In Python

textFile = open('Text.txt' , mode = 'r')
print(textFile.read())

#print(textFile.read(6)) ...will print the first six characters
#print(textFile.readline())...will print eh first line
#print(textFile.readlines()).....will print all lines in a list[]
#for i in textFile:
#    print(i)         .... Will print all of the lines


textFile.close() #Dont leave your files open

with open('Text2.txt' , 'x') as text2:
    text2.write("I Love Python So Much")  # This creates a new Text File

# To never have to think about opening and closing the files, use dis

#with open('Text.txt', 'r') as textFile:
#   for i in textFile:          Be cautious of the Gap
#        print(i)



# ********************

# r = read
# a = append(edit)
# w = write and create a new file, delete the old file
# x = create a new file
# ADDITIONAL STUFF
#t = text ... so rt = read text
#b =  image

# ******************************