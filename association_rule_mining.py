#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #5
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules

#Use the command: "pip install mlxtend" on your terminal to install the mlxtend library

#read the dataset using pandas
df = pd.read_csv('retail_dataset.csv', sep=',')

#find the unique items all over the data an store them in the set below
itemset = set()
for i in range(0, len(df.columns)):
    items = (df[str(i)].unique())
    itemset = itemset.union(set(items))

#remove nan (empty) values by using:
itemset.remove(np.nan)

#To make use of the apriori module given by mlxtend library, we need to convert the dataset accordingly. Apriori module requires a
# dataframe that has either 0 and 1 or True and False as data.
#Example:

#Bread Wine Eggs
#1     0    1
#0     1    1
#1     1    1

#To do that, create a dictionary (labels) for each transaction, store the corresponding values for each item (e.g., {'Bread': 0, 'Milk': 1}) in that transaction,
#and when is completed, append the dictionary to the list encoded_vals below (this is done for each transaction)
#-->add your python code below

encoded_vals = []
for index, row in df.iterrows():
    labels = {'Bread':0,
              'Milk': 0,
              'Wine': 0,
              'Eggs': 0,
              'Meat': 0,
              'Cheese': 0,
              'Pencil': 0,
              'Diaper' : 0,
              'Bagel' : 0}
    for i in range(len(row)-1):
        if row[i] in labels:
            labels[row[i]] =  labels.get(row[i],0) + 1
    encoded_vals.append(labels)
    print(labels)
#adding the populated list with multiple dictionaries to a data frame
ohe_df = pd.DataFrame(encoded_vals)

#calling the apriori algorithm informing some parameters
freq_items = apriori(ohe_df, min_support=0.2, use_colnames=True, verbose=1)
rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)

#iterate the rules data frame and print the apriori algorithm results by using the following format:
#Meat, Cheese -> Eggs
#Support: 0.21587301587301588
#Confidence: 0.6666666666666666
#Prior: 0.4380952380952381
#Gain in Confidence: 52.17391304347825
#-->add your python code below
supportCount = 0
print(rules)
for i in range(len(rules)):
    print("\n\n\n\nStart of print chain")
    currSupport = rules['support']
    print("current support: " + str(currSupport))
    currConfidence = rules['confidence']
    print("current confidence: " + str(currConfidence))
    #To calculate the prior and gain in confidence, find in how many transactions the consequent of the rule appears (the supporCount below). Then,
    #use the gain formula provided right after.
    prior = supportCount/len(encoded_vals) 
    print("Gain in Confidence: " + str(100*(currConfidence-prior)/prior))
    supportCount += 1
    #-->add your python code below

    #Finally, plot support x confidence
    plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
    plt.xlabel('support')
    plt.ylabel('confidence')
    plt.title('Support vs Confidence')
    plt.show()