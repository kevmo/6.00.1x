import os
import sys

names = os.path.join(sys.path[0], 'names.txt')

# Write
nameHandle = open(names, 'w')
for i in range(2):
    name = raw_input('Enter a name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

# Read
nameHandle = open(names, 'r')
for line in nameHandle:
    print line
nameHandle.close()

# Append
nameHandle = open(names, 'a')
nameHandle.write("The G.O.A.T.")
nameHandle.close()
nameHandle = open(names, 'r')
for line in nameHandle:
    print line
nameHandle.close()

