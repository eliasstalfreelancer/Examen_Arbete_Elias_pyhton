import numpy as np
import pandas as pd
import src.io_utils as io
from datetime import datetime

def simulation(amount_of_people,p_ratio,seed_for_rng = 42 ) -> pd.DataFrame:
    np.random.seed(seed_for_rng) #42 is the meaning of universe
    true_p = p_ratio

    outcome_A = np.random.binomial(n=1,p=true_p,size=amount_of_people)

    current_date = datetime.today().strftime('%Y-%m-%d')
    
    ids = range(amount_of_people)

    df = pd.DataFrame({
        "outcome" :np.concatenate([outcome_A]),
        "id" : ids
    })

    return df



