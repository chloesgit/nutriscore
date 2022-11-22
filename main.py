import pandas as pd
from nutriscore_points import *
from Nei import *
from Neo import *
from table_update_Nei_Neo import *
from comparison_with_nutriscore import *


# converts excel dataset to pandas
food_dataset = pd.read_csv("final_dataset4.csv")
# creates two new columns in the dataset: Nei and Neo
food_dataset = table_update_scores(food_dataset)
food_dataset=table_update_scores_a_e(food_dataset)
print("updated dataset", food_dataset)

food_dataset.to_csv("dataset_filled.csv")

# compares the two new scores with the nutriscore
Neo_compared_to_nutriscore = Neo_compared_to_nutriscore(food_dataset)
Nei_compared_to_nutriscore = Nei_compared_to_nutriscore(food_dataset)
Neo_compared_to_Nei=Neo_compared_to_Nei(food_dataset)

print("Neo is greater than nutriscore",
      Neo_compared_to_nutriscore["greater"], "times")
print("Neo is equal to nutriscore",
      Neo_compared_to_nutriscore["equal"], "times")
print("Neo is lower than nutriscore",
      Neo_compared_to_nutriscore["lower"], "times")


print("Nei is greater than nutriscore",
      Nei_compared_to_nutriscore["greater"], "times")
print("Nei is equal to nutriscore",
      Nei_compared_to_nutriscore["equal"], "times")
print("Nei is lower than nutriscore",
      Nei_compared_to_nutriscore["lower"], "times")

print("Neo is greater than Nei",
      Neo_compared_to_Nei["greater"], "times")
print("Neo is equal to Nei",
      Neo_compared_to_Nei["equal"], "times")
print("Neo is lower than Nei",
      Neo_compared_to_Nei["lower"], "times")
