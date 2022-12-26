# Description: This file contains the functions that calculate the points for each nutrient

def sugar_points(sugar_value, dataset):
    if sugar_value <= dataset["Sugars"].quantile(0.1):
        return (1)
    if sugar_value <= dataset["Sugars"].quantile(0.2):
        return (2)
    if sugar_value <= dataset["Sugars"].quantile(0.3):
        return (3)
    if sugar_value <= dataset["Sugars"].quantile(0.4):
        return (4)
    if sugar_value <= dataset["Sugars"].quantile(0.5):
        return (5)
    if sugar_value <= dataset["Sugars"].quantile(0.6):
        return (6)
    if sugar_value <= dataset["Sugars"].quantile(0.7):
        return (7)
    if sugar_value <= dataset["Sugars"].quantile(0.8):
        return (8)
    if sugar_value <= dataset["Sugars"].quantile(0.9):
        return (9)
    if sugar_value > dataset["Sugars"].quantile(0.9):
        return (10)


def energy_points(energy_value, dataset):
    if energy_value <= dataset["Energy"].quantile(0.1):
        return (1)
    if energy_value <= dataset["Energy"].quantile(0.2):
        return (2)
    if energy_value <= dataset["Energy"].quantile(0.3):
        return (3)
    if energy_value <= dataset["Energy"].quantile(0.4):
        return (4)
    if energy_value <= dataset["Energy"].quantile(0.5):
        return (5)
    if energy_value <= dataset["Energy"].quantile(0.6):
        return (6)
    if energy_value <= dataset["Energy"].quantile(0.7):
        return (7)
    if energy_value <= dataset["Energy"].quantile(0.8):
        return (8)
    if energy_value <= dataset["Energy"].quantile(0.9):
        return (9)
    if energy_value > dataset["Energy"].quantile(0.9):
        return (10)


def saturated_fat_points(saturated_fat_value, dataset):
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.1):
        return (1)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.2):
        return (2)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.3):
        return (3)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.4):
        return (4)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.5):
        return (5)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.6):
        return (6)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.7):
        return (7)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.8):
        return (8)
    if saturated_fat_value <= dataset["Saturated_fatty_acids"].quantile(0.9):
        return (9)
    if saturated_fat_value > dataset["Saturated_fatty_acids"].quantile(0.9):
        return (10)


def salt_points(salt_value, dataset):
    if salt_value <= dataset["Salt"].quantile(0.1):
        return (1)
    if salt_value <= dataset["Salt"].quantile(0.2):
        return (2)
    if salt_value <= dataset["Salt"].quantile(0.3):
        return (3)
    if salt_value <= dataset["Salt"].quantile(0.4):
        return (4)
    if salt_value <= dataset["Salt"].quantile(0.5):
        return (5)
    if salt_value <= dataset["Salt"].quantile(0.6):
        return (6)
    if salt_value <= dataset["Salt"].quantile(0.7):
        return (7)
    if salt_value <= dataset["Salt"].quantile(0.8):
        return (8)
    if salt_value <= dataset["Salt"].quantile(0.9):
        return (9)
    if salt_value > dataset["Salt"].quantile(0.9):
        return (10)


def fruit_veg_points(fruit_veg_value, dataset):
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.1):
        return (1)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.2):
        return (2)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.3):
        return (3)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.4):
        return (4)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.5):
        return (5)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.6):
        return (6)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.7):
        return (7)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.8):
        return (8)
    if fruit_veg_value <= dataset["Fruit/vegetable"].quantile(0.9):
        return (9)
    if fruit_veg_value > dataset["Fruit/vegetable"].quantile(0.9):
        return (10)


def protein_points(protein_value, dataset):
    if protein_value <= dataset["Proteins"].quantile(0.1):
        return (1)
    if protein_value <= dataset["Proteins"].quantile(0.2):
        return (2)
    if protein_value <= dataset["Proteins"].quantile(0.3):
        return (3)
    if protein_value <= dataset["Proteins"].quantile(0.4):
        return (4)
    if protein_value <= dataset["Proteins"].quantile(0.5):
        return (5)
    if protein_value <= dataset["Proteins"].quantile(0.6):
        return (6)
    if protein_value <= dataset["Proteins"].quantile(0.7):
        return (7)
    if protein_value <= dataset["Proteins"].quantile(0.8):
        return (8)
    if protein_value <= dataset["Proteins"].quantile(0.9):
        return (9)
    if protein_value > dataset["Proteins"].quantile(0.9):
        return (10)


def fiber_points(fiber_value, dataset):
    if fiber_value <= dataset["Fiber"].quantile(0.1):
        return (1)
    if fiber_value <= dataset["Fiber"].quantile(0.2):
        return (2)
    if fiber_value <= dataset["Fiber"].quantile(0.3):
        return (3)
    if fiber_value <= dataset["Fiber"].quantile(0.4):
        return (4)
    if fiber_value <= dataset["Fiber"].quantile(0.5):
        return (5)
    if fiber_value <= dataset["Fiber"].quantile(0.6):
        return (6)
    if fiber_value <= dataset["Fiber"].quantile(0.7):
        return (7)
    if fiber_value <= dataset["Fiber"].quantile(0.8):
        return (8)
    if fiber_value <= dataset["Fiber"].quantile(0.9):
        return (9)
    if fiber_value > dataset["Fiber"].quantile(0.9):
        return (10)
