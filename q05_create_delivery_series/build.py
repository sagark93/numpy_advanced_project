# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution


ipl_matches_array
def create_delivery_series():
    return pd.Series(ipl_matches_array[:, 11]) 
    
    
    
pd.Series(ipl_matches_array[:, 11])
create_delivery_series()

