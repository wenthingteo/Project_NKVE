from tabulate import tabulate

def weighted_scoring_island(island, weights):
    # Higher score indicates a more dangerous island
    land_condition_score = island['land_condition_score']
    wild_animals_score = island['wild_animals_score']

    score = (
        weights['land_condition'] * land_condition_score +
        weights['wild_animals'] * wild_animals_score
    )

    return score

# Weight assumptions
weights = {
    'land_condition': 0.3,
    'wild_animals': 0.7
}

# Input data as list of dictionaries
islands = [
    {"location": "North", "land_condition": "Swamp area", "wild_animals": "Full of wild animals", "land_condition_score": 5, "wild_animals_score": 5},
    {"location": "South", "land_condition": "Mountains and caves", "wild_animals": "Some wild animals", "land_condition_score": 4, "wild_animals_score": 3},
    {"location": "East", "land_condition": "Thick woods and a lake", "wild_animals": "Full of wild animals", "land_condition_score": 2, "wild_animals_score": 5},
    {"location": "West", "land_condition": "Sandy flat land", "wild_animals": "Small but poisonous animals", "land_condition_score": 3, "wild_animals_score": 4},
    {"location": "Middle", "land_condition": "Inhabited with villages and agriculture area", "wild_animals": "No wild animals", "land_condition_score": 1, "wild_animals_score": 1}
]

island_scores = []

for island in islands:
    island['total_score'] = weighted_scoring_island(island, weights)
    island_scores.append([island['location'], island['land_condition'], island['wild_animals'], island['total_score']])

island_scores.sort(key=lambda x: x[3])

# Print the table
print(tabulate(island_scores, headers=["Island Location", "Land Condition", "Wild Animals", "Score"]))
print(f"\nThe safest island to search is {island_scores[0][0]} island.")
