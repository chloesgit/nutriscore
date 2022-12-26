import pandas as pd
from nutriscore_points import *
from Nei import *
from Neo import *
from table_update_Nei_Neo import *
from comparison_with_nutriscore import *
import matplotlib.pyplot as plt
from sklearn import metrics
from plots import *
# converts excel dataset to pandas
food_dataset = pd.read_csv("chocolate_dataset.csv")

print(food_dataset['Nutriscore'].value_counts())


# creates two new columns in the dataset: Nei and Neo
food_dataset = table_update_scores(food_dataset)
food_dataset = table_update_scores_a_e(food_dataset)
food_dataset = table_update_scores_a_e_nutriscore(food_dataset)

# prints the updated dataset
print("updated dataset", food_dataset)
# Saves it in a csv file
food_dataset.to_csv("dataset_filled_Part4.csv", index=False)

# compares the two new scores with the nutriscore
Neo_compared_to_nutriscore = Neo_compared_to_nutriscore(food_dataset)
Nei_compared_to_nutriscore = Nei_compared_to_nutriscore(food_dataset)
Neo_compared_to_Nei = Neo_compared_to_Nei(food_dataset)

print("Neo is greater than nutriscore",
      Neo_compared_to_nutriscore["greater"] / len(food_dataset.index), "times")
print("Neo is equal to nutriscore",
      Neo_compared_to_nutriscore["equal"] / len(food_dataset.index), "times")
print("Neo is lower than nutriscore",
      Neo_compared_to_nutriscore["lower"] / len(food_dataset.index), "times")


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

# Plots for visualisation

point_distribution(food_dataset)
score_distribution(food_dataset)
confusion_matrix(food_dataset)
nutrient_distribution(food_dataset)
