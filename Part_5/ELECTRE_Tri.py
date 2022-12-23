###  ELECTRE TRI SORT SCORE

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
        if s == 1:
            category = k
            break
    return category

def PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterion][i] for criterion in criteria]
        category = PessimisticElectre(a,weights,limiting_profiles,threshold)
        category_nb = chr(category+97)
        data_res.append([data['code'][i],category_nb])
    return data_res
    
def OptimisticElectre(a,weights,limiting_profiles,threshold):
    category = 0
    profiles = load_profiles(limiting_profiles)
    for k in range(6):
        s = P_lambda(profiles[k],a,weights,threshold)
        if s == 1:
            category = k-1
            break
    return category

def OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterion][i] for criterion in criteria]
        category = OptimisticElectre(a,weights,limiting_profiles,threshold)
        category_nb = chr(category+97)
        data_res.append([data['code'][i],category_nb])
    return data_res