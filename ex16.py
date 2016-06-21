from sys import argv

script, filename=argv

print"we are going to erase %r"% filename
print"if you dont want that ,hit CTRL-Z"
print"if you do want that ,hit return."

raw_input("?")

print"opening a file..."
target=open(filename,'w')

print"truncating the file.goodbye!"
target.truncate()
#target.close()
print"now i am going to ask you for three lines"
line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")
print"i am going to write these  to the file"

'''target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")'''

target.write("%s\n%s\n%s\n"%(line1,line2,line3))
target.write(line1+line2+line3)

print"and finally, we close it."
target.close()