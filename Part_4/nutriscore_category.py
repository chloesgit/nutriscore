def a_e_score_Nutriscore_new(row, dataset):
    if row["Nutriscore_point"] < dataset["Nutriscore_point"].quantile(0.2):
        return ("a")
    if row["Nutriscore_point"] < dataset["Nutriscore_point"].quantile(0.4):
        return ("b")
    if row["Nutriscore_point"] < dataset["Nutriscore_point"].quantile(0.6):
        return ("c")
    if row["Nutriscore_point"] < dataset["Nutriscore_point"].quantile(0.8):
        return ("d")
    if row["Nutriscore_point"] >= dataset["Nutriscore_point"].quantile(0.8):
        return ("e")
