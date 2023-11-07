def pattern_matching(pattern, genome):
    positions = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            positions.append(i)

    return positions

# Example usage:
#pattern = "CTG"
#genome = "ACTGCATGCTGAAGCTGACCTGTGCTGCGTAACTGGGCTGCTGGCTG"
#matches = pattern_matching(pattern, genome)
#print("Positions where pattern appears:", matches)
