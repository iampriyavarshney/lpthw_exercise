from sys import argv

if len(argv)>1:
	filename = argv[1]
else:
	filename =raw_input("Enter yor File name")

print ("Now its magic time press enter to see it ::::::PPPPPPP")
raw_input()

with open(filename) as fi:
	fi = compile(str(fi.read()))
	eval(fi)