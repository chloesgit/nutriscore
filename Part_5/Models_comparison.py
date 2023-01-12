import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

from ELECTRE_Tri import OptimisticElectreSorting,PessimisticElectreSorting
from Parameters_creation import generate_limiting_profiles,generate_limiting_profiles2

### IMPORT DATASET

final_dataset = "Part_6/chocolate_dataset.csv"
lines = pd.read_csv(final_dataset)

# 2 sets of weights
weights1 = [2,2,2,2,1,1,1]
total_weights = sum(weights1)
weights1 = [w/total_weights for w in weights1]

weights2 = [2,3,3,2,1,1,1]
total_weights = sum(weights2)
weights2 = [w/total_weights for w in weights2]

def stats_total_sorts(data,criteria,Weights):
    limiting_profiles = generate_limiting_profiles2(data,criteria)
    sorts = []
    labels = []
    for i,weights in enumerate(Weights):
        for threshold in [0.5,0.6,0.7]:
            pessimisticScore = PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
            optimisticScore = OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
            sorts.append(pessimisticScore)
            sorts.append(optimisticScore)
            label = "weight: "+str(i)+" threshold:"+str(threshold)+" Pessimistic"
            labels.append(label)
            label = "weight: "+str(i)+" threshold:"+str(threshold)+" Optimistic"
            labels.append(label)
    stats_nutriscores(sorts,"",labels)
    return 0

### COMPARE SCORES

# load original score
def extract_original_score(lines):
    res = []
    for i in range(len(lines)):
        res.append([lines['code'][i],lines['Nutriscore'][i]])
    return res

# stats for given scores
def stats_nutriscores(scores,title="",labels=[]):
    X = [i for i in range(5)]
    for k,score in enumerate(scores):
        Y = [0 for _ in range(5)]
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

# compare 2 nutriscores using pairwise comparison
def compare_nutriscores(score1,score2):
    res = [ {} for _ in range(5) ]
    for i in range(len(score1)):
        cat1 = ord(score1[i][1])-97
        cat2 = ord(score2[i][1])-97
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

# display pairwise comparison of 2 nutriscores
def stats_compare_nutriscores(score1,score2,title):
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


### COMPARE ORIGINAL SORT AND PESSIMISTIC SORT

def load_score(score):
    column_name = 'Part_5 model'
    res = []
    for i in range(len(score)):
        res.append([score['code'][i],score[column_name][i]])
    return res

def final_compare(data,criteria):

    limiting_profiles = generate_limiting_profiles2(data,criteria)
    weights = weights1
    threshold = 0.6

    pessimistic = PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
    original = extract_original_score(lines)
    optimistic = OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
    
    # stats on pessimistic and optimistic
    stats_nutriscores([pessimistic, optimistic,original],'Models: Number of products by category', ['Pessimistic','Optimistic','Original Nutriscore'])
    
    # comparison between pessimistic ELECTRE-Tri and original Nutriscore
    stats_compare_nutriscores(pessimistic,original,'Original nutriscore categories distribution depending on the Pessimistic ELECTRE-Tri categories')
    stats_compare_nutriscores(optimistic,original,'Original nutriscore categories distribution depending on the Optimistic ELECTRE-Tri categories')
    
    # comparison between pessimistic ELECTRE-Tri and optimistic
    stats_compare_nutriscores(pessimistic,optimistic,'Optimistic nutriscore categories distribution depending on the Pessimistic ELECTRE-Tri categories')
    
    # comparison between pessimistic ELECTRE-Tri weights1 and weights2
    pessimistic2 = PessimisticElectreSorting(data,criteria,weights2,limiting_profiles,threshold)
    stats_compare_nutriscores(pessimistic,pessimistic2,'Pessimistic (with weights2) nutriscore categories distribution depending on\n the Pessimistic ELECTRE-Tri (with weights1) categories')
    
    # comparison between pessimistic ELECTRE-Tri threshold 0.5 and 0.7
    pessimistic31 = PessimisticElectreSorting(data,criteria,weights,limiting_profiles,0.5)
    pessimistic32 = PessimisticElectreSorting(data,criteria,weights,limiting_profiles,0.7)
    stats_compare_nutriscores(pessimistic31,pessimistic32,'Pessimistic (with threshold 0.7) nutriscore categories distribution depending\n on the Pessimistic ELECTRE-Tri (with threshold 0.5) categories')
    
    # comparison between pessimistic ELECTRE-Tri limiting profiles naive and v2
    limiting_profiles2 = generate_limiting_profiles(data,criteria)
    pessimistic4 = PessimisticElectreSorting(data,criteria,weights,limiting_profiles2,threshold)
    stats_compare_nutriscores(pessimistic,pessimistic4,'Pessimistic (with \'naive\' limiting profiles) nutriscore categories distribution\n depending on the Pessimistic ELECTRE-Tri (with threshold 0.5) categories')
    