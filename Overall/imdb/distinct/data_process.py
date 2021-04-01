import pandas as pd
import numpy as mp
import random
from numpy.random import choice

# Read raw data that has not been populated
df_title = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-unpopulated/title.csv', sep=',', escapechar='\\', encoding='utf-8',
                       low_memory=False, quotechar='"',usecols = ['id','imdb_index', 'kind_id', 'production_year', 'phonetic_code', 'season_nr', 'episode_nr', 'series_years'])

idlist = df_title["id"].tolist()

df_cast_info = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-unpopulated/cast_info.csv', sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"',error_bad_lines=False
                          ,usecols =['movie_id', 'nr_order', 'role_id'])

df_movie_companies = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-unpopulated/movie_companies.csv', sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"',
                                usecols=['movie_id', 'company_type_id'])

df_movie_info = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-unpopulated/movie_info.csv', sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"',
                           usecols = ['movie_id', 'info_type_id'])

df_movie_info_idx = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-unpopulated/movie_info_idx.csv', sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"',
                               usecols = ['movie_id', 'info_type_id'])

df_movie_keyword = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-unpopulated/movie_keyword.csv', sep=',', escapechar='\\', encoding='utf-8', low_memory=False, quotechar='"',
                              usecols=['movie_id', 'keyword_id'])

dict1 = {'title':['t', 'id', 'imdb_index', 'kind_id', 'production_year', 'phonetic_code', 'season_nr', 'episode_nr', 'series_years'],
         'movie_info_idx': ['mi_idx', 'movie_id', 'info_type_id'], 
         'movie_info': ['mi', 'movie_id', 'info_type_id'],
         'cast_info': ['ci', 'movie_id', 'nr_order', 'role_id'],
         'movie_keyword': ['mk', 'movie_id', 'keyword_id'],
         'movie_companies': ['mc', 'movie_id', 'company_type_id']}  

for key, value in dict1.items():
    for i in range(2, len(value)):
        locals()[value[0] + '_' + value[i]] = list(locals()['df_'+key][value[i]].unique())  #
        locals()[value[0] + '_' + value[i]].sort()
        del locals()[value[0] + '_' + value[i]][0]
        for j in range(len(locals()['df_'+key][value[i]])):
            if pd.isnull(locals()['df_'+key][value[i]][j]):
                locals()['df_'+key][value[i]][j] = list(choice(locals()[value[0] + '_' + value[i]], 1, replace=False))[0]

for key, value in dict1.items():
    for i in range(2, len(value)):
        locals()[value[0] + '_' + value[i]] = list(locals()['df_'+key][value[i]].unique())  #
        locals()[value[0] + '_' + value[i]].sort()
        del locals()[value[0] + '_' + value[i]][0]

df_title.to_csv('/home/zhangjintao/Benchmark2/Data/high-populated/title.csv',index=0)
df_cast_info.to_csv('/home/zhangjintao/Benchmark2/Data/high-populated/cast_info.csv',index=0)
df_movie_companies.to_csv('/home/zhangjintao/Benchmark2/Data/high-populated/movie_companies.csv',index=0)
df_movie_info.to_csv('/home/zhangjintao/Benchmark2/Data/high-populated/movie_info.csv',index=0)
df_movie_info_idx.to_csv('/home/zhangjintao/Benchmark2/Data/high-populated/movie_info_idx.csv',index=0)
df_movie_keyword.to_csv('/home/zhangjintao/Benchmark2/Data/high-populated/movie_keyword.csv',index=0)

# Mid  production_year & phonetic_code & series_year & role_id
dict2 = {'title':['t', 'id', 'production_year', 'phonetic_code', 'series_years'],
         'cast_info': ['ci', 'movie_id', 'role_id']} 
# It has been dealt with before locals()['df_'+key][value[i]])
py = list(choice(locals()['t' + '_' + 'production_year'], int(0.6*len(locals()['t' + '_' + 'production_year'])), replace=False))
ph = list(choice(locals()['t' + '_' + 'phonetic_code'], int(0.6*len(locals()['t' + '_' + 'phonetic_code'])), replace=False))
sy = list(choice(locals()['t' + '_' + 'series_years'], int(0.6*len(locals()['t' + '_' + 'series_years'])), replace=False))
ri = list(choice(locals()['ci' + '_' + 'role_id'], int(0.6*len(locals()['ci' + '_' + 'role_id'])), replace=False))

df_title = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-populated/title.csv', sep=',', escapechar='\\', encoding='utf-8',
                       low_memory=False, quotechar='"')

df_cast_info = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-populated/cast_info.csv', sep=',', escapechar='\\', encoding='utf-8',
                       low_memory=False, quotechar='"',error_bad_lines=False)
# Title is filtered first, and then other tables are filtered 1. ID is filtered, 2. Other column conditions are filtered
df_title = df_title[(df_title['production_year'].isin(py)) & (df_title['phonetic_code'].isin(ph)) & (df_title['series_years'].isin(sy))]
idlist = df_title["id"].tolist()
df_cast_info = df_cast_info[(df_cast_info['role_id'].isin(ri)) & (df_cast_info['movie_id'].isin(idlist))]
df_title.to_csv('/home/zhangjintao/Benchmark2/Data/mid-populated/title.csv',index=0)
df_cast_info.to_csv('/home/zhangjintao/Benchmark2/Data/mid-populated/cast_info.csv',index=0)


# Low  production_year & phonetic_code & series_year & role_id
dict2 = {'title':['t', 'id', 'production_year', 'phonetic_code', 'series_years'],
         'cast_info': ['ci', 'movie_id', 'role_id']} 
# 
py = list(choice(locals()['t' + '_' + 'production_year'], int(0.3*len(locals()['t' + '_' + 'production_year'])), replace=False))
ph = list(choice(locals()['t' + '_' + 'phonetic_code'], int(0.3*len(locals()['t' + '_' + 'phonetic_code'])), replace=False))
sy = list(choice(locals()['t' + '_' + 'series_years'], int(0.3*len(locals()['t' + '_' + 'series_years'])), replace=False))
ri = list(choice(locals()['ci' + '_' + 'role_id'], int(0.3*len(locals()['ci' + '_' + 'role_id'])), replace=False))

df_title = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-populated/title.csv', sep=',', escapechar='\\', encoding='utf-8',
                       low_memory=False, quotechar='"')

df_cast_info = pd.read_csv( '/home/zhangjintao/Benchmark2/Data/high-populated/cast_info.csv', sep=',', escapechar='\\', encoding='utf-8',
                       low_memory=False, quotechar='"',error_bad_lines=False)
# 
df_title = df_title[(df_title['production_year'].isin(py)) & (df_title['phonetic_code'].isin(ph)) & (df_title['series_years'].isin(sy))]
idlist = df_title["id"].tolist()
df_cast_info = df_cast_info[(df_cast_info['role_id'].isin(ri)) & (df_cast_info['movie_id'].isin(idlist))]
df_title.to_csv('/home/zhangjintao/Benchmark2/Data/low-populated/title.csv',index=0)
df_cast_info.to_csv('/home/zhangjintao/Benchmark2/Data/low-populated/cast_info.csv',index=0)
