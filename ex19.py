def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print"you have %d cheese!"% cheese_count
	print"ypu have %d boxes of crackers!"% boxes_of_crackers
	print"man that's enough for a party!"
	print"get a blanket.\n"

print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)

print"or, we can use variable from our scripts."
cheese_count=10
amount_of_crackers=50

cheese_and_crackers(cheese_count, amount_of_crackers)


print"we can even do math inside too:"
cheese_and_crackers(10+20,5+6)


print"and we combine the two, variables and math:"
cheese_and_crackers(cheese_count+100, amount_of_crackers+1000)

#Write at least one more function of your own design, and run it 10 different ways.