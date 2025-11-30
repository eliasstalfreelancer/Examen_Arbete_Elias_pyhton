import numpy as np
import pandas as pd
import src.viz as viz



class DiseaseSimulator:
    """
    En klass som hanterar simulering av sjukdomsutfall baserat på den
    verkliga sjukdomssannolikheten i datasetet.

    Klassen kan:
    - räkna ut sannolikheten för sjukdom i det verkliga datat
    - simulera nya personer med samma sannolikhet
    - jämföra simulerad och verklig sjukdomsförekomst
    - skapa stapeldiagram för jämförelsen
    """

    def __init__(self, df):
        """
        Initierar simulatorn med ett DataFrame.

        Parametrar
        ----------
        df : pandas.DataFrame
            Dataset som innehåller kolumnen 'disease'.
        """
        self.df = df

    def ratio(self):
        """
        Beräknar verklig sjukdomsförekomst i datasetet.

        Returnerar
        ----------
        float
            Andelen personer som har sjukdomen.
        """
        return self.df["disease"].mean()

    def simulate(self, n=1000, seed=42):
        """
        Simulerar n personer med sjukdom sannolikheten som hämtats från datasetet.

        Parametrar
        ----------
        n : int
            Antal personer som ska simuleras.
        seed : int
            Frö för slumpgeneratorn (för reproducerbarhet).

        Returnerar
        ----------
        float
            Andelen simulerade personer som får sjukdomen.
        """
        np.random.seed(seed)
        p = self.ratio()
        simulated = np.random.choice([0, 1], size=n, p=[1 - p, p])
        return simulated.mean()

    def compare(self, n=1000):
        """
        Jämför verklig och simulerad sjukdomsförekomst i procent.

        Parametrar
        ----------
        n : int
            Antalet personer som ska simuleras.

        Returnerar
        ----------
        pandas.DataFrame
            Tabell med verklig och simulerad sjukdomsförekomst i procent.
        """
        true = self.ratio()
        sim = self.simulate(n)

        return pd.DataFrame({
            "IRL": [float(((true) * 100).round(2))],
            "Simulated": [float(((sim) * 100).round(2))]
        })

    def bar_chart(self, name):
        """
        Skapar ett stapeldiagram som visualiserar jämförelse mellan
        verklig och simulerad sjukdomsförekomst.

        Parametrar
        ----------
        name : str
            Titel på diagrammet.

        Returnerar
        ----------
        matplotlib-objekt
            Ett stapeldiagram.
        """
        return viz.bar(self.compare(), name)
