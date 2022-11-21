import pandas as pd


def convert_excel_to_graph(file_name):
    excelFile = pd.read_excel(file_name)
    excelFile.to_csv("file_to_csv.csv")
    dataframeObject = pd.DataFrame(pd.read_csv("file_to_csv.csv"))
    return dataframeObject
