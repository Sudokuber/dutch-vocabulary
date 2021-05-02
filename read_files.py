import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods
from os.path import splitext, isfile

def file_path():
    file_path = "E:/Inburgering examen/Welkom in Nederland/vocabulary exercise/wordlists/"
    return file_path

# if ext.endswith('.csv'):
def read_csv_file(file_loc):
    df = pd.read_csv(file_loc, delimiter='\t')
    return df

# if ext.endswith('.ods'):
def read_ods_file(file_loc):
    df = read_ods(file_loc, 1)
    return df


def clean_dataframe(df):
     # replace any empty strings in the engels column with NaN value
    df['Engels'].replace('', np.nan, inplace=True)
    # drop the null values
    df.dropna(subset=['Engels'], inplace=True)
    wordlist = df.set_index('Nederlands')['Engels'].to_dict()
    return wordlist

def pick_file(file_path):
    file = file_path + \
                input('write down the name (with extension) of the word list you want to use today: ')
    file_not_exist = True
    while file_not_exist:
        if isfile(file):
            file_not_exist = False
            return file
        else:
            print('File does not exist!')
            file = file_path + input('Please write down a valid file name: ')


def convert_file(file_loc):
    #check extension (.ods or .csv)
    ext = splitext(file_loc)[-1].lower()
    if ext.endswith('.csv'):
        df = read_csv_file(file_loc)
    elif ext.endswith('.ods'):
        df = read_ods_file(file_loc)
    wordlist = clean_dataframe(df)
    return wordlist


