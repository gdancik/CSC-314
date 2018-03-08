#############################################################
# A regular expression is a sequence of characters defining
# a search pattern used in a a string searching algorithm.
#############################################################

#############################################################
# we have already seen ways to find exact matches, using
# the 'in' operator or the 'find' method
#############################################################

sentence = "Hello, how are you?"

# in operator returns True or False
print("sentence: " + sentence)
print("sentence contains \"are\": ", "are" in sentence)
print("sentence contains \"the\": ", "the" in sentence)
print()

# find method returns index or -1 if not found
print("index of \"are\": ", sentence.find("are"))
print("index of \"the\": ", sentence.find("the"))
print()

##############################################################################
# A regular expression can be used to search for a pattern, which can
# include special characters
#   - a dot ('.') matches any character except a newline
#   - a dollar ('$') matches the end of a string (which may be
#     before a newline character)
#   - brackets [ab] will match any characters in the brackets 
#       (e.g., 'a' or 'b')
#   - brackets [1-4] will match any characters in the range 1-4
# For more information, see: https://docs.python.org/3.6/library/re.html
##############################################################################


# import re to use regular expressions in python
import re

# create regular expression that looks for file1.txt or file2.txt
pattern = re.compile("file[1-2].txt")

fileStr = "file0.txt file1.txt file2.txt file3.txt"

# find all occurences of the pattern; returns a list of matches
results = pattern.findall(fileStr)
print("Searching for file[1-2].txt pattern:")
print("# of results: ", len(results))
print("results: ", results)
print()

# what if pattern is not found?
results = pattern.findall("file0.txt")
print("When pattern is not found:")
print("# of results: ", len(results))
print("results: ", results)
print()


# find the position of each match; returns an interator, where 
# each element contains
#    .start() - the starting index of the match
#    .end() - the ending index of the match
#    .group() - the match 
results = pattern.finditer(fileStr)
print("Searching for file[1-2].txt pattern using .finditer:")
for r in results :
    print(r.group(), "found at:",  [r.start(), r.end()])
print()

results = pattern.finditer("file0.txt")
print("When pattern is not found: (iterator is empty)")
for r in results :
    print(r.group(), "found at:",  [r.start(), r.end()])
print()


# string substitution based on regular expressions
# re.sub(pattern, replacement, string) - replaces pattern in the string
# note the caret ('^') indicates we want to match any characters NOT in []
print("Substition using a regular expression to format a sequence: ")
seq = "ACFTGCAEG"
print("seq: " + seq)
seqFormatted = re.sub("[^ACTG]", "-", seq)
print("seq: " + seqFormatted + "(formatted)")

