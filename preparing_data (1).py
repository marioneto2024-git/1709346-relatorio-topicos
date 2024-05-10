import pandas as pd

from sklearn import datasets, linear_model
name="<finalIMG_3784_0.jpg.csv>" # from the folder building_dataset
final_name="<dataset-mario>"
data = pd.read_csv("datasets/"+name+".csv", sep=";", header=None)
print(type(data))
print(data)
list=[1,2,3,4,5,6,7,8,9,0]
u=[]

for x in list:
    for y in range(0,10):
        u.append(x)
print(u)
print(len(u))
data[0] = u
print(data)
data.to_csv('./datasets/'+final_name+'.csv', header=None,index=None)
