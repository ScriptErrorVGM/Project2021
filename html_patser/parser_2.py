from unicodedata import name
from pyrsistent import b
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def main():
    df = pd.read_csv (r'C:\Users\mixaj\Documents\Python1_2021\html_patser\titanic.csv', index_col = 0)
    #df = pd.DataFrame(index = ['PassengerId'], columns = ['Survived','Pclass'])
    df1 = df.dropna() 
    print(df1)
    print(df1.info())
    print(df1.describe())

    ax = df1["Age"].plot.hist(color = "red")
    ax.set_title('Age of Passengers')
    ax.set_xlabel('Age')
    ax.set_ylabel('Amount')
    #plt.show()
    print("---------------------")
    print(df1['Fare'].describe())

    l = list(df1.columns)
    print(l)

    #df.columns = ['Survived', 'Class', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    #df.rename(columns = {"Pcalss" : "Class"}, inplace = True)
    my_cols = list(df1.columns)
    my_cols[1] = "Class"
    df1.columns = my_cols
    print(df1.columns)

    df1["female"] = df1["Sex"] == 'female'
    print(df1.info())

    df1["Ymale"] = ((df1["Survived"] == 1) & (df1["Sex"] == 'Male') & (df1["Age"] < 32))
    print(df1.info())

    print(df1[(df1["Class"] == 1) | (df1["Class"] == 2)])
    print(df1[(df1["Survived"] == 1) & ((df1["Class"] == 1) | (df1["Class"] == 2))])
    
    df1["Female"] = df1["female"] 
    newh =[int(i) for i in df1["Female"]]
    df1["Female"] = newh
    print(df1.head())

    print(df1["Embarked"].unique())

    df_g = df1.groupby("Survived")['Class', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    print(df_g)

    df1.columns = map(str.lower, df1.columns)
    df1.to_csv("Titanic-new.csv", encoding= 'utf-8')



if __name__ == "__main__":
    main()    
    
