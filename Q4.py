def compare_letters(file1, file2):
    # Read the contents of the files and split into words
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        words1 = f1.read().split()
        words2 = f2.read().split()
    
    # Create sets from the words
    set1 = set(words1)
    set2 = set(words2)
    
    # Find the intersection of the sets
    common_words = set1.intersection(set2)
    
    # Identify the differences by comparing against the intersection
    differences = []
    for word1, word2 in zip(words1, words2):
        if word1 not in common_words or word2 not in common_words:
            differences.append((word1, word2))
    
    # Print the differences
    for diff in differences:
        print(f'Difference: {diff[0]} -> {diff[1]}')

# File names
file1 = 'letter1.txt'
file2 = 'letter2.txt'

# Compare the letters
compare_letters(file1, file2)
