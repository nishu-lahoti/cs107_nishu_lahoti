def dna_complement(sequence):
    
    b = [x for x in sequence]

    for i in b:
        if (i.upper() == "A"):
            print("T")
        elif(i.upper() == "T"):
            print("A")
        elif(i.upper() == "G"):
            print("C")
        elif(i.upper() == "C"):
            print("G")
        else:
            print("Your bases are incorrect.")
            return None
        
dna_sequence = "AT7GcXT"
dna_complement(dna_sequence)