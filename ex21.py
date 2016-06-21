def add(a,b):
	print"adding %d +%d"%(a,b)
	return a+b

def substract (a,b):
	print "substracting %d - %d"%(a,b)
	return a-b

def multiply(a,b):
	print"mulyipying %d *%d"%(a,b)
	return a*b

def divide(a,b):
	print"dividing %d/%d"%(a,b)
	return a/b

#a=add(10,30)
#b=add(40,60)
#c=add(a,b)
#c=add(add(40,60),add(10,30))
#print c
print"lets do some maths with just functions!"
age=add(30,5)
height=substract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print"age:%d, height:%d, weight:%d, IQ:%d"%(age,height,weight,iq)

 # a puzzle for extra credit ,type it in anyway
print"here is a puzzle."

what=add(age,substract(height,multiply(weight,divide(iq,2))))

print"thats becomes:",what,"can you do it  by hand?"