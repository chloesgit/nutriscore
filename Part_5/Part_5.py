import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

lines = pd.read_excel("food_dataset.xlsx")

""" headers = ['code', 'product_name_fr', 'quantity', 'brands', 'energy-kcal_value',
 'saturated-fat_value', 'sugars_value', 'fiber_value', 'proteins_value',
 'salt_value', 'Fruit/Vegetable, %', 'off:nutriscore_grade',
 'off:nutriscore_score']"""

###

criteria = [
    'Energy',#'energy-kcal_value',
    'Sugars',#'sugars_value',
    'Saturated fatty acids',#'saturated-fat_value',
    'Salt',#'salt_value',
    'Proteins',#'proteins_value',
    'Fiber',#'fiber_value',
    'Fruit/vegetable'#'Fruit/Vegetable, %'
]
weights = [2,2,2,2,1,1,1]
#weights = [2,2,2,2,-1,-1,-1]
total_weights = sum(weights)
weights = [w/total_weights for w in weights]
threshold = 0.5

def data_value(lines, criteria):
    data = pd.DataFrame(lines)
    for crit in criteria:
        line = []
        for val in lines[crit]:
            line.append(val)
        data[crit] = line
    return data

data = data_value(lines, criteria)

def generate_limiting_profiles(lines,criteria):
    res = []
    for crit in criteria:
        mini,maxi = lines[crit].min(),lines[crit].max()
        profile = [mini + (maxi-mini)*i/5 for i in range(6)]
        res.append(profile)
    return res

limiting_profiles = generate_limiting_profiles(data,criteria)

def compute_score(a,weights,profile):
    res = 0
    for i,w in enumerate(a):
        if w > profile[i]:
            res += weights[i]
    return res

def load_profiles(limiting_profiles):
    profiles = []
    for i in range(len(limiting_profiles[0])):
        profile = []
        for j in range(len(limiting_profiles)):
            profile.append(limiting_profiles[j][i])
        profiles.append(profile)
    return profiles

def PessimisticmajoritySortingElement(a,weights,limiting_profiles,threshold):
    profiles = load_profiles(limiting_profiles)
    scores = []
    category = 0
    for profile in profiles:
        score = compute_score(a,weights,profile)
        scores.append(score)
        if score >= threshold:
            category +=1
    return category

def PessimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterium][i] for criterium in criteria]
        category = PessimisticmajoritySortingElement(a,weights,limiting_profiles,threshold)
        data_res.append([data['code'][i],category])
    return data_res

def OptimisticmajoritySortingElement(a,weights,limiting_profiles,threshold):
    profiles = load_profiles(limiting_profiles)[::-1]
    scores = []
    category = 0
    for profile in profiles:
        score = compute_score(a,weights,profile)
        scores.append(score)
        if score < threshold:
            category +=1
    return category

def OptimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterium][i] for criterium in criteria]
        category = PessimisticmajoritySortingElement(a,weights,limiting_profiles,threshold)
        data_res.append([data['code'][i],category])
    return data_res

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

def compute_total_sorts(data,criteria,weights,limiting_profiles,threshold):
    pessimisticScore = PessimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold)
    optimisticScore = OptimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold)
    write_sorting("PessimisticSort_"+str(threshold).replace('.','')+".csv",pessimisticScore)
    write_sorting("OptimisticSort_"+str(threshold).replace('.','')+".csv",optimisticScore)
    for i in range(len(pessimisticScore)):
        if pessimisticScore[i][1] != optimisticScore[i][1]:
            print(pessimisticScore[i],optimisticScore[i])

def stats_nutriscores(score):
    X = [i for i in range(5)]
    Y = [0 for _ in range(5)]
    for el in score:
        Y[el[1]] += 1
    plt.plot(X,Y)
    plt.title('Number of products by category')
    plt.show()

stats_nutriscores(PessimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold))

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

def extract_original_score(lines):
    res = []
    for i in range(len(lines)):
        res.append([lines['code'][i],lines['Nutriscore'][i]])
    return res

def stats_compare_nutriscores(score1,score2):
    comparison = compare_nutriscores(score1,score2)
    labels = ['0','1','2','3','4']
    score2_rep = [[0 for _ in range(5)] for _ in range(5)]
    for i,dic in enumerate(comparison):
        for cat in dic.keys():
            score2_rep[ord(cat)-97][i] = dic[cat]
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

score1 = (PessimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold))
score2 = extract_original_score(lines)
stats_compare_nutriscores(score1,score2)

compute_total_sorts(data,criteria,weights,limiting_profiles,threshold)