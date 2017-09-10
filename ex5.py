name = 'Zed A. Shaw'
age = 35 # not a lie
height = 180.0 #cm
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r meters tall." % (height/100)
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." % (age, height, weight, age + height + weight)