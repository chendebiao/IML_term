import numpy as np
import pandas as pd

def feature_reduction(df):
    """
    This function reduction features amount from 100 to 23
    """
    df = df.set_index("date")
    

    ## Tell that "class4" is categorical variable. (R does this automatically.)
    df["class4"] = df["class4"].astype("category")

    # add a class 2 column
    class2 = np.where(df['class4']!= 'nonevent', 'event', 'notevent')
    df.insert(0, 'class2', class2)
    df['class2'] = df['class2'].astype("category")


    df = df.drop(["id","partlybad"],axis=1)

    # reduce CO2 features
    CO2_mean = df['CO2168.mean']
    CO2_std = df['CO2168.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('CO2')])
    df['CO2168.mean'] = CO2_mean
    df['CO2168.std'] = CO2_std

    # reduce radiation features
    df = df.drop(columns=df.columns[df.columns.str.startswith(('Glob','NET','RGlob','UV'))])

    # reduce H2O features
    H2O_mean = df['H2O168.mean']
    H2O_std = df['H2O168.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('H2O')])
    df['H2O168.mean'] = H2O_mean
    df['H2O168.std'] = H2O_std

    # reduce NO and NOx features
    NO_mean = df['NO504.mean']
    NOx_mean = df['NOx336.mean']
    df = df.drop(columns=df.columns[df.columns.str.startswith('NO')&df.columns.str.endswith('mean')])
    df['NO504.mean'] = NO_mean
    df['NOx336.mean'] = NOx_mean

    # reduce O3 features
    O3_mean = df['O384.mean']
    O3_std = df['O3168.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('O3')])
    df['O384.mean'] = O3_mean
    df['O3168.std'] = O3_std

    # reduce RHIRGA features
    RHIRGA_mean = df['RHIRGA42.mean']
    RHIRGA_std = df['RHIRGA42.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('RHIRGA')])
    df['RHIRGA42.mean'] = RHIRGA_mean
    df['RHIRGA42.std'] = RHIRGA_std

    # reduce T features
    T_mean = df['T84.mean']
    T_std = df['T84.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('T')])
    df['T84.mean'] = T_mean
    df['T84.std'] = T_std

    return(df)