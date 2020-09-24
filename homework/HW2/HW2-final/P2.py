# Function
def dna_complement(sequence):
    
    a = ""
    b = [x for x in sequence]

    for i in b:
        if (i.upper() == "A"):
            a += "T"
        elif(i.upper() == "T"):
            a += "A"
        elif(i.upper() == "G"):
            a += "C"
        elif(i.upper() == "C"):
            a += "G"
        else:
            print("Your bases are incorrect.")
            return None
    
    print a
        

# Demo
sequence_correct = "ATGCATACGGCCT"
print(sequence_correct)

sequence_wrong = "ATGCCTTX3GAAA"
print(sequence_wrong)

dna_complement(sequence_correct)
dna_complement(sequence_wrong)
