import src.io_utils as io
import src.sim as sim
import pandas as pd
import numpy as np
import math 
from scipy.stats import ttest_ind
from sklearn.linear_model import LinearRegression


def summarize_decriptic_statistics(loader):
    """
    Sammanställer beskrivande statistik (medelvärde, median, min och max)
    för utvalda kolumner i datasetet.

    Parametrar
    ----------
    loader : Load_CSV_To_DataFrame
        Objekt som innehåller det laddade datat.

    Returnerar
    ----------
    pandas.DataFrame
        En tabell med beskrivande statistik.
    """
    df = loader.df
    rows = ["age", "weight", "height", "systolic_bp", "cholesterol"]

    summary = pd.DataFrame({
        "mean":   [loader.avg(col) for col in rows],
        "median": [loader.median(col) for col in rows],
        "min":    [loader.min(col) for col in rows],
        "max":    [loader.max(col) for col in rows],
    })
    
    summary.rename(index={nr: rows[nr] for nr in range(len(rows))}, inplace=True)
    return summary


def summarize_confidence_interval(loader, df, collum):
    """
    Beräknar ett konfidensintervall för en vald kolumn genom att använda
    normalapproximationen.

    Parametrar
    ----------
    loader : Load_CSV_To_DataFrame
    df : pandas.DataFrame
    collum : str
        Namnet på kolumnen som ska analyseras.

    Returnerar
    ----------
    tuple
        (nedre_gräns, övre_gräns, medelvärde)
    """
    sum_df = pd.DataFrame(summarize_decriptic_statistics(loader))
    mean = sum_df["mean"].loc[collum]
    return normalapproximation(mean, df[collum])


def proption_of_A_B(A_df: pd.DataFrame, A_col: str, A_name: str,
                    B_df: pd.DataFrame, B_col: str = "outcome",
                    B_name: str = None, rowname=("Inte sjuk", "Sjuk")) -> pd.DataFrame:
    """
    Jämför procentuell fördelning mellan två dataset.

    Parametrar
    ----------
    A_df : pandas.DataFrame
    A_col : str
        Kolumnnamn i dataset A.
    A_name : str
        Namn på kolumnen i resultatet.
    B_df : pandas.DataFrame
    B_col : str
        Kolumnnamn i dataset B.
    B_name : str
        Namn på kolumnen i resultatet.
    rowname : tuple
        Namn för index (t.ex. "Sjuk" / "Inte sjuk").

    Returnerar
    ----------
    pandas.DataFrame
        En tabell med procentuell fördelning från båda dataset.
    """

    A_prop = (A_df[A_col].value_counts(normalize=True) * 100).round(2)
    B_prop = (B_df[B_col].value_counts(normalize=True) * 100).round(2)

    df = pd.DataFrame({A_name: A_prop, B_name: B_prop})
    return df.rename(index={0: rowname[0], 1: rowname[1]})


def disease_simulation_summary(loader):
    """
    Skapar en sammanställning av verklig och simulerad sjukdomsfrekvens.

    Parametrar
    ----------
    loader : Load_CSV_To_DataFrame

    Returnerar
    ----------
    pandas.DataFrame
    """
    r = loader.proportion_of("disease", 1)
    A = loader.df
    B = sim.simulation(1000, r)
    return proption_of_A_B(A, "disease", "IRL (%)", B, B_name="Sim (%)")


def normalapproximation(mean_vaule, df_and_index, confidence=1.95):
    """
    Beräknar ett konfidensintervall med hjälp av normalapproximationen.

    Parametrar
    ----------
    mean_vaule : float
        Medelvärdet av data.
    df_and_index : array-like
        Datapunkter.
    confidence : float
        Multiplikatorn (≈ 1.96 för 95% intervall).

    Returnerar
    ----------
    tuple
        (nedre_gräns, övre_gräns, medelvärde)
    """
    df_and_index = np.array(df_and_index, dtype=float)
    s = float(np.std(df_and_index, ddof=1))
    n = len(df_and_index)

    confidence = confidence + 0.01
    s_sqrt = s / math.sqrt(n)

    lower = mean_vaule - confidence * s_sqrt
    upper = mean_vaule + confidence * s_sqrt
    return float(round(lower, 2)), float(round(upper, 2)), mean_vaule


def t_test(df, collum_1, collum_2):
    """
    Utför ett ensidigt t-test för att jämföra medelvärdet mellan två grupper.

    Parametrar
    ----------
    df : pandas.DataFrame
    collum_1 : str
        Kolumn som definierar grupperna (t.ex. "Yes"/"No").
    collum_2 : str
        Kolumn med värdena som ska jämföras.

    Returnerar
    ----------
    tuple
        (t_värde, p_värde, medel_grupp_a, medel_grupp_b)
    """
    group_a = df[df[collum_1] == "Yes"][collum_2]
    group_b = df[df[collum_1] == "No"][collum_2]

    t_stat, p_value = ttest_ind(group_a, group_b, alternative='greater')
    return t_stat, p_value, group_a.mean(), group_b.mean()


def linijer_regresion(df, x_index_1, x_index_2, y_index):
    """
    Utför en linjär regression med två förklarande variabler.

    Parametrar
    ----------
    df : pandas.DataFrame
    x_index_1 : str
        Första förklaringsvariabeln.
    x_index_2 : str
        Andra förklaringsvariabeln.
    y_index : str
        Målvariabeln (t.ex. systoliskt blodtryck).

    Returnerar
    ----------
    dict
        En sammanställning av intercept, koefficienter, R² och ett exempelvärde.
    """
    X = df[[x_index_1, x_index_2]].values
    Y = df[y_index].values

    linreg = LinearRegression()
    linreg.fit(X, Y)

    output = {
        "Intercept": [float(linreg.intercept_)],
        "Slope_" + x_index_1: float(linreg.coef_[0]),
        "Slope_" + x_index_2: float(linreg.coef_[1]),
        "r2": float(linreg.score(X, Y)),
        "pred_50,70": float(linreg.predict(np.array([[50, 70]]))[0])
    }
    return output
