def reverse_complement(dna_sequence):
    # Define a dictionary to map DNA bases to their complements
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Convert the DNA sequence to uppercase to handle mixed cases
    dna_sequence = dna_sequence.upper()
    
    # Reverse the DNA sequence and compute the complement
    reverse_comp_sequence = ''.join(complement_dict[base] for base in reversed(dna_sequence))
    
    return reverse_comp_sequence

# Example usage:
#dna_sequence = "ATgcCtAg"
#reverse_comp = reverse_complement(dna_sequence)
#print("Reverse Complement:", reverse_comp)
