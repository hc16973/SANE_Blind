
## This is a script for Blind SANE ##

#####################################

## Research question: 

## Is there any gender and ethnicity differences in willingness of going to the university?

## ===========================================================================================================================

#### Getting things set-up

## Check the version of Python 

## There should have Python 3.8 but can install Python 3.12

#### Install the packages

#%matplotlib inline
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

#### Setting up working directory

##### Check the current working directory

path = os.getcwd()

print(path)

print(type(path))

##### Change the working directory 

os.chdir('..')

print(os.getcwd())


#### Read-in and open the data file

my_dataframe_main = pd.read_csv("SANE Blind/main_dummy.csv")      # Read in the main interview data
# my_dataframe_main = pd.read_csv("../input/main_dummy.csv") 


#### Subset the data (only keep those relevant variables)

data_main = my_dataframe_main[["NSID", "W4SexYP", "w4ethnic2YP", "W4IfeverYP"]]

data_main.head()


#### Rename the variables

## Sex = W9DSEX; Ethnicity = W9ETHNICCAT; Total Correct = W9NUMCORRECT; Total Score = W9SCORE

data = data_main.rename(columns={'W4SexYP':'SEX', 'w4ethnic2YP':'ETHNICITY', 'W4IfeverYP':'University'}) 

print(data)

#### Frequency table (To check all the Ns are above threshold)

##### One-way table
# Table of sex
table_sex = pd.crosstab(index=data['SEX'],  # Make a crosstab
                       columns="count")     # Name the count column

table_sex

type(table_sex)             # Confirm that the crosstab is a DataFrame


# Table of ethnicity
table_eth = pd.crosstab(index=data['ETHNICITY'],  # Make a crosstab
                       columns="count")           # Name the count column

table_eth

type(table_eth)             # Confirm that the crosstab is a DataFrame


##### Two-way tables

# Table of Sex vs. Ethnicity 
table_sex_eth = pd.crosstab(index=data['SEX'], 
                           columns=data['ETHNICITY'])

#table_sex_eth.index= ["Male","Female"]

table_sex_eth


#### Descriptive statistics table

#### Descriptive statistics

data.head()

data.describe()


table_both = pd.crosstab(index=[data['SEX'], data['ETHNICITY']], columns=data['University'])
print(table_both)


#### ANOVA

##### Check is there any gender differences in willingness of going to the university

model = ols('University~SEX',                 # Model formula
            data = data).fit()
                
anova_sex = sm.stats.anova_lm(model, typ=2)

print (anova_sex)


##### Check is there any differences in ethnicity in willingness of going to the university

model = ols('University~ETHNICITY',                 # Model formula
            data = data).fit()
                
anova_eth = sm.stats.anova_lm(model, typ=2)

print (anova_eth)


##### Check is there any gender and ethnicity in willingness of going to the university

model = ols('University~ETHNICITY*SEX',                 # Model formula
            data = data).fit()
                
anova_both = sm.stats.anova_lm(model, typ=2)

print (anova_both)


