from sys import argv

script,filename=argv

print "We are going to erase %r"%(filename)
print "If you don't want that hit ctrl-c"
print "If you want that hit enter"

raw_input('?')

print "opening the file :...."
target=open(filename,'w')#if we remove the 'w' we will get an error as expected :D....it opens the file in read mode only so we can't make any changes

print "Truncating the file.  Goodbye!!!"

target.truncate()

print "Now I'm going to ask you for three lines"

line1=raw_input()
line2=raw_input()
line3=raw_input()

print "I am going to write this in the file."

one_target=line1+'\n'+line2+'\n'+line3

target.write(one_target)

line1=raw_input("New")
line2=raw_input("New")
line3=raw_input("New")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "Finally close it."

target.close()


