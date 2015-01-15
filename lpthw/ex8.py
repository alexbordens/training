# create a variable of string formatters
formatter = "%r %r %r %r"

# print all four numbers
print formatter % (1, 2, 3, 4)

# print the four strings
print formatter % ("one", "two", "three", "four")

# print the boolean as string
print formatter % (True, False, False, True)

# print the formatters over and over 
print formatter % (formatter, formatter, formatter, formatter)

# print each string 
print formatter % (
	'I had this thing.,
	'That you could type up right.',
	"But it didn't sing.",
	'So I said goodnight.'
	)