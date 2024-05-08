def generate_combinations():
    count = 0
    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                count += 1
                print(f"{i}{j}{k}", end=" ")
                if count % 30 == 0:
                    print() 
    print("\nTotal number of combinations:", count)

generate_combinations()


