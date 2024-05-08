def generate_combinations():
    total_combinations = 0
    combinations = []

    combination = [0, 0, 0]

    while combination != [9, 9, 9]:
        combinations.append(tuple(combination))
        total_combinations += 1

        for i in range(2, -1, -1):
            if combination[i] < 9:
                combination[i] += 1
                break
            else:
                combination[i] = 0

        if total_combinations % 35 == 0:
            process_combinations(combinations)
            combinations = []

    combinations.append((9, 9, 9))
    total_combinations += 1
    process_combinations(combinations)

    return total_combinations

def process_combinations(combinations):
    print(" ".join("".join(str(digit) for digit in combination) for combination in combinations))

total_combinations = generate_combinations()
print("\nTotal number of combinations:", total_combinations)



