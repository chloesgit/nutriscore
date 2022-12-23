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
        res.append(profile)
    return res