def choosing_treasures(bag_w, item_w, value, num_items):

    # Define a list of items, where each item is represented as a tuple
    # (name, value in million dollars, weight in kilograms)
    items = [
        ("Sceptre of Eternal Power", 1000, 5),
        ("The Eye of Horus Pendant", 2, 0.5),
        ("The Ankh of Immortality", 5, 1.5),
        ("The Scarab Amulet of Fortune", 1.5, 0.2),
        ("The Golden Mask of Osiris", 10, 2),
        ("The Crown of the Pharaohs", 15, 3),
        ("The Emerald Scarab of Transformation", 3, 2)
    ]

    # Initialize a 2D list (DP table) to store maximum values
    K = [[0 for _ in range(bag_w + 1)] for _ in range(num_items + 1)]

    # Fill the DP table using bottom-up approach
    for i in range(num_items + 1):
        for w in range(bag_w + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif item_w[i - 1] <= w:
                # If the current item can fit in the bag, choose the maximum value
                K[i][w] = max(value[i - 1] + K[i - 1][w - item_w[i - 1]], K[i - 1][w])
            else:
                # Otherwise, skip the item
                K[i][w] = K[i - 1][w]
                
    # Backtrack to find the selected items
    total_weight = bag_w
    selected_items = []
    for i in range(num_items,0,-1):
        if K[i][total_weight] != K[i-1][total_weight]:
            selected_items.append(items[i-1])
            total_weight -= item_w[i-1]

    #Print output
    print("Selected Item\t\t\tValue($ Mil)\tWeight(kg)")
    for item in selected_items:
        print(f"{item[0]}\t{item[1]}\t\t{item[2]}")

    return (f"\nTotal value in the bag: ${K[num_items][bag_w]} Million")

value = [1000, 2, 5, 1.5, 10, 15, 3]
item_w = [5000, 500, 1500, 200, 2000, 3000, 2000] #Assign the Weight in grams
bag_w = 10000 
num_items = len(value)
print(choosing_treasures(bag_w, item_w, value, num_items))