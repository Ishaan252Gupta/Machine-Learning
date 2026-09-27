import pandas as pd
import numpy as np
#series
a=["INDIA","PAKISTAN","USA"]
b=[1,2,3,4,2]
print(pd.Series(a))
print(pd.Series(b))
#custom index
marks=[28,6,7,99]
sub=["maths","english","sst","hindi"]
print(pd.Series(marks,index=sub))
pd.Series(marks,index=sub,name="ishaan")
marks={"maths":67,"chem":43,"SST":32}
run=pd.Series([1,2,3,4,5,6])
Marks_series=pd.Series(marks,name="Ishaan")
print(Marks_series)
print(Marks_series.size)
print(Marks_series.dtype)
print(Marks_series.index)
print(run.index)
print(Marks_series.values)
#reading csv file
subs=pd.read_csv("/Users/ishaangupta/Downloads/subs.csv").squeeze()
print(subs)
kohli=pd.read_csv("/Users/ishaangupta/Downloads/kohli_ipl.csv",index_col='match_no').squeeze()
print(kohli)
bolly=pd.read_csv("/Users/ishaangupta/Downloads/bollywood.csv",index_col="movie").squeeze()
print(bolly)
#head and tail
print(subs.head())
#we can give howmany no too
print(bolly.head(3))
#tail
print(subs.tail(4))
#for random use sample
print(subs.sample())
#can also pass no of them
print(subs.sample(4))
#counts no of times value has occured
print(bolly.value_counts())
#sorting
print(kohli.sort_values().tail(1).values[0])
kohli=kohli.sort_values()
print(kohli.tail(1))
print(bolly.sort_index().head(1).index[0])
bolly=bolly.sort_index()
#mean,medan,mode,standard deviation
print(subs.mean())
print(subs.var())
print(subs.std())
print(bolly.mode().values[0])
#min/max
print(bolly.min())
print(subs.describe())
marks={"maths":67,"chem":43,"SST":32}
marks[1]=100
print(marks[1])
marks["sst"]=100
print(marks)
