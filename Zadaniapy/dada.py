

def DNA_strand(dna):
 converter = { 'A': 'T', 'T': 'A', 'C': 'G', 'G' : 'C'}
  
 return ''.capitalize().join([converter[i] for i in dna])

skibidi = "ATTGC"

for dna in skibidi:
    print(DNA_strand(dna))
    
 
def to_jaden_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)