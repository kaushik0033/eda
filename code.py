# --------------
# Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
#### Data 1
# Load the data


df_automobile_1=pd.read_csv(path)
# Overview of the data
df_automobile_1.info()
df_automobile_1.describe()
plt.hist(df_automobile_1.price)
sns.countplot(df_automobile_1.make)
sns.heatmap(df_automobile_1.corr(),annot=True)
sns.jointplot(df_automobile_1.horsepower,df_automobile_1.price)
sns.boxplot(x='body-style',y='price',data=df_automobile_1)
# Histogram showing distribution of car prices


# Countplot of the make column


# Jointplot showing relationship between 'horsepower' and 'price' of the car


# Correlation heat map


# boxplot that shows the variability of each 'body-style' with respect to the 'price'


#### Data 2

# Load the data
df_automobile_2=pd.read_csv(path2)
df_automobile_2.info()
df_automobile_2.describe()
df_num=df_automobile_2.select_dtypes(exclude='object')
df_num.info()
df_num.replace('?','NaN',inplace=True)
df_num.fillna(df_num.mean(), inplace=True)
skewdata=skew(df_num)
# Impute missing values with mean


# Skewness of numeric features



# Label encode 



# Code ends here


