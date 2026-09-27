import pandas as pd
import numpy as np
# USING LIST
studentdata=[
            [100,90,12],
            [80,80,10],
            [70,20,6],
]
s1=pd.DataFrame({
    "name ": ['a','gr','e','h'],
    "marks": [21,98,90,65],
})
print(pd.DataFrame(studentdata, columns=["iq","avd","pack"]))
#USING DICTIONARY
student_dict=pd.DataFrame({
    "name": ["a","ba","c","d","e"],
    "iq":[100,80,70,0,0],
    "avd":[90,80,20,0,0],
    "pack":[12,10,6,0,0],
})
print(pd.DataFrame(student_dict))
#reading file
movies=pd.read_csv("/Users/ishaangupta/Downloads/COLLEGE/movies.csv")
print(movies.shape)
print(movies.dtypes)
print(movies.index)
print(movies.columns)
print(movies.values)
#HEAD AND TAIL
print(movies.head(10))
#SAMPLE
print(movies.sample(5))
#info of data
print(movies.info())
#describe used to represent only numeric values
print(movies.describe())
#is null the empty values become true
print(movies.isnull())
#can add sum ahead it will tell  how many of them are them are empty ""COLOUMN WISE"" // NOT ROW WISE
print(movies.isnull().sum()) 
#flags the row as ""TRUE "" if its remoted as before
print(movies.duplicated())
#same as sum it sums rows which are duplicted
print(movies.duplicated().sum())
print(student_dict.duplicated().sum())
print(pd.DataFrame(student_dict))
#we can rename the coloumns names
print(student_dict.rename(columns={"avd":"package","pack":"i"}))
#if we need to print multiple selected cols "single col =series"
print(student_dict[["avd"]])
#fetch rows and make any coloumn as index coloumn inplace makes it permanent
student_dict.set_index("name",inplace=True)
print(student_dict)
print(movies.iloc[5:9])
#in iloc last one is excluded[)
#butt in loc last one is included[]
print(movies.iloc[0:9,0:2])
ipl=pd.read_csv("/Users/ishaangupta/Downloads/ipl-matches.csv")
mask=ipl["MatchNumber"]=="Final"
print(ipl[mask])



