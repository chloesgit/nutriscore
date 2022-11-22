from Nei import *
from Neo import *


def table_update_scores(food_dataset):
    columns=list(food_dataset)
    row_data={}
    Nei=[]
    Neo=[]
    for index in food_dataset.index:
        for column in columns:
            row_data[column]=food_dataset.loc[index, column]

        Nei.append(score_Nei(row_data))
        Neo.append(score_Neo(row_data))
    food_dataset["Neo"]=Neo
    food_dataset["Nei"]=Nei
    return (food_dataset)

def table_update_scores_a_e(food_dataset):
    columns=list(food_dataset)
    row_data={}
    Nei=[]
    Neo=[]
    for index in food_dataset.index:
        for column in columns:
            row_data[column]=food_dataset.loc[index, column]
        Nei.append(a_e_score_Nei(row_data,food_dataset))
        Neo.append(a_e_score_Neo(row_data,food_dataset))
    food_dataset["Neo_score"]=Neo
    food_dataset["Nei_score"]=Nei
    return (food_dataset)

