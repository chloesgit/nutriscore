from nutriscore_points import *

# Computes Neo points


def Neo(row):
    negative = (10-sugar_points(row["Sugars"]))+(10-saturated_fat_points(
        row["Saturated_fatty_acids"]))+(10-salt_points(row["Salt"]))
    positive = (protein_points(row["Proteins"])+fruit_veg_points(
        row["Fruit/vegetable"])+fiber_points(row["Fiber"]))*2
    Neo = negative+1/2*positive
    return (Neo)


def score_Neo(row):
    return (30 - Neo(row))

# Computes Neo categories based on the percentiles of the dataset.


def a_e_score_Neo(row, dataset):
    if score_Neo(row) < dataset["Neo"].quantile(0.2):
        return ("a")
    if score_Neo(row) < dataset["Neo"].quantile(0.4):
        return ("b")
    if score_Neo(row) < dataset["Neo"].quantile(0.6):
        return ("c")
    if score_Neo(row) < dataset["Neo"].quantile(0.8):
        return ("d")
    if score_Neo(row) >= dataset["Neo"].quantile(0.8):
        return ("e")
