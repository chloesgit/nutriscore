import pandas as pd
from nutriscore_points import *
from xlsx_to_pandas import *
from Nei import *
from Neo import *
from table_update_Nei_Neo import *
from comparison_with_nutriscore import *

# converts excel dataset to pandas
food_dataset = convert_excel_to_graph("food_dataset.xlsx")


print(food_dataset)

# computes Neo score for one food item
print("Neo", Neo("Barres croustillantes tout chocolat", food_dataset))

# computes 30-Neo score and a to e classification for one food item
print("score Neo", score_Neo("Barres croustillantes tout chocolat", food_dataset),
      a_e_score_Neo(
    "Barres croustillantes tout chocolat", food_dataset))

# computes Nei score for one food item
print("Nei", Nei("Barres croustillantes tout chocolat", food_dataset))
# computes 20-Nei score and a to e classification for one food item
print("score Nei", score_Nei("Barres croustillantes tout chocolat", food_dataset), a_e_score_Nei(
    "Barres croustillantes tout chocolat", food_dataset))

# creates two new columns in the dataset: Nei and Neo
food_dataset = table_update(food_dataset)
print("updated dataset", food_dataset)

# compares the two new scores with the nutriscore
Neo_compared_to_nutriscore = Neo_compared_to_nutriscore(food_dataset)
Nei_compared_to_nutriscore = Nei_compared_to_nutriscore(food_dataset)

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
