import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# load original score
def load_score(filename,column_name):
    lines = pd.read_csv(filename)

    res = []
    for i in range(len(lines)):
        res.append([lines['code'][i],lines[column_name][i]])
    return res

# models to compare:
models = {
    "Part_4": "Part_4/dataset_filled_Part4.csv",
    "Part_5": "Part_5/Sorts/weights_1/PessimisticSort_threshold06.csv",
    "Part_6": "Part_6/results.csv"
}
column_name = {
    "Part_4": "Neo_score",
    "Part_5": "Part_5 model",
    "Part_6": "Predicted_Nutriscore_ML"
}

score_4 = load_score(models["Part_4"],column_name["Part_4"])
score_5 = load_score(models["Part_5"],column_name["Part_5"])
score_6 = load_score(models["Part_6"],column_name["Part_6"])

#print(score_4[:100])

# stats for given scores
def stats_nutriscores(scores,title="",labels=[]):
    X = [i for i in range(5)]
    for k,score in enumerate(scores):
        Y = [0 for i in range(5)]
        for el in score:
            Y[ord(el[1])-97] += 1
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
    print(len(score1),len(score2))
    for i in range(len(score1)):
        cat1 = score1[i][1]
        cat2 = score2[i][1]

        cat1 = ord(cat1)-97
        cat2 = ord(cat2)-97
        
        if cat2 not in res[cat1].keys():
            res[cat1][cat2] = 1
        else:
            res[cat1][cat2] += 1
    return res


def transform_dict_to_plot_value(array):
    score2_rep = [[0 for _ in range(5)] for _ in range(5)]
    for i,dic in enumerate(array):
        for cat in dic.keys():
            try:
                score2_rep[cat][i] = dic[cat]
            except:
                score2_rep[ord(cat)-97][i] = dic[cat]
    return score2_rep

# display comparison of 2 nutriscores
def stats_compare_nutriscores(score1,score2,title=''):
    comparison = compare_nutriscores(score1,score2)
    labels = ['0','1','2','3','4']
    score2_rep = transform_dict_to_plot_value(comparison)

    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, score2_rep[0], width, label='a')
    bottom = np.array(score2_rep[0])

    for i in range(1,5):
        ax.bar(labels, score2_rep[i], width, bottom=bottom,
            label=str(chr(i+97)))
        bottom += np.array(score2_rep[i])

    ax.set_ylabel('Number')
    ax.set_title(title)
    ax.legend()

    plt.show()

stats_compare_nutriscores(score_4,score_5)