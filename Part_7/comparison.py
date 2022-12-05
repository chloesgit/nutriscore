import matplotlib.pyplot as plt
import pandas as pd

# load original score
def load_score(filename,column_name):
    lines = pd.read_csv(filename)

    res = []
    for i in range(len(lines)):
        res.append([lines['code'][i],lines[column_name][i]])
    return res

# stats for given scores
def stats_nutriscores(scores,title="",labels=[]):
    X = [i for i in range(5)]
    for k,score in enumerate(scores):
        Y = [0 for _ in range(5)]
        for el in score:
            Y[el[1]] += 1
        if labels!=[]:
            label = labels[k]
        else:
            label = str(k)
        plt.plot(X,Y,label=label)
    plt.title(title)
    plt.legend()
    plt.show()

# compare 2 nutriscores
def compare_nutriscores(score1,score2):
    res = [ {} for _ in range(5) ]
    for i in range(len(score1)):
        cat1 = score1[i][1]
        cat2 = score2[i][1]
        if cat2 not in res[cat1].keys():
            res[cat1][cat2] = 1
        else:
            res[cat1][cat2] += 1
    return res

# models to compare:
models = {
    "Part_4":"",
    "Part_5": "Part_5/Sorts/weights_1/PessimisticSort_threshold06.csv",
    "Part_6": "Part_6/results.csv"
}
column_name = {
    "Part_4":"",
    "Part_5": "Part_5 model",
    "Part_6": "Predicted_Nutriscore_ML"
}

print(load_score(models["Part_6"],column_name["Part_6"]))