def Nei_compared_to_nutriscore(dataset):
    greater = 0
    equal = 0
    lower = 0
    for x in dataset["name"]:
        dataset_item = dataset[dataset["name"] == x]
        dataset_item_Nei = dataset_item["Nei"].item()
        dataset_item_Nutriscore = dataset_item["Nutriscore"].item()
        if dataset_item_Nei > dataset_item_Nutriscore:
            greater += 1
        elif dataset_item_Nei == dataset_item_Nutriscore:
            equal += 1
        else:
            lower += 1
    return {"greater": greater, "equal": equal, "lower": lower}


def Neo_compared_to_nutriscore(dataset):
    greater = 0
    equal = 0
    lower = 0
    for x in dataset["name"]:
        dataset_item = dataset[dataset["name"] == x]
        dataset_item_Neo = dataset_item["Neo"].item()
        dataset_item_Nutriscore = dataset_item["Nutriscore"].item()
        if dataset_item_Neo > dataset_item_Nutriscore:
            greater += 1
        elif dataset_item_Neo == dataset_item_Nutriscore:
            equal += 1
        else:
            lower += 1
    return {"greater": greater, "equal": equal, "lower": lower}
