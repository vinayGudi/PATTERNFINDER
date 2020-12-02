#https://www.youtube.com/watch?v=zBVQvVCZPCM
#https://www.viralml.com/video-content.html?fm=yt&v=zBVQvVCZPCM
import glob
import pandas as pd

files = glob.glob("/home/vinay/Downloads/HDFCDATA/*.csv")
dfs = [pd.read_csv(f, header=None, sep=",") for f in files]

Data = pd.concat(dfs,ignore_index=True)


####################################################################
#making first column as header
Data.columns = Data.iloc[0]
#####################################################################
# Get indexes where name column has value Date
indexNames = Data[Data['Date '] == 'Date '].index
 
# Delete these row indexes from dataFrame
Data.drop(indexNames , inplace=True)
########################################################################

%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import io, base64, os, json, re 
import pandas as pd
import numpy as np
import datetime
import warnings
warnings.filterwarnings('ignore')
Data['Date '] = pd.to_datetime(Data['Date '])
Data = Data[['Date ','OPEN ', 'HIGH ', 'LOW ', 'PREV. CLOSE ','close ']]
Data['OPEN '] = Data['OPEN '].str.replace(',', '')
Data['HIGH '] = Data['HIGH '].str.replace(',', '')
Data['LOW '] = Data['LOW '].str.replace(',', '')
Data['close '] = Data['close '].str.replace(',', '')
Data['PREV. CLOSE '] = Data['PREV. CLOSE '].str.replace(',', '')
Data['OPEN '] = pd.to_numeric(Data['OPEN '], errors='coerce')
Data['HIGH '] = pd.to_numeric(Data['HIGH '], errors='coerce')
Data['LOW '] = pd.to_numeric(Data['LOW '], errors='coerce')
Data['close '] = pd.to_numeric(Data['close '], errors='coerce')
Data['PREV. CLOSE '] = pd.to_numeric(Data['PREV. CLOSE '], errors='coerce')


