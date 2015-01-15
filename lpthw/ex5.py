name = 'Zed A. Shaw'
age = 30 # not a lie
height = 9 # inches
weight = 200 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_centimeters = height * 2.54
weight_kilograms = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall or about %d centimers." % (height, round(height_centimeters))
print "He's %d pounds heavy or about %d kilograms." % (weight, round(weight_kilograms))
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)