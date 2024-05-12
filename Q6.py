def weighted_scoring_island(islands, weights):
    # Hiigher score indicate more dangerous island
    land_condition_score = islands[1]
    wild_animals_score = islands[2]

    score = (
        weights['land_condition'] * land_condition_score +
        weights['wild_animals'] * wild_animals_score
    )

    return score

# Weight assumptions
weights = {
    'land_condition': 0.4,
    'wild_animals': 0.6
}

# Input data (Location, Land condition, Wild animals)
islands = [
    ("North",5,5),
    ("South",4,3),
    ("East",2,5),
    ("West",3,4),
    ("Middle",1,1)
]

island_scores = []

# Calculate the weighted score for each island
for island in islands:
    score = weighted_scoring_island(island, weights)
    island_scores.append((score, island[0]))

sorted_island_scores = sorted(island_scores, key=lambda x: x[0])

print("Island Location (from Safest to Most Dangerous)")
i = 1
for island in sorted_island_scores:
    print(f"{i} {island[1]}")
    i += 1