from Nei import *
from Neo import *
from nutriscore_category import *


# Updates the table with the Neo and Nei points
def table_update_scores(food_dataset):
    columns = list(food_dataset)
    row_data = {}
    Nei = []
    Neo = []
    for index in food_dataset.index:
        for column in columns:
            row_data[column] = food_dataset.loc[index, column]

        Nei.append(score_Nei(row_data))
        Neo.append(score_Neo(row_data))
    food_dataset["Neo"] = Neo
    food_dataset["Nei"] = Nei
    return (food_dataset)

# Updates the table with the Neo and Nei scores


def table_update_scores_a_e(food_dataset):
    columns = list(food_dataset)
    row_data = {}
    Nei = []
    Neo = []
    for index in food_dataset.index:
        for column in columns:
            row_data[column] = food_dataset.loc[index, column]
        Nei.append(a_e_score_Nei(row_data, food_dataset))
        Neo.append(a_e_score_Neo(row_data, food_dataset))
    food_dataset["Neo_score"] = Neo
    food_dataset["Nei_score"] = Nei
    return (food_dataset)

# Updates the table with the new computation of Nutriscore categories based on the percentiles of the dataset


def table_update_scores_a_e_nutriscore(food_dataset):
    columns = list(food_dataset)
    row_data = {}
    Nutriscore = []
    for index in food_dataset.index:
        for column in columns:
            row_data[column] = food_dataset.loc[index, column]

        Nutriscore.append(a_e_score_Nutriscore_new(row_data, food_dataset))
    food_dataset["Nutriscore_new_score"] = Nutriscore
    return (food_dataset)
