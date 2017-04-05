import sys

#Attempts to open the specified file and reports an error if the file is not in the same directory as the program.
try:
    input = open(sys.argv[1] , 'r')
    
except:
    print("Could not open file for reading. Please ensure that it is in the same directory as the program.")
    exit()
    
sequence = ''

#For each line in the target file, any data with a # out front is removed. The remaining information is stripped of excess lines, all spaces removed and coverted into capital letters. Then it is added onto a new string that will contain the entire sequence.
for line in input:     
    if line[0] == '#':
        continue
    line = line.strip()
    line = line.replace(" ","")
    line = line.upper()
    sequence += line
input.close()

def identify_type():
#List out the possible letters in the sequence that correlate to the specific idenity.
    validDNA = ["A", "T", "G", "C"]
    validRNA = ["A", "U", "G", "C"]
    validProtein = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]

#The program then goes through the sequence and determines if the codon is a part of DNA, RNA, or protein.
    countDNA = 0
    countRNA = 0
    countProtein = 0

    for letter in sequence:
    
        if letter in validDNA:
            countDNA += 1
    
        if letter in validRNA:
            countRNA += 1
            
        if letter in validProtein:
            countProtein += 1
            
#The number of codons that relate to the specific sequence types are compared to the sequence length to determine if the identity of the sequence. The results is then returned.

    if countDNA == len(sequence):
        result = 'DNA'
    
    elif countRNA == len(sequence):
        result = 'already RNA'

    elif countProtein == len(sequence):
        result = 'a Protein'
    
    else:
        result = 'not DNA, RNA, or a Protein.'
   
    return result

#This function is only executed if the identity of the sequence is DNA.
#It creates a new complement strand and converts the DNA into RNA by converting the codons into its appropriate pair.

def complement():
    
    complementStrand = ""
    
    for base in sequence:
            
        if base == "A":
            complementStrand += "T"
        if base == "T":
            complementStrand += "A"
        if base == "C":
            complementStrand += "G"
        if base == "G":
            complementStrand += "C"
                
    return complementStrand

#This function will only run when the sequence is determined to be DNA.
#Looping through the DNA complent strand, the function adds the codons to a new mRNA strand. Any T's are replaced with a U.
#The resulting mRNA strand is then returned.
def substitute():    
    mRNA = ''
    strand = complement()
    
    for base in strand:
        if base == "T":
            mRNA += "U"
        else:
            mRNA += base
            
    return mRNA
        

#The sequence type is then printed out and if the original sequence is DNA or RNA, the coresponding mRNA is determined and printed.

print ('This sequence is', identify_type())


if identify_type() == "DNA":
    print ("mRNA transcript after synthesis is:", substitute())
    
if identify_type() == "already RNA":
    print ("mRNA transcript after synthesis is:", sequence)
