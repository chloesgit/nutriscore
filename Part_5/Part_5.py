import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### IMPORT DATASET

lines = pd.read_csv("Part_6/final_dataset.csv")

### DEFINE PARAMETERS

# criteria
criteria = [
    'Energy',#'energy-kcal_value',
    'Sugars',#'sugars_value',
    'Saturated_fatty_acids',#'saturated-fat_value',
    'Salt',#'salt_value',
    'Proteins',#'proteins_value',
    'Fiber',#'fiber_value',
    'Fruit/vegetable'#'Fruit/Vegetable, %'
]
#code,name,quantity,brands,Energy,Saturated_fatty_acids,Sugars,Fiber,Proteins,Salt,Fruit/vegetable,Nutriscore,Nutriscore_point

# 2 sets of weights
weights1 = [2,2,2,2,1,1,1]
total_weights = sum(weights1)
weights = [w/total_weights for w in weights1]

weights2 = [2,2,2,2,1,1,1]
total_weights = sum(weights2)
weights = [w/total_weights for w in weights2]

# threashold
threshold = 0.5

# convert data loaded to usable data for our algorithms
def data_value(lines, criteria):
    data = pd.DataFrame(lines)
    for crit in criteria:
        line = []
        for val in lines[crit]:
            line.append(val)
        data[crit] = line
    return data

data = data_value(lines, criteria)

# generate limiting profiles
def generate_limiting_profiles(lines,criteria):
    # using uniform distribution of [min,max]
    res = []
    for crit in criteria:
        mini,maxi = lines[crit].min(),lines[crit].max()
        profile = [mini + (maxi-mini)*i/5 for i in range(6)]
        res.append(profile)
    return res
def generate_limiting_profiles2(lines,criteria):
    # using quantiles
    res = []
    for crit in criteria:
        profile = []
        for i in range(6):
            profile.append(lines[crit].quantile(i/5))
        mini,maxi = lines[crit].min(),lines[crit].max()
        res.append(profile)
    return res

limiting_profiles = generate_limiting_profiles2(data,criteria)


###  MAJORITY SORTING SCORE

# profile format transformation
def load_profiles(limiting_profiles):
    profiles = []
    for i in range(len(limiting_profiles[0])):
        profile = []
        for j in range(len(limiting_profiles)):
            profile.append(limiting_profiles[j][i])
        profiles.append(profile)
    return profiles

def concordance_index(a,b,weights):
    res = 0
    for i in range(len(a)):
        if b[i] - a[i] <= 0: # we consider each p_i = 0
            res += 1*weights[i]
    return res

def outranking_relation(a,b,weights,threshold):
    c = concordance_index(a,b,weights)
    if c >= threshold:
        return 1
    else:
        return 0

def P_lambda(a,b,weights,threshold):
    c1 = outranking_relation(a,b,weights,threshold)
    c2 = outranking_relation(b,a,weights,threshold)
    if c1 == 1 and c2 == 0:
        return 1
    else:
        return 0
    
def PessimisticElectre(a,weights,limiting_profiles,threshold):
    category = 5
    profiles = load_profiles(limiting_profiles)
    for k in range(5,-1,-1):
        s = outranking_relation(a,profiles[k],weights,threshold)
        if s == 0:
            category -= 1
    return category

def PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterium][i] for criterium in criteria]
        category = PessimisticElectre(a,weights,limiting_profiles,threshold)
        data_res.append([data['code'][i],category])
    return data_res
    
def OptimisticElectre(a,weights,limiting_profiles,threshold):
    category = -1
    profiles = load_profiles(limiting_profiles)
    for k in range(6):
        s = P_lambda(a,profiles[k],weights,threshold)
        if s == 0:
            category += 1
    return category

def OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterium][i] for criterium in criteria]
        category = OptimisticElectre(a,weights,limiting_profiles,threshold)
        data_res.append([data['code'][i],category])
    return data_res

# save data in files
def write_sorting(filename,data):
    data_str = ""
    for l in data:
        l_str = ""
        for el in l:
            l_str += str(el) + ","
        data_str += l_str[:-1]+"\n"
    print("writing sorting in "+filename+"...")
    output = open('Part_5/Sorts/'+filename,"w")
    output.write(data_str)
    output.close()

# save total sorts
def compute_total_sorts(data,criteria,weights,limiting_profiles,threshold):
    pessimisticScore = PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
    optimisticScore = OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
    write_sorting("PessimisticSort_"+str(threshold).replace('.','')+".csv",pessimisticScore)
    write_sorting("OptimisticSort_"+str(threshold).replace('.','')+".csv",optimisticScore)
    for i in range(len(pessimisticScore)):
        if pessimisticScore[i][1] != optimisticScore[i][1]:
            print(pessimisticScore[i],optimisticScore[i])


### COMPARE SCORES

# load original score
def extract_original_score(lines):
    res = []
    for i in range(len(lines)):
        res.append([lines['code'][i],lines['Nutriscore'][i]])
    return res

# stats for 1 given score
def stats_nutriscores(score):
    X = [i for i in range(5)]
    Y = [0 for _ in range(5)]
    for el in score:
        Y[el[1]] += 1
    plt.plot(X,Y)
    plt.title('Number of products by category')
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
def stats_compare_nutriscores(score1,score2):
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
    ax.set_title('Score2 categories distribution depending on score1 category')
    ax.legend()

    plt.show()


### COMPARE ORIGINAL SORT AND PESSIMISTIC SORT

"""for threshold in [0.5,0.6,0.7]:
    score1 = (PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold))
    score2 = extract_original_score(lines)
    stats_compare_nutriscores(score1,score2)
    score3 = OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
    stats_compare_nutriscores(score1,score3)
"""
compute_total_sorts(data,criteria,weights,limiting_profiles,threshold)