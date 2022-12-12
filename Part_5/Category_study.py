import matplotlib.pyplot as plt
import pandas as pd
from ELECTRE_Tri import OptimisticElectreSorting,PessimisticElectreSorting
from Models_comparison import extract_original_score

final_dataset = "Part_6/chocolate_dataset.csv"

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

def find_category_names(score,total_score,cat):
    cat_names = []
    for i in range(len(score)):
        if score[i][1] == cat:
            cat_names.append(total_score['name'][i])
    return cat_names

def find_category_stats(score,total_score,cat):
    cat_stats = {}
    category_size = 0
    for crit in criteria:
        cat_stats[crit] = 0

    for i in range(len(score)):
        if score[i][1] == cat:
            category_size +=1
            for crit in criteria:
                cat_stats[crit] += (total_score[crit][i])
    
    for crit in criteria:
        cat_stats[crit] = round(cat_stats[crit]/category_size,3)
        
    return cat_stats

def find_category_Y(cat_stats):
    Y = []
    for crit in criteria:
        Y.append(cat_stats[crit])
    return Y

def overview_categories(score,total_score):
    categories = ['a','b','c','d','e']
    results = {}

    for cat in categories:
        cat_names = find_category_names(score,total_score,cat),
        cat_stats = find_category_stats(score,total_score,cat)
        Y = find_category_Y(cat_stats)

        results[cat] = {
            "names": cat_names,
            "stats": cat_stats,
            "Y": Y
        }

    return results

def compare_categories(results,title="Average value by criterion"):
    X = [i for i in range(len(criteria))]

    for cat in results.keys():
        plt.plot(X[1:],results[cat]["Y"][1:],label=cat)

    plt.title(title)
    plt.legend()
    plt.show()  

def generate_categories_results(scores):
    lines = pd.read_csv(final_dataset)
    Results = []
    for (label,score) in scores:
        total_data = pd.read_csv(final_dataset)
        total_data[label] = [d[1] for d in score]
        results = overview_categories(score,total_data)
        Results.append(results)
    return Results

def total_categories_comparison(lines,data,criteria,weights,limiting_profiles,threshold):
    Scores = [
        ('Nutriscore',extract_original_score(lines)), #Nutriscore
        ('Part_5 model',PessimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold)),
        ('Part_5 model',OptimisticElectreSorting(data,criteria,weights,limiting_profiles,threshold))
    ]
    names = ['Nutriscore','Pessimistic','Optimistic']

    Results = generate_categories_results(Scores)

    for i,results in enumerate(Results):
        compare_categories(results,"Average value by criterion for model "+names[i])

    # Nutriscore v Pessimistic

    Pessimistic_vs_Nutriscore = {
        "Category A from Pessimistic": Results[1]["a"],
        "Category E from Pessimistic": Results[1]["e"],
        "Category A from original Nutriscore": Results[0]["a"],
        "Category E from original Nutriscore": Results[0]["e"],
    }
    compare_categories(Pessimistic_vs_Nutriscore,"Average value of A and E categories by criterion\n for models Pessimistic and Nutriscore")

    # Optimistic v Pessimistic
    Optimistic_vs_Nutriscore = {
        "Category A from Pessimistic": Results[1]["a"],
        "Category E from Pessimistic": Results[1]["e"],
        "Category A from Optimistic": Results[2]["a"],
        "Category E from Optimistic": Results[2]["e"],
    }
    compare_categories(Optimistic_vs_Nutriscore,"Average value of A and E categories by criterion\n for models Pessimistic and Optimistic")
