import glob
import numpy as pd
import pandas as pd
import os
import numpy as np
from ast import literal_eval

def dump1dtocsv(mename, melist, verbose=True):
    if mename not in melist:
        raise Exception('Monitoring element name does not exist')
       
    if not os.path.exists('./proc_data'):
        os.makedirs('./proc_data')
    
    all_files = glob.glob('data/DF2017*_1D_Complete/ZeroBias_2017*_DataFrame_1D*.csv')
    fname = './proc_data/ZeroBias_2017UL_DataFrame_' + mename + '.csv'
    dflist=[]
    
    print('Dumping {} histograms into {}'.format(mename, fname))
    
    for i, filename in enumerate(all_files):
#         print('Adding file {}'.format(filename))
        if verbose:
            print('Adding file {} ({}/{})'.format(filename, i+1, len(all_files)))
        dfi = pd.read_csv(filename, index_col=None)
    #select your histogram here, metype == 6 for 2D histograms and < 6 for 1D
        dfclean = dfi.loc[(dfi['metype'] <= 5) & (dfi['hname'] == mename),['fromrun','fromlumi','hname','histo','entries','Xmax','Xmin','Xbins','metype']]
        dflist.append(dfclean)

    df = pd.concat(dflist, axis=0, ignore_index=True)


    df_tmp = df[['fromrun','fromlumi','hname','entries','Xmax','Xmin','Xbins','metype']].copy()

    df_tmp['histo'] = df['histo'].apply(literal_eval)#.apply(lambda x: x[1:-1]) #eval the string and cut the first and last value which correspond to Underflow and Overflow

#     print(df_tmp.head())

    
    print('Saved {} histograms to {}'.format(mename, fname))
    df_tmp.to_csv(fname)

    
    # array[array == 0] = 1
def normalizeME(ME, emptyto0=True):
    summation = ME.sum(axis=1, keepdims=True)
    
    if not emptyto0:
        return ME / summation
    
    summation[summation == 0] = 1
    return ME / summation
    
def normalizeMEs(MEs, filterruns=True, emptyto0=True):
    MEs_norm = []
    
    if not filterruns:
        for ME in MEs:
            MEs_norm.append(normalizeME(ME, emptyto0))
        return(np.array(MEs_norm))
                            
    for ME in MEs:
        if not(0 in ME.sum(axis=1, keepdims = True)):
            MEs_norm.append(normalizeME(ME))
        else:
            return None
    return(np.array(MEs_norm))
        
    
    
