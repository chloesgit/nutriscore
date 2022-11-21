from nutriscore_points import *


def Nei(food_item, food_dataset):
    food_item_data = food_dataset[food_dataset["name"] == food_item]

    negative = (10-energy_points(food_item, food_dataset)) + \
        (10-salt_points(food_item, food_dataset))
    positive = (fruit_veg_points(food_item, food_dataset))*2
    Nei = negative+1/2*positive
    return (Nei)


def score_Nei(food_item, food_dataset):
    return (20 - Nei(food_item, food_dataset))


def a_e_score_Nei(food_item, food_dataset):
    if score_Nei(food_item, food_dataset) < 0:
        return ("a")
    if score_Nei(food_item, food_dataset) < 3:
        return ("b")
    if score_Nei(food_item, food_dataset) < 8:
        return ("c")
    if score_Nei(food_item, food_dataset) < 13:
        return ("d")
    if score_Nei(food_item, food_dataset) >= 13:
        return ("e")
