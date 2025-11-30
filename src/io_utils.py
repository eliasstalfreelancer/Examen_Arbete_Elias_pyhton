import csv 
import pandas as pd

class Load_CSV_To_DataFrame:
    """
    En klass som laddar en CSV-fil till ett pandas DataFrame och tillhandahåller
    hjälpfunktioner för grundläggande statistik.

    Klassen erbjuder:
    - Medelvärde, median, min och max för valfri kolumn
    - Andelsberäkning för en kolumn (t.ex. sjukdomsförekomst)
    """

    def __init__(self, path):
        """
        Läser in en CSV-fil från angiven sökväg och lagrar den som ett DataFrame.

        Parametrar
        ----------
        path : str
            Filvägen till CSV-filen.
        """
        file_loaded = pd.read_csv(path)
        df = pd.DataFrame(file_loaded)
        self.df = df

    def avg(self, catagory):
        """
        Beräknar medelvärdet för en kolumn.

        Parametrar
        ----------
        catagory : str
            Namnet på kolumnen.

        Returnerar
        ----------
        float
            Medelvärdet avrundat till två decimaler.
        """
        df = self.df[catagory]
        return df.mean().round(2)
    
    def median(self, catagory):
        """
        Beräknar medianvärdet för en kolumn.

        Parametrar
        ----------
        catagory : str
            Namnet på kolumnen.

        Returnerar
        ----------
        float
            Medianen avrundad till två decimaler.
        """
        df = self.df[catagory]
        return df.median().round(2)
    
    def min(self, catagory):
        """
        Hämtar minsta värdet i en kolumn.

        Parametrar
        ----------
        catagory : str
            Namnet på kolumnen.

        Returnerar
        ----------
        float
            Det minsta värdet avrundat till två decimaler.
        """
        df = self.df[catagory]
        return df.min().round(2)
    
    def max(self, catagory):
        """
        Hämtar största värdet i en kolumn.

        Parametrar
        ----------
        catagory : str
            Namnet på kolumnen.

        Returnerar
        ----------
        float
            Det största värdet avrundat till två decimaler.
        """
        df = self.df[catagory]
        return df.max().round(2)
    
    def proportion_of(self, catagory, identafier=1):
        """
        Beräknar andelen rader i en kolumn som matchar ett specifikt värde.
        Används exempelvis för att räkna andel sjuka i datasetet.

        Parametrar
        ----------
        catagory : str
            Kolumn som ska analyseras.
        identafier : int eller str
            Det värde som ska kontrolleras (t.ex. 1 = sjuk, 0 = frisk).

        Returnerar
        ----------
        float
            Andelen av kolumnen som matchar värdet.
        """
        df = self.df[catagory]
        df_count = df.value_counts().get(identafier)
        df_sum = df.count()
        df_prop = df_count / df_sum
        return df_prop
