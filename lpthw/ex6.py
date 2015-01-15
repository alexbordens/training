# setting the variable x as a string and string formatted integer
x = "There are %d types of people." % 10

# setting the variable as a string
binary = "binary"

# setting the variable as a string
do_not = "don't"

# setting the string
y = "Those who know %s and those who %s." % (binary, do_not)

# print the x and y strings
print x
print y

# print the statement and place the string assigned to x inside
print "I said: %r." % x
# print the statement and place the string assigned to y inside
print "I also said: '%s'." % y

# set the variable to boolean
hilarious = False

# set the variable to a string with a string formatter
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string with hilarious inside 
print joke_evaluation % hilarious

# assign string variables
w = "This is the left side of..."
e = "a string with a right side."

# print the two strings
print w + e