#!/usr/bin/env python
# ClusterSpy.py: script to inspect illustrative (randomly chosen) clusters 
# from the paper "From Mad Men to Maths Men:  Concentration and Buyer Power in Online Advertising"
# by Francesco Decarolis and Gabriele Rovigatti
from os.path import dirname, abspath, basename
import pandas as pd
from random import randint
# Function to read cluster #
def readClust(data):
    ind = input("""Input the desired industry (numbers ONLY):
        'Houseware' - 12
        'Restaurants' - 18 or 8 or 10
        'Travel' - 22 or 9
        'Automotive' - 4 or 23
        'Institutions' - 3 
        'Agriculture' - 7 
        'Apparel' - 2 
        'Financial' - 6 or 16
        'Retail' - 19
        'Technology' - 20 or 15 or 21
        'Media' - 14
        'Industrial' - 13
        'Recreation' - 17
        'Beauty' - 1
        'Education' - 5
        'DIY'  11
        """)
    while ind.isdigit() == False or int(ind) > 23 or int(ind) < 1:
        ind = input('Please, input numbers 1 to 23 only!')
    inddata = data.loc[int(ind)] # subset the industry
    inddata.set_index('ordered_cluster_ID', inplace=True) # reset the index to cluster
    return inddata['keyword'].loc[randint(1, 6)] # return a random cluster
# Main Code #
if __name__ == "__main__":
    clustdir = dirname(abspath(__file__)) + '/cluster_examples_full.csv'
    cldf = pd.read_csv(clustdir, index_col = 3, delimiter = '\t')
    reader = 'Y'
    while reader == 'Y' or reader == 'y' or reader == 'Yes':
        print(readClust(cldf).to_frame().to_string(index=False, justify = 'initial'))
        reader = input("Another cluster? Type 'Y' to continue")
