import pandas as pd

# noinspection PyUnresolvedReferences
name="<dataset-finalIMG_3784_0>" # from the folder building_dataset
final_name="<mario_neto>"
data = pd.read_csv("datasets/"+name+".csv", sep=";", header=None)
print(type(data))
print(data)
list=[1,2,3,4,5,6,7,8,9]
u=[]
u.append(0)

for x in list:
    u.append(0)
    for y in range(0,10):
        u.append(x)
print(u)
print(len(u))
data[0] = u
print(data)
data.to_csv('./datasets/'+final_name+'.csv', header=None,index=None)
