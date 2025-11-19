import csv 
import pandas as pd

class Load_CSV_To_DataFrame: 
    def __init__(self,path):
        file_loaded = pd.read_csv(path)
        df = pd.DataFrame(file_loaded)
        self.df = df

    def avg(self, catagory):
        df = self.df
        df = df[catagory]
        
        return df.mean().round(2)
    
    def median(self, catagory):
        df = self.df
        df = df[catagory]
        return df.median().round(2)
    
    def min(self, catagory):
        df = self.df
        df = df[catagory]
        return df.min().round(2)
    
    def max(self, catagory):
        df = self.df
        df = df[catagory]
        return df.max().round(2)
    
    def proportion_of(self, catagory,identafier):
        df = self.df
        df = df[catagory]
        df_count = df.value_counts()
        df_count = df_count.get(identafier)
        df_sum = df.count()
        df_prop = df_count/df_sum
        return df_prop

        


