def FREQUENTWORDS(Text, k):
    FrequentPatterns = set()
    COUNT = []

    # Create a list to store counts for each k-mer in Text
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        COUNT.append(PATTERNCOUNT(Text, Pattern))

    maxCount = max(COUNT)

    # Find k-mers with counts equal to maxCount
    for i in range(len(Text) - k + 1):
        if COUNT[i] == maxCount:
            FrequentPatterns.add(Text[i:i + k])

    return list(FrequentPatterns)  # Convert set to a list and return
