import matplotlib.pyplot as plt
import pandas as pd
import numpy

def scater(RL, df, index_1="age", index_2="systolic_bp", index_3="weights",
           name_x="Ålder", name_y="Systoliskt blodtryck",
           title="Relation mellan blodtryck och ålder", line_name="Regression"):
    """
    Ritar ett scatter-diagram (spridningsdiagram) tillsammans med en 
    regressionslinje som baseras på resultaten från en linjär regression.

    Parametrar
    ----------
    RL : dict
        Resultatet av linjär regression (Intercept + slopes).
    df : pandas.DataFrame
        Dataset som används för visualiseringen.
    index_1 : str
        Kolumn som används som x-axel (t.ex. ålder).
    index_2 : str
        Kolumn för y-axeln (t.ex. systoliskt blodtryck).
    index_3 : str
        Kolumn som används för att beräkna medelvärde när regressionen ritas.
    name_x : str
        Etikett för x-axeln.
    name_y : str
        Etikett för y-axeln.
    title : str
        Titel för grafen.
    line_name : str
        Namn på regressionslinjen i legend.

    Returnerar
    ----------
    None
        Visar grafen på skärmen.
    """

    b0 = RL["Intercept"]
    b1 = RL["Slope_age"]
    b2 = RL["Slope_weight"]

    dfVaule_1 = df[index_1].values
    dfVaule_2 = df[index_2].values
    dfVaule_3 = df[index_3].values

    avg_dfVaule_3 = dfVaule_3.mean()

    # Beräknar regressionslinjen
    reg_line = b0 + b1 * dfVaule_1 + b2 * avg_dfVaule_3

    plt.scatter(dfVaule_1, dfVaule_2)
    plt.plot(dfVaule_1, reg_line, label=line_name, color="black")
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()


def histogram(df, column, name):
    """
    Ritar ett histogram för en vald kolumn.

    Parametrar
    ----------
    df : pandas.DataFrame
        Datasetet.
    column : str
        Kolumn som ska visualiseras.
    name : str
        Titel / beskrivning av grafen.

    Returnerar
    ----------
    None
    """

    plt.hist(df[column])
    plt.xlabel(column)
    plt.ylabel("Frekvens")
    plt.title(f"Histogram över {name}")
    plt.grid(axis="y")
    plt.show()


def box(df, column, by, title=None, x_label=None, y_label=None):
    """
    Ritar en boxplot grupperad efter en annan kolumn (t.ex. kön).

    Parametrar
    ----------
    df : pandas.DataFrame
        Datasetet.
    column : str
        Kolumn som ska box-plottas.
    by : str
        Kolumn att gruppera efter.
    title : str
        Titel på diagrammet.
    x_label : str
        Etikett för x-axeln.
    y_label : str
        Etikett för y-axeln.

    Returnerar
    ----------
    None
    """

    df.boxplot(column=column, by=by)
    plt.title(title)
    plt.suptitle("")  # Tar bort default-subtitle
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def count_vaule_bar(df, column, name):
    """
    Ritar ett stapeldiagram baserat på antal förekomster i en kolumn.

    Parametrar
    ----------
    df : pandas.DataFrame
        Datasetet.
    column : str
        Kolumnen som ska räknas.
    name : str
        Titel på grafen.

    Returnerar
    ----------
    None
    """
    df[column].value_counts().plot(kind="bar")
    plt.title(name)
    plt.grid(axis="y")
    plt.show()


def bar(df, name):
    """
    Ritar ett generellt stapeldiagram från en DataFrame med två kolumner.

    Parametrar
    ----------
    df : pandas.DataFrame
        En DataFrame med två värden att plottas.
    name : str
        Titel på stapeldiagrammet.

    Returnerar
    ----------
    None
    """
    df.plot(kind="bar")
    plt.title(name)
    plt.grid(axis="y")
    plt.show()
