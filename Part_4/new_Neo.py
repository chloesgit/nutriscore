from nutrients_new_points import *

# Computes Neo points


def New_Neo(row, dataset):
    negative = sugar_points(row["Sugars"], dataset)+saturated_fat_points(
        row["Saturated_fatty_acids"], dataset)+salt_points(row["Salt"], dataset)
    positive = protein_points(row["Proteins"], dataset)+fruit_veg_points(
        row["Fruit/vegetable"], dataset)+fiber_points(row["Fiber"], dataset)
    New_Neo = negative-positive
    return (New_Neo)


# Computes Neo categories based on the percentiles of the dataset.


def a_e_score_NewNeo(row, dataset):
    if New_Neo(row, dataset) < dataset["NewNeo"].quantile(0.2):
        return ("a")
    if New_Neo(row, dataset) < dataset["NewNeo"].quantile(0.4):
        return ("b")
    if New_Neo(row, dataset) < dataset["NewNeo"].quantile(0.6):
        return ("c")
    if New_Neo(row, dataset) < dataset["NewNeo"].quantile(0.8):
        return ("d")
    if New_Neo(row, dataset) >= dataset["NewNeo"].quantile(0.8):
        return ("e")
