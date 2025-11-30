import numpy as np
import pandas as pd
from datetime import datetime

def simulation(amount_of_people, p_ratio, seed_for_rng=42) -> pd.DataFrame:
    """
    Simulerar ett antal personer och deras sjukdomsutfall baserat på en
    given sannolikhet. Används för att jämföra den verkliga
    sjukdomsförekomsten i datasetet med en simulerad population.

    Parametrar
    ----------
    amount_of_people : int
        Antalet personer som ska simuleras.
    p_ratio : float
        Sannolikheten att en person har sjukdomen (t.ex. 0.23).
    seed_for_rng : int
        Frö till slumpgeneratorn för att få reproducerbara resultat.

    Returnerar
    ----------
    pandas.DataFrame
        Ett DataFrame som innehåller två kolumner:
        - "outcome": 1 = sjuk, 0 = frisk
        - "id": unikt ID för varje simulerad person
    """
    np.random.seed(seed_for_rng)

    
    outcome_A = np.random.binomial(n=1, p=p_ratio, size=amount_of_people)

    ids = range(amount_of_people)

    df = pd.DataFrame({
        "outcome": outcome_A,
        "id": ids
    })

    return df
