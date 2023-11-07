def clump_finding(genome, k, L, t):

#genome = DNA STRING
#k = size of k-mer
#L = length of genome
#t = Number that times
    clumps = set()
    kmer_counts = {}

    for i in range(len(genome) - L + 1):
        window = genome[i:i + L]
        kmer_counts.clear()

        for j in range(len(window) - k + 1):
            kmer = window[j:j + k]

            if kmer not in kmer_counts:
                kmer_counts[kmer] = 1
            else:
                kmer_counts[kmer] += 1

            if kmer_counts[kmer] >= t:
                clumps.add(kmer)

    return list(clumps)

# Example usage:
#genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGTGAGGACAGAGTGAAGAGAAGAGGAAAGAGGAAAGAGGACGAAG"
#k = 5
#L = 50
#t = 4

#clump_patterns = clump_finding(genome, k, L, t)
#print(f"Distinct k-mers forming ({L}, {t})-clumps:", clump_patterns)
