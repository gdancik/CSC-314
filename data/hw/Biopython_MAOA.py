###########################################################
# Lab 8: BioPython
# This script reads the MAOA genbank file that we have
# seen previously in Lab 5. Here, you will use BioPython
# to answer some of the questions you had answered in 
# that lab. Biopython must be used to answer the questions
# and to output the answers where indicated at the end of
# this script 
###########################################################

import urllib2  # to read file from url
from StringIO import StringIO # to convert string to 'handle'
from Bio import SeqIO # to parse Seq data
from Bio.Seq import Seq # for Seq

# get 'file' by retriving text through URL 
url = "http://bioinformatics.easternct.edu/CSC-314/MAOA.gb.txt"
file = urllib2.urlopen(url)
txt = file.read() # convert contents to string

# convert to handle, which behaves like open file, necessary for SeqIO
handle = StringIO(txt) 
print handle

# gets an iterator that allows you to go through each entry
iter = SeqIO.parse(handle, "genbank")

# gets next sequence (which is the 1st one here)
seq_record = next(iter)

# print out full record
#print seq_record
print "seq length = ", len(seq_record)
print 



# loop through each of the features
for feature in seq_record.features :

  # print out chromosome
  if feature.type == "source":
    print "=================== Chromosome =================="
    print feature.qualifiers['chromosome'][0] 
    print 
 
  # print out gene feature
  if feature.type == "gene":
    print "=================== Gene =================="
    print feature

  # print out exon 13 #
  if feature.type == "exon": 
	if feature.qualifiers['number'][0] == '13':
    		print "=================== Exon 13 =================="
    		print feature 
		print

  # print out CDS location #
  if feature.type == "CDS": 
    print "=================== CDS location =================="
    print feature.location
    print


##########################################################################
# Output the answers to the questions below, and answer the questions 
# using the appropriate python code to analyze the MAOA GenBank entry. 
# You must use python to analyze the GenBank entry to receive credit.
# Notes: for (5), create a Sequence object of the codons, and use BioPython to
#   translate the sequence. Note: when creating a sequence objects, the
#   codons must be converted to a string using the 'str' function 
##########################################################################
print "1. The gene is on chromosome: ", "ANSWER HERE" 
print "2. The first 5 nucleotides are: ", "ANSWER HERE"
print "3. The number of exons contained is: ", "ANSWER HERE"
print "4. The last 3 codons of the protein are: ", "ANSWER HERE"
print "5. The last 3 codons code for: ", "ANSWER HERE"

