from Nei import *
from Neo import *


def table_update(food_dataset):
    food_dataset["Nei"] = [a_e_score_Nei(
        x, food_dataset) for x in food_dataset["name"]]
    food_dataset["Neo"] = [a_e_score_Neo(
        x, food_dataset) for x in food_dataset["name"]]
    return (food_dataset)
