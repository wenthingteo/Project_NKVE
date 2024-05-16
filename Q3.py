def choosing_treasures(bag_w, item_w, value, num_items):

    # Define a list of items, where each item is represented as a tuple
    # (name, value in million dollars, weight in kilograms)
    items = [
        ("Sceptre of Eternal Power", 'Priceless', 5),
        ("The Eye of Horus Pendant", 2, 0.5),
        ("The Ankh of Immortality", 5, 1.5),
        ("The Scarab Amulet of Fortune", 1.5, 0.2),
        ("The Golden Mask of Osiris", 10, 2),
        ("The Crown of the Pharaohs", 15, 3),
        ("The Emerald Scarab of Transformation", 3, 2)
    ]

    # Placeholder value for 'Priceless' during calculation
    priceless_value = 1000

    # Initialize a 2D list (DP table) to store maximum values
    K = [[0 for _ in range(bag_w + 1)] for _ in range(num_items + 1)]

    # Fill the DP table using bottom-up approach
    for i in range(num_items + 1):
        for w in range(bag_w + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif item_w[i - 1] <= w:
                if value[i - 1] == 'Priceless':
                    # Use the placeholder value for 'Priceless' only if there is enough space in the bag
                    if item_w[i - 1] <= w:
                        K[i][w] = max(priceless_value + K[i - 1][w - item_w[i - 1]], K[i - 1][w])
                    else:
                        K[i][w] = K[i - 1][w]
                else:
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

    # Print output in columns
    selected_item_weight = 0
    print("Selected Item".ljust(30), "Value($ Mil)".ljust(18), "Weight(kg)")
    for item in selected_items:
        selected_item_weight += item[2]
        # Replace placeholder value with 'Priceless' in the output
        value_str = 'Priceless' if item[1] == 'Priceless' else f"${item[1]} Mil"
        print(item[0].ljust(30), value_str.ljust(18), str(item[2]))

    return (f"\nTotal value in the bag: ${K[num_items][bag_w]} Million\nTotal weight in the bag: {selected_item_weight} kg")

value = ['Priceless', 2, 5, 1.5, 10, 15, 3]
item_w = [5000, 500, 1500, 200, 2000, 3000, 2000] #Assign the Weight in grams
bag_w = 10000 
num_items = len(value)

print(choosing_treasures(bag_w, item_w, value, num_items))
