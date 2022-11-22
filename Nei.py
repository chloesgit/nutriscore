from nutriscore_points import *


def Nei(row):
    negative = (10-energy_points(row["Energy"])) + (10-salt_points(row["Salt"]))
    positive = (fruit_veg_points(row["Fruit/vegetable"]))*2
    Nei = negative+1/2*positive
    return (Nei)


def score_Nei(row):
    return (20 - Nei(row))


def a_e_score_Nei(row,dataset):
    if row ["Nei"] < dataset["Nei"].quantile(0.2):
        return ("a")
    if row ["Nei"] < dataset["Nei"].quantile(0.4):
        return ("b")
    if row ["Nei"] < dataset["Nei"].quantile(0.6):
        return ("c")
    if row ["Nei"] < dataset["Nei"].quantile(0.8):
        return ("d")
    if row ["Nei"] >= dataset["Nei"].quantile(0.8):
        return ("e")
