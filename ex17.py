from sys import argv
#from os.path import exists 

#script, from_file, to_file=argv

#print"copying from %s to %s " %(from_file, to_file)
# we could do these two on one line,how?

#indata=open(from_file).read()

#Bprint"the input file is %d bytes long"% len(indata)

#print"does the output file exists %r?"% exists(to_file)
#print"ready, hit RETURN to continue, CTRL-C to abort."

#raw_input()

#open(to_file,'w').write(indata)
#out_file.write(indata)
#print"alright, all done."
#open(to_file,'w').write(open(from_file).read())
#out_file.close()
#in_file.close()
open(argv[2],'w').write(open(argv[1]).read())