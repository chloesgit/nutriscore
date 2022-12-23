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


# Plots the score distribution for each index
def score_distribution(food_dataset):
    # distribution histogram for Neo score
    hist = food_dataset['Neo_score'].sort_values().hist()
    plt.xlabel('Neo_score')
    plt.ylabel('Number of products')
    plt.title("Number of produits per Neo category")
    plt.savefig("pandas_hist_Neo_score.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nei score
    hist = food_dataset['Nei_score'].sort_values().hist()
    plt.xlabel('Nei')
    plt.ylabel('Number of products')
    plt.title("Number of produits per Nei category")
    plt.savefig("pandas_hist_Nei_score.png", bbox_inches='tight', dpi=100)
    plt.close()
    # distribution histogram for Nutriscore
    hist = food_dataset['Nutriscore'].sort_values().hist()
    plt.xlabel('Nutriscore')
    plt.ylabel('Number of products')
    plt.title("Number of produits per Nutriscore category")
    plt.savefig("pandas_hist_Nutriscore_score.png",
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
    print(food_dataset["Nei"].value_counts())

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
