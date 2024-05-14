def compare_letters(file1, file2):
    # Read the contents of the files and split into words
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        words1 = f1.read().split()
        words2 = f2.read().split()

    # Create a hash table for the words in the first letter
    hash_table = {word: True for word in words1}

    differences = []

    # Compare words from the second letter against the hash table
    for word in words2:
        if word not in hash_table:
            differences.append(word)

    # Print the differences
    for changed_word in differences:
        original_word = find_original_word(changed_word, words1, words2)
        print(f'Difference: {original_word} -> {changed_word}')

def find_original_word(changed_word, words1, words2):
    for index, word in enumerate(words2):
        if word == changed_word:
            return words1[index] if index < len(words1) else ''
    return ''

# File names
file1 = 'letter1.txt'
file2 = 'letter2.txt'

# Compare the letters
compare_letters(file1, file2)
