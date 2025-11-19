import matplotlib.pyplot as plt
import pandas as pd
import numpy




def histogram(df:pd.DataFrame,column:str,name:str):
    plt.hist(df[column])
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {name}")
    plt.grid(axis="y")
    plt.show()

def box(df:pd.DataFrame,column:str,by:str,title:str = None,x_label:str = None,y_label:str = None):
    df.boxplot(column=column,by=by)
    plt.title(title)
    plt.suptitle("")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def count_vaule_bar(df:pd.DataFrame,column:str,name:str):
    df[column].value_counts().plot(kind="bar")
    plt.title(name)
    plt.grid(axis="y")
    plt.show()

def bar(df:pd.DataFrame,name:str):
    df.plot(kind = "bar")
    plt.title(name)
    plt.grid(axis="y")
    plt.show()