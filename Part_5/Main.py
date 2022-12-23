import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from ELECTRE_Tri import OptimisticElectreSorting,PessimisticElectreSorting
from Parameters_creation import generate_limiting_profiles,generate_limiting_profiles2
from Category_study import overview_categories,compare_categories, generate_categories_results
from Models_comparison import extract_original_score, final_compare, stats_total_sorts
from Storage import save_total_sorts
from Category_study import total_categories_comparison

### IMPORT DATASET

final_dataset = "Part_6/chocolate_dataset.csv"
lines = pd.read_csv(final_dataset)

### DEFINE PARAMETERS

# criteria
criteria = [
    'Energy',
    'Sugars',
    'Saturated_fatty_acids',
    'Salt',
    'Proteins',
    'Fiber',
    'Fruit/vegetable'
]
#code,name,quantity,brands,Energy,Saturated_fatty_acids,Sugars,Fiber,Proteins,Salt,Fruit/vegetable,Nutriscore,Nutriscore_point

# 2 sets of weights
weights1 = [2,2,2,2,1,1,1]
total_weights = sum(weights1)
weights1 = [w/total_weights for w in weights1]

weights2 = [2,3,3,2,1,1,1]
total_weights = sum(weights2)
weights2 = [w/total_weights for w in weights2]

# threshold
threshold = 0.6

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

limiting_profiles = generate_limiting_profiles2(data,criteria)


### MAIN FUNCTION

if __name__=="__main__":
    # to store all sorts
    if False:
        save_total_sorts(data,criteria,[weights1,weights2])

    # to display the models comparison
    if False:
        final_compare(data,criteria)

    # Models order comparison
    if False:
        stats_total_sorts(data,criteria,[weights2])
    
    # Models categories comparison
    if True:
        total_categories_comparison(lines,data,criteria,weights1,limiting_profiles,threshold)