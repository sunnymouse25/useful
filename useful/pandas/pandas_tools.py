import pandas as pd
import numpy as np

def pivot_2d(df, col1, col2):
    '''
    Makes simple 2-dimensional pivot table with counts. 
    col1 will be rows, col2 - columns
    '''   
    y = df.groupby([col1,col2]).size().reset_index(name='counts')
    z = y.pivot(index = col1, columns = col2, values = 'counts')
    return z