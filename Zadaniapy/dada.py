

def DNA_strand(dna):
 converter = { 'A': 'T', 'T': 'A', 'C': 'G', 'G' : 'C'}
  
 return ''.capitalize().join([converter[i] for i in dna])

skibidi = "ATTGC"

for dna in skibidi:
    print(DNA_strand(dna))