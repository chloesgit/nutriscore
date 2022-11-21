def sugar_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Sugars"].item()
    if dataset_fooditem <= 4.5:
        return (0)
    if dataset_fooditem <= 9:
        return (1)
    if dataset_fooditem <= 13.5:
        return (2)
    if dataset_fooditem <= 18:
        return (3)
    if dataset_fooditem <= 22.5:
        return (4)
    if dataset_fooditem <= 27:
        return (5)
    if dataset_fooditem <= 31:
        return (6)
    if dataset_fooditem <= 36:
        return (7)
    if dataset_fooditem <= 40:
        return (8)
    if dataset_fooditem <= 45:
        return (9)
    if dataset_fooditem > 45:
        return (10)


def energy_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Energy"].item()

    if dataset_fooditem <= 335:
        return (0)
    if dataset_fooditem <= 670:
        return (1)
    if dataset_fooditem <= 1005:
        return (2)
    if dataset_fooditem <= 1340:
        return (3)
    if dataset_fooditem <= 1675:
        return (4)
    if dataset_fooditem <= 2010:
        return (5)
    if dataset_fooditem <= 2345:
        return (6)
    if dataset_fooditem <= 2680:
        return (7)
    if dataset_fooditem <= 3015:
        return (8)
    if dataset_fooditem <= 3350:
        return (9)
    if dataset_fooditem > 3350:
        return (10)


def saturated_fat_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Saturated fatty acids"].item()
    if dataset_fooditem <= 1:
        return (0)
    if dataset_fooditem <= 2:
        return (1)
    if dataset_fooditem <= 3:
        return (2)
    if dataset_fooditem <= 4:
        return (3)
    if dataset_fooditem <= 5:
        return (4)
    if dataset_fooditem <= 6:
        return (5)
    if dataset_fooditem <= 7:
        return (6)
    if dataset_fooditem <= 8:
        return (7)
    if dataset_fooditem <= 9:
        return (8)
    if dataset_fooditem <= 10:
        return (9)
    if dataset_fooditem > 10:
        return (10)


def salt_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Salt"].item()
    if dataset_fooditem <= 0.09:
        return (0)
    if dataset_fooditem <= 0.18:
        return (1)
    if dataset_fooditem <= 0.27:
        return (2)
    if dataset_fooditem <= 0.36:
        return (3)
    if dataset_fooditem <= 0.45:
        return (4)
    if dataset_fooditem <= 0.54:
        return (5)
    if dataset_fooditem <= 0.63:
        return (6)
    if dataset_fooditem <= 0.72:
        return (7)
    if dataset_fooditem <= 0.81:
        return (8)
    if dataset_fooditem <= 0.9:
        return (9)
    if dataset_fooditem > 0.9:
        return (10)


def fruit_veg_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Fruit/vegetable"].item()
    if dataset_fooditem <= 40:
        return (0)
    if dataset_fooditem <= 60:
        return (1)
    if dataset_fooditem <= 80:
        return (2)
    if dataset_fooditem < 80:
        return (5)


def protein_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Proteins"].item()

    if dataset_fooditem <= 1.6:
        return (0)
    if dataset_fooditem <= 3.2:
        return (1)
    if dataset_fooditem <= 4.8:
        return (2)
    if dataset_fooditem <= 6.4:
        return (3)
    if dataset_fooditem <= 8:
        return (4)
    if dataset_fooditem > 8:
        return (5)


def fiber_points(food_item, food_dataset):
    dataset_fooditem = food_dataset[food_dataset["name"]
                                    == food_item]["Fiber"].item()

    if dataset_fooditem <= 0.9:
        return (0)
    if dataset_fooditem <= 1.9:
        return (1)
    if dataset_fooditem <= 2.8:
        return (2)
    if dataset_fooditem <= 3.7:
        return (3)
    if dataset_fooditem <= 4.7:
        return (4)
    if dataset_fooditem > 4.7:
        return (5)
