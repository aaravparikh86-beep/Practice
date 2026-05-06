# Syntax for opening a file:
# open("filename", "mode of opening(read mode by defalt)")

f = open("File-IO\\hello.txt")

# to read from file line by line
text = f.readline() 
print(text)
f.close()


# to read file
with open("File-IO\\hello.txt",'r') as f:
    a = f.read()

#to write file
with open("File-IO\\hello.txt",'w') as f:
    a = f.write("hi\n")

# when we use with we don't need to close