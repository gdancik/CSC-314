###############################################################################
# list comprehension - allows for list construction in a 'natural' 
# and concise way, following mathematical syntax:

# mathematical notation: {f(x) : x in values}       
#       python notation: [f(x) for x in values]     	    

# mathematical notation: {f(x) : x in values and condition is true} 
#       python notation: [f(x) for x in values if condition]     
###############################################################################


# output squared numbers for numbers 1 - 10
print("print i^2 for i = 1, 2, ....10")
for i in range(1,11):
  print(i*i)

print()


# construct a list of squared numbers, for numbers 1 - 10
print("create list the old fashioned way")
squares = []
for i in range(1,11):
  squares.append(i*i)

# print list
print(squares)
print()

# use list comprehension
print("list comprehension: ")
squares = [i*i for i in range(1,11)]
print(squares)
print()

# use list comprehension with condition, to only look at even numbers
print("list comprehension with condition")
squares = [i*i for i in range(1,11) if i % 2 == 0]
print(squares)
print()

print("list comprehension where each value is a list")
squares = [ [i, i*i] for i in range(1,10) if i % 2 == 0]
print(squares)
print()

# print out element by element 
print ("i, i^2")
print ("-------")
for s in squares:
  print(s)

print()

# use list comprehension to find the max value in each set of numbers
# Note: max(x) returns the maximum value in list 'x'
numbers = [ [1,3,5], [2,3,1], [3,7], [11,2,6] ]
m = [max(nums) for nums in numbers]
print("numbers = ", numbers)
print("max of numbers is ", m)
print() 

###########################################################################
# Question 1: use list comprehension to create a list that contains
# the first number of each list in 'numbers'
###########################################################################

###########################################################################
# Question 2: use list comprehension to create a list where each element
# is itself a list containing the minimum and maximum number for each
# list in 'numbers'
###########################################################################



#######################################################
# Let's apply this concept to FASTA sequence data
#######################################################

from Bio import SeqIO # to parse sequence data

import urllib.request
import io # to convert string to 'handle'

# here we read in a file from a url, which must be converted
# to a file handle
url = "https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta"
handle = urllib.request.urlopen(url).read().decode('utf-8')
handle = io.StringIO(handle)

# parse sequences in 'fasta' format, which returns an iterator, 
sequence_iter = SeqIO.parse(handle, "fasta")

# convert the iterator to a list 
# (because python iterators cannot be reset)
sequences = [s for s in sequence_iter]


##########################################################
# Answer some questions about the sequences
##########################################################

# Question 1: how many sequences are there?

# Question 2: use list comprehension to create a list containing the 
# length of each sequence

# Question 3: use list comprehension to create a list containng the
# ID and length of each sequence that is more than 750 nucleotides long


