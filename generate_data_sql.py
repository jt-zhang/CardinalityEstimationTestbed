import random
import logging
import numpy as np
import pandas as pd
from scipy.stats import truncnorm, truncexpon, genpareto
from typing import Dict, Any
import os
from numpy.random import choice
import argparse

parser = argparse.ArgumentParser(description='generatedata')

parser.add_argument('--distinct', type=int, help='datasets_dir', default=1000)
parser.add_argument('--cols', type=int, help='datasets_dir', default=4)
parser.add_argument('--corr', type=float, help='datasets_dir', default=5)
parser.add_argument('--skew', type=float, help='datasets_dir', default=5)

args = parser.parse_args()

dom = args.distinct
cols = args.cols
corr = args.corr
skew = args.skew

version = 'cols_' + str(cols) + '_distinct_' + str(args.distinct) + '_corr_' + str(int(corr)) + '_skew_' + str(int(skew))

corr = args.corr/10
skew = args.skew/10  # 除10为了create table

path = '/home/zhangjintao/Benchmark3/csvdata_sql'
csv_path = path+ '/' f"{version}.csv"
csv_path2 = path+ '/' f"{version}_nohead.csv"
seed = 2
L = logging.getLogger(__name__)

for i in range(cols-1):
    seed = seed + 1
    row_num = 100000  # 
    col_num = 2

    random.seed(seed)
    np.random.seed(seed)

    # generate the first column according to skew
    col0 = np.arange(dom) # make sure every domain value has at least 1 value
    tmp = genpareto.rvs(skew-1, size=row_num-len(col0)) # c = skew - 1, so we can have c >= 0
    tmp = ((tmp - tmp.min()) / (tmp.max() - tmp.min())) * dom # rescale generated data to the range of domain
    col0 = np.concatenate((col0, np.clip(tmp.astype(int), 0, dom-1)))

    # generate the second column according to the first
    col1 = []
    for c0 in col0:
        col1.append(c0 if np.random.uniform(0, 1) <= corr else np.random.choice(dom))
    if i == 0:
        df = pd.DataFrame(data={'col' + str(2*i): col0, 'col' + str(2*i+1): col1})
    else:
        df['col' + str(i+1)] = col1
    

L.info(f"Dump as version {version} to disk")
df.to_csv(csv_path, index=False)
df.to_csv(csv_path2, index=False, header = False)

ops = ['=', '<', '>']  #训练和测试均无 >=, <=
f2 = open('/home/zhangjintao/Benchmark3/csvdata_sql/'+ version + '.sql','w')
for i in range(3600000):   # 尽可能多的sql
    a = list(np.random.randint(0, dom, 1))[0]
    sql = 'SELECT COUNT(*) FROM ' + version + ' cdcs WHERE '
    for i in range(cols):
        sql += 'cdcs.col' + str(i) + choice(ops) + str(a) + ' AND '
    sql = sql[0: len(sql)-5]
    sql = sql + ';\n'
    f2.write(sql)
f2.close()

f3 = open('/home/zhangjintao/Benchmark3/csvdata_sql/schema_'+ version + '.sql','w')
sql = 'CREATE TABLE ' + version + '(\n'
for i in range(cols):
    sql += '    col' + str(i) + ' integer NOT NULL,\n'
sql = sql[0: len(sql)-2] + '\n);'
f3.write(sql)
f3.close()