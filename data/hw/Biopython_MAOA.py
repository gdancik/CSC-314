####################################################################
# Lab 7: BioPython
# This script reads the MAOA genbank file that we have
# seen previously in Lab 5. Here, you will use BioPython
# to answer some of the questions you had answered in 
# the previous lab. Biopython must be used to answer the questions
# and to output the answers where indicated at the end of
# this script 
###################################################################

from Bio import SeqIO # to parse Seq data
#åfrom Bio.Seq import Seq # for Seq

import urllib.request
import io # to convert string to 'handle'


# get 'file' by retriving text through URL 
url = "https://raw.githubusercontent.com/gdancik/CSC-314/master/data/hw/MAOA.gb.txt"
handle = urllib.request.urlopen(url).read().decode('utf-8')
handle = io.StringIO(handle)

# gets an iterator that allows you to go through each entry
sequence_iter = SeqIO.parse(handle, "genbank")

# gets next sequence (which is the 1st one here)
seq_record = next(sequence_iter)

# print out full record
#print seq_record
print("seq length = ", len(seq_record))
print() 


# loop through each of the features
for feature in seq_record.features :

  # print out chromosome
  if feature.type == "source":
    print("=================== Chromosome ==================")
    print(feature.qualifiers['chromosome'][0])
    print() 
 
  # print out gene feature
  if feature.type == "gene":
    print("=================== Gene ==================")
    print(feature)

  # print out exon 13 #
  if feature.type == "exon": 
    if feature.qualifiers['number'][0] == '13':
      print("=================== Exon 13 ==================")
      print(feature)
      print()

  # print out CDS location #
  if feature.type == "CDS": 
    print("=================== CDS location ==================")
    numParts = len(feature.location.parts)
    end_cds_position = feature.location.parts[numParts-1] 
    print("CDS end position:", end_cds_position) 
    print()

##########################################################################
# Output the answers to the questions below, and answer the questions 
# using the appropriate python code to analyze the MAOA GenBank entry. 
# You must use python to analyze the GenBank entry, and your code must be
# generic so that it will work for any GenBank entry that contains 
# information for a single gene. Notes: for (5), use python splicing to 
# extract the nucleotides from the seq_record sequence object. This will 
# give you a Bio.Seq object. Then use the translate method of the 
# Bio.Seq object to translate the sequence.
# In answering the questions, you may assume that all exons in this entry
# are for the gene MAOA (this is true here, but some entries contain 
# multiple genes), and that the last part of the CDS contains at least 3 
# codons.
##########################################################################
print("1. The gene is on chromosome: ", "ANSWER HERE")
print("2. The first 5 nucleotides are: ", "ANSWER HERE")
print("3. The number of exons contained is: ", "ANSWER HERE")
print("4. The last 3 codons of the protein are: ", "ANSWER HERE")
print("5. The last 3 codons code for: ", "ANSWER HERE")
print("4. The last 3 codons of the protein are: ", "ANSWER HERE")
print("5. The last 3 codons code for: ", "ANSWER HERE") 
 