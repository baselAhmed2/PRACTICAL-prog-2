
"""
Fare  المبلغ المدفوع في التذكره 
Embarked المنطقة السفينة التي صعد منها 
pclass     [1, 2, 3]  درجه الركوب
"SibSp" = 0: لا يوجد أشقاء أو زوجات على متن السفينة للراكب.
"SibSp" = 1: هناك أخ أو شقيقة واحدة أو زوجة أو زوج على متن السفينة للراكب.
"SibSp" = 2: هناك أختان أو زوجتان أو زوجين على متن السفينة للراكب.
وهكذا.


Pclass  1 راقي
Pclass  2 متوسط
Pclass  3 عاديه 
"""

# ---------------------------------------------------------------------------------
#? ---------------------------START PREPROCESSING----------------------------------
#! ---------------------------------------------------------------------------------

# !IMPORT CATEGORY
# ---------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv("train_and_test2.csv")
# ---------------------------------------------------------------------------------

# !HANDLING CATEGORY
# ---------------------------------------------------------------------------------
# ? Handling duplicates columns if they exist
duplicated_columns = df.columns[df.columns.duplicated()]
df = df.drop(duplicated_columns, axis=1)

# ? fill null value with mean
mean = df["Embarked"].mean()
df["Embarked"].fillna(value=mean, inplace=True)

# --------------------------------------------------------------------------------

# !DROPS CATEGORY 
# ---------------------------------------------------------------------------------
#? delete zero columns from 1 to 90
for x in range(1, 20):
    column_name = f"zero.{x}"
    try:
        
        df = df.drop([column_name], axis=1)
    except:
        continue
df = df.drop(["zero"], axis=1)
# ? Delete the column id 
df = df.drop(["Passengerid"], axis=1)
# ---------------------------------------------------------------------------------

# !CONVERT CATEGORY
# ---------------------------------------------------------------------------------
# ? convert sex into string
# df["Sex"].replace({"male":0, "female":1}, inplace=True)


# ---------------------------------------------------------------------------------
#! ---------------------------END PREPROCESSING------------------------------------
#? ---------------------------------------------------------------------------------


# print(df)


# ---------------------------------------------------------------------------------
#? ---------------------------START DATA VISUALIZATION-----------------------------
#! ---------------------------------------------------------------------------------

# !HISTOGRAM
# ---------------------------------------------------------------------------------
# # ? Histogram
# plt.style.use('ggplot')

# df.hist(bins=50,layout=(4,3),figsize=(20,20))
# plt.show()
# -------------------------------------------------------------------------------


# !PLOT
# ---------------------------------------------------------------------------------
# ?plot
# plt.style.use('ggplot')
# df_without_f = df.drop('Fare', axis=1)
# df_without_f.plot()
# plt.show()
# --------------------------------------------------------------------------------


# !DENSITY PLOT
# ---------------------------------------------------------------------------------
# ? Density plot
# plt.style.use('ggplot')
# df_without_f = df.drop('Fare', axis=1)
# # subplots بتفصلهم 
# df_without_f.plot(kind='density', subplots=True, layout=(4,3), sharex=False)
# plt.show()
# --------------------------------------------------------------------------------


# !BOX PLOT
# ---------------------------------------------------------------------------------
# ? Box plot
# plt.style.use('ggplot')
# df_without_f = df.drop('Fare', axis=1)
# df_without_f.plot(kind='box', subplots=True, layout=(4,3), sharex=False, sharey=False)
# plt.show()
# # ? Box plot bar chart
# ! don't try it at your home 
# # plt.style.use('ggplot')
# df_without_f = df.drop('Fare', axis=1)
# df_without_f.plot(kind='bar', subplots=True, layout=(4,3))
# df_without_f.plot=df_without_f.head(2)
# plt.show()

# ----------------------------------------------------------------

# ! correlation
# ---------------------------------------------------------------------------------
# # ? Correlation
# plt.style.use('ggplot')
# df_without_f = df.drop('Fare', axis=1)
# d=df_without_f.select_dtypes(include='number')
# d=sns.heatmap(d.corr())
# plt.show()
# --------------------------------------------------------------------------------

# ! Triangle correlation
# ---------------------------------------------------------------------------------
# ? Triangle correlation
# plt.style.use('ggplot')
# df = df.drop('Fare', axis=1)
# d=df.select_dtypes(include='number')
# mask=np.triu(np.ones_like(d.corr()))
# dataplot=sns.heatmap(d.corr(), cmap="YlGnBu", annot=True, mask=mask)
# plt.show()
# --------------------------------------------------------------------------------

# !Scatter Matrix Plot
# ---------------------------------------------------------------------------------
# ? Scatter Matrix Plot
# plt.style.use('ggplot')
# df_without_f = df.drop('Fare', axis=1)
# d=df_without_f.select_dtypes(include='number')
# d=sns.pairplot(d)
# plt.show()
# --------------------------------------------------------------------------------

#! pairpolt
# --------------------------------------------------------------------------------
# # ? pairpolt
# plt.style.use('ggplot')
# d = df.head(5)
# sns.pairplot(d, hue="Sex")
# plt.show()
# --------------------------------------------------------------------------------






