def load_profiles(limiting_profiles):
    profiles = []
    for i in range(len(limiting_profiles[0])):
        profile = []
        for j in range(len(limiting_profiles)):
            profile.append(limiting_profiles[j][i])
        profiles.append(profile)
    return profiles

def compute_score(a,weights,profile):
    res = 0
    for i,w in enumerate(a):
        if w > profile[i]:
            res += weights[i]
    return res

# Pessimistic sorting of 1 element
def PessimisticmajoritySortingElement(a,weights,limiting_profiles,threshold):
    profiles = load_profiles(limiting_profiles)
    scores = []
    category = -1
    for profile in profiles:
        score = compute_score(a,weights,profile)
        scores.append(score)
        if score >= threshold:
            category +=1
    return category

# Pessimistic sort
def PessimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterium][i] for criterium in criteria]
        category = PessimisticmajoritySortingElement(a,weights,limiting_profiles,threshold)
        data_res.append([data['code'][i],category])
    return data_res

# Optimistic sorting of 1 element
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

# Optimistic sort
def OptimisticmajoritySorting(data,criteria,weights,limiting_profiles,threshold):
    data_res = []
    for i in range(len(data)):
        a = [data[criterium][i] for criterium in criteria]
        category = PessimisticmajoritySortingElement(a,weights,limiting_profiles,threshold)
        data_res.append([data['code'][i],category])
    return data_res
