import matplotlib.pyplot as plt
from sklearn import metrics

# Plots the point distribution for each index


def point_distribution(food_dataset):
    # distribution histogram for Neo
    hist = food_dataset['Neo'].sort_values().hist()
    plt.xlabel('Neo')
    plt.ylabel('Number of products')
    plt.title("Neo distribution")
    plt.savefig("pandas_hist_Neo.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nei
    hist = food_dataset['Nei'].sort_values().hist()
    plt.xlabel('Nei')
    plt.ylabel('Number of products')
    plt.title("Nei distribution")
    plt.savefig("pandas_hist_Nei.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nutriscore points
    hist = food_dataset['Nutriscore_point'].sort_values().hist()
    plt.xlabel('Nutriscore')
    plt.ylabel('Number of products')
    plt.title("Nutriscore distribution")
    plt.savefig("pandas_hist_Nutriscore.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nutriscore points
    hist = food_dataset['NewNeo'].sort_values().hist()
    plt.xlabel('New Neo')
    plt.ylabel('Number of products')
    plt.title("New Neo distribution")
    plt.savefig("pandas_hist_NewNeo.png", bbox_inches='tight', dpi=100)
    plt.close()


# Plots the score distribution for each index
def score_distribution(food_dataset):
    # distribution histogram for Neo score
    hist = food_dataset['Neo_score'].sort_values().hist()
    plt.xlabel('Neo_score')
    plt.ylabel('Number of products')
    plt.title("Number of products per Neo category")
    plt.savefig("pandas_hist_Neo_score.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nei score
    hist = food_dataset['Nei_score'].sort_values().hist()
    plt.xlabel('Nei')
    plt.ylabel('Number of products')
    plt.title("Number of products per Nei category")
    plt.savefig("pandas_hist_Nei_score.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nutriscore
    hist = food_dataset['Nutriscore'].sort_values().hist()
    plt.xlabel('Nutriscore')
    plt.ylabel('Number of products')
    plt.title("Number of products per Nutriscore category")
    plt.savefig("pandas_hist_Nutriscore_score.png",
                bbox_inches='tight', dpi=100)
    plt.close()
    hist = food_dataset['NewNeo_score'].sort_values().hist()
    plt.xlabel('New Neo score')
    plt.ylabel('Number of products')
    plt.title("Number of products per New Neo category")
    plt.savefig("pandas_hist_NewNeo_score.png",
                bbox_inches='tight', dpi=100)
    plt.close()


# Plots confusion matrix of the new scores vs nutriscore
def confusion_matrix(food_dataset):
    # Confusion matrix between Neo and Nutriscore
    confusion_matrix = metrics.confusion_matrix(
        food_dataset['Nutriscore'], food_dataset['Neo_score'])

    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=["a", "b", "c", "d", "e"])
    cm_display.plot()
    plt.title("Confusion matrix between Nutriscore and Neo")
    plt.ylabel("Nutriscore")
    plt.xlabel("Neo")
    plt.savefig("confusion_matrix_Neo.png", bbox_inches='tight', dpi=100)
    plt.close()
    # Confusion matrix between Neo and Nutriscore with redefined labels
    confusion_matrix = metrics.confusion_matrix(
        food_dataset['Nutriscore_new_score'], food_dataset['Neo_score'])

    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=["a", "b", "c", "d", "e"])
    cm_display.plot()
    plt.title("Confusion matrix between Nutriscore and Neo")
    plt.ylabel("New nutriscore")
    plt.xlabel("Neo")
    plt.savefig("confusion_matrix_Neo_new_Nutriscore.png",
                bbox_inches='tight', dpi=100)
    plt.close()
    # Confusion matrix between Nei and Nutriscore

    confusion_matrix = metrics.confusion_matrix(
        food_dataset['Nutriscore'], food_dataset['Nei_score'])

    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=["a", "b", "c", "d", "e"])
    cm_display.plot()
    plt.title("Confusion matrix between Nutriscore and Nei")
    plt.ylabel("Nutriscore")
    plt.xlabel("Nei")
    plt.savefig("confusion_matrix_Nei_Nutriscore.png",
                bbox_inches='tight', dpi=100)
    plt.close()
    confusion_matrix = metrics.confusion_matrix(
        food_dataset['Neo_score'], food_dataset['NewNeo_score'])

    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=["a", "b", "c", "d", "e"])
    cm_display.plot()
    plt.title("Confusion matrix between Neo and New Neo")
    plt.ylabel("Neo")
    plt.xlabel("New Neo")
    plt.savefig("confusion_matrix_Neo_NewNeo.png",
                bbox_inches='tight', dpi=100)
    plt.close()
    confusion_matrix = metrics.confusion_matrix(
        food_dataset['Nutriscore'], food_dataset['NewNeo_score'])

    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=["a", "b", "c", "d", "e"])
    cm_display.plot()
    plt.title("Confusion matrix between Nutriscore and New Neo")
    plt.ylabel("Nutriscore")
    plt.xlabel("New Neo")
    plt.savefig("confusion_matrix_Nutriscore_NewNeo.png",
                bbox_inches='tight', dpi=100)
    plt.close()


def nutrient_distribution(food_dataset):
    # distribution histogram for Neo
    hist = food_dataset['Energy'].sort_values().hist()
    plt.xlabel('Energy')
    plt.ylabel('Number of products')
    plt.title("Energy distribution")
    plt.savefig("Energy.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nei
    hist = food_dataset['Saturated_fatty_acids'].sort_values().hist()
    plt.xlabel('Saturated_fatty_acids')
    plt.ylabel('Number of products')
    plt.title("Saturated_fatty_acids distribution")
    plt.savefig("Saturated_fatty_acids.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nutriscore points
    hist = food_dataset['Sugars'].sort_values().hist()
    plt.xlabel('Sugars')
    plt.ylabel('Number of products')
    plt.title("Sugars distribution")
    plt.savefig("Sugars.png", bbox_inches='tight', dpi=100)
    plt.close()
    hist = food_dataset['Fiber'].sort_values().hist()
    plt.xlabel('Fiber')
    plt.ylabel('Number of products')
    plt.title("Fiber distribution")
    plt.savefig("Fiber.png", bbox_inches='tight', dpi=100)
    plt.close()
    hist = food_dataset['Proteins'].sort_values().hist()
    plt.xlabel('Proteins')
    plt.ylabel('Number of products')
    plt.title("Proteins distribution")
    plt.savefig("Proteins.png", bbox_inches='tight', dpi=100)
    plt.close()
    hist = food_dataset['Salt'].sort_values().hist()
    plt.xlabel('Salt')
    plt.ylabel('Number of products')
    plt.title("Salt distribution")
    plt.savefig("Salt.png", bbox_inches='tight', dpi=100)
    plt.close()
    hist = food_dataset['Fruit/vegetable'].sort_values().hist()
    plt.xlabel('Fruit/vegetable')
    plt.ylabel('Number of products')
    plt.title("Fruit/vegetable distribution")
    plt.savefig("Fruitvegetable.png", bbox_inches='tight', dpi=100)
    plt.close()
