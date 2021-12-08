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
    class2 = np.where(df['class4']!= 'nonevent', True, False)
    df.insert(0, 'class2', class2)


    df = df.drop(["id","partlybad"],axis=1)

    # reduce CO2 features
    CO2_mean = df['CO2168.mean']
    CO2_std = df['CO2168.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('CO2')])
    df['CO2.mean'] = CO2_mean
    df['CO2_std'] = CO2_std

    # reduce radiation features
    radiation = df['RGlob.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith(('Glob','NET','PAR','RGlob','RPAR','UV'))])
    df['radiation'] = radiation

    # reduce H2O features
    H2O_mean = df['H2O168.mean']
    H2O_std = df['H2O168.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('H2O')])
    df['H2O.mean'] = H2O_mean
    df['H2O.std'] = H2O_std

    # reduce NO and NOx features
    NO_mean = df['NO504.mean']
    NO_std = df['NO84.std']
    NOx_mean = df['NOx336.mean']
    NOx_std = df['NOx84.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('NO')])
    df['NO.mean'] = NO_mean
    df['NO.std'] = NO_std
    df['NOx.mean'] = NOx_mean
    df['NOx.std'] = NOx_std

    # reduce O3 features
    O3_mean = df['O384.mean']
    O3_std = df['O3168.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('O3')])
    df['O3.mean'] = O3_mean
    df['O3.std'] = O3_std

    # reduce RHIRGA features
    RHIRGA = df['RHIRGA42.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('RHIRGA')])
    df['RHIRGA'] = RHIRGA

    # rename SO2 features
    df = df.rename(columns={"SO2168.mean": "SO2.mean", "SO2168.std": "SO2.std"})

    # reduce SWS features
    SWS = df['SWS.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('SWS')])
    df['SWS'] = SWS

    # reduce T features
    T_mean = df['T84.mean']
    T_std = df['T84.std']
    df = df.drop(columns=df.columns[df.columns.str.startswith('T')])
    df['T.mean'] = T_mean
    df['T.std'] = T_std

    return(df)