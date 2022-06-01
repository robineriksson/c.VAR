import numpy as np
import pandas as pd
import pymc as pm
import matplotlib.pyplot as plt

# get Uppsala data
d = pd.read_csv('../data/C19.csv',sep=',')
d_upp = d[['date','Uppsala','compartment']]

# reorganize to a matrix format
Dinc = d_upp.loc[d_upp.compartment == 'Dinc','Uppsala'].to_numpy()
H = d_upp.loc[d_upp.compartment == 'H','Uppsala'].to_numpy()
W = d_upp.loc[d_upp.compartment == 'W','Uppsala'].to_numpy()
Icum = d_upp.loc[d_upp.compartment == 'Icum','Uppsala'].to_numpy()
date = d_upp.loc[d_upp.compartment == 'Icum','date'].to_numpy()

c19 = pd.DataFrame({'date':date,'Dinc':Dinc,'H': H,'W': W,'Icum':Icum})
