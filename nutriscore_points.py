def sugar_points(sugar_value):
    if sugar_value <= 4.5:
        return (0)
    if sugar_value <= 9:
        return (1)
    if sugar_value <= 13.5:
        return (2)
    if sugar_value <= 18:
        return (3)
    if sugar_value <= 22.5:
        return (4)
    if sugar_value <= 27:
        return (5)
    if sugar_value <= 31:
        return (6)
    if sugar_value <= 36:
        return (7)
    if sugar_value <= 40:
        return (8)
    if sugar_value <= 45:
        return (9)
    if sugar_value > 45:
        return (10)


def energy_points(energy_value):
    if energy_value <= 335:
        return (0)
    if energy_value <= 670:
        return (1)
    if energy_value <= 1005:
        return (2)
    if energy_value <= 1340:
        return (3)
    if energy_value <= 1675:
        return (4)
    if energy_value <= 2010:
        return (5)
    if energy_value <= 2345:
        return (6)
    if energy_value <= 2680:
        return (7)
    if energy_value <= 3015:
        return (8)
    if energy_value <= 3350:
        return (9)
    if energy_value > 3350:
        return (10)


def saturated_fat_points(saturated_fat_value):
    if saturated_fat_value <= 1:
        return (0)
    if saturated_fat_value <= 2:
        return (1)
    if saturated_fat_value <= 3:
        return (2)
    if saturated_fat_value <= 4:
        return (3)
    if saturated_fat_value <= 5:
        return (4)
    if saturated_fat_value <= 6:
        return (5)
    if saturated_fat_value <= 7:
        return (6)
    if saturated_fat_value <= 8:
        return (7)
    if saturated_fat_value <= 9:
        return (8)
    if saturated_fat_value <= 10:
        return (9)
    if saturated_fat_value > 10:
        return (10)


def salt_points(salt_value):
    if salt_value <= 0.09:
        return (0)
    if salt_value <= 0.18:
        return (1)
    if salt_value <= 0.27:
        return (2)
    if salt_value <= 0.36:
        return (3)
    if salt_value <= 0.45:
        return (4)
    if salt_value <= 0.54:
        return (5)
    if salt_value <= 0.63:
        return (6)
    if salt_value <= 0.72:
        return (7)
    if salt_value <= 0.81:
        return (8)
    if salt_value <= 0.9:
        return (9)
    if salt_value > 0.9:
        return (10)


def fruit_veg_points(fruit_veg_value):
    if fruit_veg_value <= 40:
        return (0)
    if fruit_veg_value <= 60:
        return (1)
    if fruit_veg_value <= 80:
        return (2)
    if fruit_veg_value >= 80:
        return (5)


def protein_points(protein_value):
    if protein_value <= 1.6:
        return (0)
    if protein_value <= 3.2:
        return (1)
    if protein_value <= 4.8:
        return (2)
    if protein_value <= 6.4:
        return (3)
    if protein_value <= 8:
        return (4)
    if protein_value > 8:
        return (5)


def fiber_points(fiber_value):
    if fiber_value <= 0.9:
        return (0)
    if fiber_value <= 1.9:
        return (1)
    if fiber_value <= 2.8:
        return (2)
    if fiber_value <= 3.7:
        return (3)
    if fiber_value <= 4.7:
        return (4)
    if fiber_value > 4.7:
        return (5)
