
import src.io_utils as io
import src.sim as sim
import pandas as pd
import numpy as np
import math 
from scipy.stats import ttest_ind



def summarize_decriptic_statistics(loader):
    
    df = loader.df

    rows = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    
    summary = pd.DataFrame({
        "mean" : [loader.avg(col) for col in rows],
        "median" : [loader.median(col) for col in rows],
        "min" : [loader.min(col) for col in rows],
        "max" : [loader.max(col) for col in rows],
    })
    summary.rename(index= {nr : rows[nr] for nr in range(len(rows))},inplace= True)
    return summary

def summarize_confidence_interval(loader,df,collum):
    sum_df = pd.DataFrame(summarize_decriptic_statistics(loader))
    #vet att loc söker rows men jag strukturen blev gallen med summery ovan
    mean = sum_df["mean"].loc[collum]
   
    return normalapproximation(mean,df[collum])


def proption_of_A_B(A_df:pd.DataFrame,A_col:str,A_name:str,B_df:pd.DataFrame,B_col:str="outcome" ,B_name:str=None, rowname = ("Inte sjuk","Sjuk")) -> pd.DataFrame:
    
    #time 100 to get it to percent. probly a better way to do this but it works
    A_prop = (A_df[A_col].value_counts(normalize=True)*100).round(2)
    B_prop = (B_df[B_col].value_counts(normalize=True)*100).round(2)
    df = pd.DataFrame({A_name: A_prop, B_name: B_prop})
    return df.rename(index={0: rowname[0], 1: rowname[1]})


def disease_simulation_summary(loader):
    
    r = loader.proportion_of("disease",1)
    A = loader.df
    B = sim.simulation(1000,r)
    return proption_of_A_B(A,"disease","IRL (%)",B,B_name="Sim (%)")

def normalapproximation(mean_vaule,df_and_index,confidence=1.95):
    
    df_and_index = np.array(df_and_index,dtype= float)
    s = float(np.std(df_and_index,ddof=1))
    n = len(df_and_index)
    
    confidence = confidence + 0.01
    s_sqrt = s /math.sqrt(n)

    lower = mean_vaule - confidence * s_sqrt
    upper = mean_vaule + confidence * s_sqrt
    return float(round(lower,2)), float(round(upper,2)), mean_vaule

def t_test(df,collum_1,collum_2):
    
    group_a = df[df[collum_1] == "Yes"][collum_2]
    group_b = df[df[collum_1] == "No"][collum_2]
    
    t_stat, p_value = ttest_ind(group_a, group_b, alternative='greater') 
    
    return t_stat, p_value, group_a.mean(), group_b.mean()