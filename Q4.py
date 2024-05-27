def myers_diff(letter_1, letter_2):
    # Split text into words
    words_1 = letter_1.split()
    words_2 = letter_2.split()
    
    # Initialize the matrix
    rows = len(words_1) + 1
    cols = len(words_2) + 1
    matrix = [[0] * cols for _ in range(rows)]
    
    # Fill in the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if words_1[i - 1] == words_2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    # Traceback to find the differences
    i, j = rows - 1, cols - 1
    differences = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and words_1[i - 1] == words_2[j - 1]:
            i -= 1
            j -= 1
        else:
            differences.append(f"Changed '{words_1[i - 1]}' to '{words_2[j - 1]}'")
            i -= 1
            j -= 1
            
    # Reverse to get correct order
    return differences[::-1]  

# Implementation
letter_1 = "To My Dearest Nefertari,\nAs I sit here amidst the grandeur of this ancient pyramid, surrounded by the whispers of the past, my thoughts turn to you, my beloved. Though miles may separate us, know that you are always in my heart, a beacon of light guiding me through the darkness of the unknown.\nAs I embark on this journey into the depths of the pyramid, I am filled with a mixture of excitement and trepidation. The allure of uncovering ancient secrets and treasures beckons me forward, but with each step I take, I am reminded of the risks that accompany such endeavors.\nI cannot help but think of the life we have built together, the moments of joy and laughter we have shared, and the love that binds us together across time and space. It is your unwavering support and encouragement that give me strength in the face of uncertainty, and for that, I am eternally grateful.\nThough the sands of time may have long since buried the civilization that built this magnificent structure, I find solace in the knowledge that our love transcends the ages, a timeless testament to the power of the human spirit.\nUntil we are reunited once more, know that you are always with me, guiding me through the labyrinth of life with your love and light.\nWith all my heart,\nYour devoted."
letter_2 = "To My Dearest Nefertari,\nAs I sit here amidst the grandeur of this antediluvian pyramid, surrounded by the whispers of the past, my thoughts turn to you, my beloved. Though miles may separate us, know that you are always in my heart, a beacon of light guiding me through the darkness of the unknown.\nAs I embark on this voyage into the depths of the pyramid, I am filled with a mixture of excitement and trepidation. The allure of uncovering ancient secrets and treasures beckons me forward, but with each step I take, I am reminded of the risks that accompany such endeavors.\nI cannot help but think of the life we have built together, the moments of joy and laughter we have shared, and the love that binds us together within time and space. It is your unwavering support and encouragement that give me strength in the face of uncertainty, and for that, I am eternally grateful.\nThough the sands of time may have long since buried the society that built this magnificent structure, I find solace in the knowledge that our love transcends the ages, a timeless testament to the power of the human spirit.\nUntil we are reunited once more, know that you are always with me, guiding me through the labyrinth of life with your love and light.\nWith all my heart,\nYour devoted."
print("Different words between letter 1 and letter 2:")
differences = myers_diff(letter_1, letter_2)
for diff in differences:
    print(diff)