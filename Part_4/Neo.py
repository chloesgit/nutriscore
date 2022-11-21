from nutriscore_points import *


def Neo(food_item, food_dataset):
    food_item_data = food_dataset[food_dataset["name"] == food_item]

    negative = (10-sugar_points(food_item, food_dataset))+(10-saturated_fat_points(
        food_item, food_dataset))+(10-salt_points(food_item, food_dataset))
    positive = (protein_points(food_item, food_dataset)+fruit_veg_points(
        food_item, food_dataset)+fiber_points(food_item, food_dataset))*2
    Neo = negative+1/2*positive
    return (Neo)


def score_Neo(food_item, food_dataset):
    return (30 - Neo(food_item, food_dataset))


def a_e_score_Neo(food_item, food_dataset):
    if score_Neo(food_item, food_dataset) < 0:
        return ("a")
    if score_Neo(food_item, food_dataset) < 3:
        return ("b")
    if score_Neo(food_item, food_dataset) < 11:
        return ("c")
    if score_Neo(food_item, food_dataset) < 19:
        return ("d")
    if score_Neo(food_item, food_dataset) >= 19:
        return ("e")
