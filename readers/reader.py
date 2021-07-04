# -*- coding: utf-8 -*-
"""
@author: rishabbh-sahu
"""

import os
import yaml

class Reader:
    
    def __init__(self):
        pass

    def read_yaml_from_file(filepath:str):
        with open(filepath, encoding='utf-8') as fp:
            return yaml.load(fp, Loader=yaml.SafeLoader)

    def read_dataframes(filepath:str,header=None):
        '''Reading input data from csv'''
        import pandas
        return pandas.read_csv(filepath,header=header,skip_blank_lines=True)


    def read(dataset_folder_path):
        labels = None
        text_arr = None
        tags_arr = None
        with open(os.path.join(dataset_folder_path, 'label'), encoding='utf-8') as f:
            labels = f.read().splitlines()
        
        with open(os.path.join(dataset_folder_path, 'seq.in'), encoding='utf-8') as f:
            text_arr = f.read().splitlines()
        
        with open(os.path.join(dataset_folder_path, 'seq.out'), encoding='utf-8') as f:
            tags_arr = f.read().splitlines()
            
        assert len(text_arr) == len(tags_arr) == len(labels)
        return text_arr, tags_arr, labels
        
if __name__ == '__main__':
    df = Reader.read_dataframes('./data/atis_intents.csv')
