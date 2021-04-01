import pandas as pd
import numpy as np
import random
from numpy.random import choice

dictforest = {'forest':[ 'forest', 'Elevation','Aspect','Slope','Horizontal_Distance_To_Hydrology','Vertical_Distance_To_Hydrology','Horizontal_Distance_To_Roadways','Hillshade_9am','Hillshade_Noon','Hillshade_3pm','Horizontal_Distance_To_Fire_Points']}

df_forest = pd.read_csv("/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/forest.csv", sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"')

df_forest = df_forest.dropna(axis=0, how='any', inplace=False)

forest_Elevation=[]
forest_Aspect=[]
forest_Slope=[]
forest_Horizontal_Distance_To_Hydrology=[]
forest_Vertical_Distance_To_Hydrology=[]
forest_Horizontal_Distance_To_Roadways=[]
forest_Hillshade_9ams=[]
forest_Hillshade_Noon=[]
forest_Hillshade_3pm=[]
forest_Horizontal_Distance_To_Fire_Points=[]

for key, value in dictforest.items():
    for i in range(1, len(value)):
        locals()[value[0] + '_' + value[i]] = list(locals()['df_'+key][value[i]].unique())

f2 = open("/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/forest.sql",'w')

ops = ['=', '<', '>']  #训练和测试均无 >=, <=

dictcols = {'forest':['Elevation','Aspect','Slope','Horizontal_Distance_To_Hydrology','Vertical_Distance_To_Hydrology','Horizontal_Distance_To_Roadways','Hillshade_9am','Hillshade_Noon','Hillshade_3pm','Horizontal_Distance_To_Fire_Points']}

for i in range(180000):
    questr = 'SELECT COUNT(*) FROM forest forest WHERE '
    predicates = []
    
    num_col = random.randint(1,len(dictcols['forest'])-1)
      
    t1 = list(choice(dictcols['forest'], num_col, replace=False))
    for k in range(num_col):
        t2 = locals()['forest_'+ t1[k]]
        predicates.append('forest.' + str(t1[k]) + choice(ops) + str(float(choice(t2))))
    
    for pre in predicates:
          questr += pre + ' AND '
    questr = questr[:len(questr)-5]
    questr +=';\n'
    
    f2.write(questr)
f2.close()

dictpower = {'power':[ 'power', 'Global_active_power','Global_reactive_power','Voltage','Global_intensity','Sub_metering_1','Sub_metering_2','Sub_metering_3']}

df_power = pd.read_csv("/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/power.csv", sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"')

df_power = df_power.dropna(axis=0, how='any', inplace=False)

power_Elevation=[]
power_Aspect=[]
power_Slope=[]
power_Horizontal_Distance_To_Hydrology=[]
power_Vertical_Distance_To_Hydrology=[]
power_Horizontal_Distance_To_Roadways=[]
power_Hillshade_9ams=[]
power_Hillshade_Noon=[]
power_Hillshade_3pm=[]
power_Horizontal_Distance_To_Fire_Points=[]

for key, value in dictpower.items():
    for i in range(1, len(value)):
        locals()[value[0] + '_' + value[i]] = list(locals()['df_'+key][value[i]].unique())
f2 = open("/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/power.sql",'w')

ops = ['=', '<', '>']  #训练和测试均无 >=, <=

dictcols = {'power':['Global_active_power','Global_reactive_power','Voltage','Global_intensity','Sub_metering_1','Sub_metering_2','Sub_metering_3']}

for i in range(180000):
    questr = 'SELECT COUNT(*) FROM power power WHERE '
    predicates = []
    
    num_col = random.randint(1,len(dictcols['power'])-1)
      
    t1 = list(choice(dictcols['power'], num_col, replace=False))
    for k in range(num_col):
        t2 = locals()['power_'+ t1[k]]
        predicates.append('power.' + str(t1[k]) + choice(ops) + str(float(choice(t2))))
    
    for pre in predicates:
          questr += pre + ' AND '
    questr = questr[:len(questr)-5]
    questr +=';\n'
    
    f2.write(questr)
f2.close()

f = open('/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/' + 'forest' + 'test.sql')
queries = f.readlines() 
f2 = open('/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/' + 'forest' + 'test2.sql', 'w')
for query in queries:
    cnt = query.count('forest')
    if cnt == 3 or cnt == 12:
        continue
    else:
        f2.write(query)
f2.close()

f = open('/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/' + 'power' + 'test.sql')
queries = f.readlines() 
f2 = open('/home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/' + 'power' + 'test2.sql', 'w')
for query in queries:
    cnt = query.count('power.')
    if cnt == 1 or cnt == 10:
        continue
    else:
        f2.write(query)
f2.close()