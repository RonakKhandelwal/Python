def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print"You have %d cheese"%cheese_count
    print "You have %d boxes of cheese"%boxes_of_crackers
    print "Man that's enough for the party"
    print "Get a blanket \n"
print "We can give the numbers to the function directly ::"
cheese_and_crackers(10,20)


print" Or we can do it with the help of variables"
amount_of_cheese=10
amount_of_crackers=20
cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print"We can do math inside too"
cheese_and_crackers(10+5,20-5)

print "We can also combine variable and math"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+20)
