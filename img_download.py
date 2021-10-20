# -*- coding: utf-8 -*-

import pandas as pd
import requests


dataset_description = pd.read_csv("Description_file.csv")

if __name__ == "__main__":

    for index,row in dataset_description.iterrows():
        
        with open(row['Depiction_Name'], 'wb') as handle:
            response = requests.get(row['Depiction'], stream=True)
        
            if not response.ok:
                print (response)
        
            for block in response.iter_content(1024):
                if not block:
                    break
        
                handle.write(block)
        print(index)
