import os
import pandas as pd

from ELECTRE_Tri import PessimisticElectreSorting, OptimisticElectreSorting
from Parameters_creation import generate_limiting_profiles,generate_limiting_profiles2

final_dataset = "Part_6/chocolate_dataset.csv"

# save total sorts for all the assignments
def save_total_sorts(data,criteria,Weights):
    limiting_profiles = generate_limiting_profiles2(data,criteria)
    for i,weights in enumerate(Weights):
        for threshold in [0.5,0.6,0.7]:
            path = 'Part_5/Sorts/'+'weights_'+str(i)+'/'

            folders = path.split('/')
            current_folder = ''
            for folder in folders:
                if not os.path.exists(current_folder + folder):
                    os.makedirs(current_folder + folder)
                current_folder += folder+'/'

            pessimisticScore = PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)
            optimisticScore = OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)

            total_data_pessimistic = pd.read_csv(final_dataset)
            total_data_pessimistic['Part_5 model'] = [d[1] for d in pessimisticScore]
            total_data_optimistic = pd.read_csv(final_dataset)
            total_data_optimistic['Part_5 model'] = [d[1] for d in optimisticScore]
            
            total_data_pessimistic.to_csv(path+"PessimisticSort_threshold"+str(threshold).replace('.','')+".csv")
            total_data_optimistic.to_csv(path+"OptimisticSort_threshold"+str(threshold).replace('.','')+".csv")
    return 0