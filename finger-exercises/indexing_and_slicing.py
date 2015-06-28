name = "Kevin Moore"

print "Name is the string: '{}'".format(name)

print "Indexing is 0-based and -1 returns the final index."
print "So this should just be an e:", name[-1]

print "Slicing is inclusive on the left, and exclusive on the right."
print "First name:", name[0:5]
print "First name and last initial", name[0:7]
print "So you have to slice the right side from 1+ the final position. Look at this 'o':", name[7]
