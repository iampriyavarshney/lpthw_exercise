s="priya varshney lives in aligarh studies in amu"
#name = priya varsney
#lives in =  aligarh
#study = amu
def split(s):
	a=s.split('lives in')
#print a
	b=a[0]
#print "name=%s"%b
	c=a[1].split('studies in')
	return a[0],c[0],c[1]


words=split(s)
print words
print"name=%s"% words[0] 

print "lives in=%s"% words[1]
print"study=%s"% words[2]