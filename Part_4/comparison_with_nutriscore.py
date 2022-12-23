
# Calculates the number of products with a nutriscore greater, equal or lower than the Nei score
def Nei_compared_to_nutriscore(dataset):
    greater = 0
    equal = 0
    lower = 0
    for index in dataset.index:
        dataset_item_Nei = dataset.loc[index, "Nei_score"]
        dataset_item_Nutriscore = dataset.loc[index, "Nutriscore"]
        if dataset_item_Nei > dataset_item_Nutriscore:
            greater += 1
        elif dataset_item_Nei == dataset_item_Nutriscore:
            equal += 1
        else:
            lower += 1
    return {"greater": greater, "equal": equal, "lower": lower}

# Calculates the number of products with a nutriscore greater, equal or lower than the Neo score


def Neo_compared_to_nutriscore(dataset):
    greater = 0
    equal = 0
    lower = 0
    for index in dataset.index:
        dataset_item_Neo = dataset.loc[index, "Neo_score"]
        dataset_item_Nutriscore = dataset.loc[index, "Nutriscore"]
        if dataset_item_Neo > dataset_item_Nutriscore:
            greater += 1
        elif dataset_item_Neo == dataset_item_Nutriscore:
            equal += 1
        else:
            lower += 1
    return {"greater": greater, "equal": equal, "lower": lower}

# Calculates the number of products with a Neo score greater, equal or lower than the Nei score


def Neo_compared_to_Nei(dataset):
    greater = 0
    equal = 0
    lower = 0
    for index in dataset.index:
        dataset_item_Neo = dataset.loc[index, "Neo_score"]
        dataset_item_Nei = dataset.loc[index, "Nei_score"]
        if dataset_item_Neo > dataset_item_Nei:
            greater += 1
        elif dataset_item_Neo == dataset_item_Nei:
            equal += 1
        else:
            lower += 1
    return {"greater": greater, "equal": equal, "lower": lower}
