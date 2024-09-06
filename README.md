# CardinalityEstimationTestbed
The source code of Paper [`Learned Cardinality Estimation: A Design Space Exploration and A Comparative Evaluation`](https://vldb.org/pvldb/vol15/p85-li.pdf).
## Experiment of synthetic
#### Generate_data_sql
`cd CardinalityEstimationTestbed/Synthetic`\
`python generate_data_sql.py --cols [COLUMNS_NUM] --distinct [DOMAIN_SIZE] --corr [CORRELATION] --skew [SKEWNESS]`
#### Get_sql_truecard
`python get_truecard.py --version cols_[COLUMNS_NUM]_distinct_[DOMAIN_SIZE]_corr_[CORRELATION]_skew_[SKEWNESS]`
#### Get_result
`python get_result.py --cols [COLUMNS_NUM] --distinct [DOMAIN_SIZE] --corr [CORRELATION] --skew [SKEWNESS] --method [METHOD]`
- Then experimental results of all methods can be obtained.
#### Parameters
- `[COLUMNS_NUM]` should be an integer between 1 and 9.
- `[DOMAIN_SIZE]` should be an integer between 10 and 20000.
- `[CORRELATION]` should be an integer between 1 and 9.
- `[SKEWNESS]` should be an integer between 1 and 9.
- The parameters we use are:

`cols in [2, 4, 6, 8];
distinct in [10, 100, 1000, 10000];
corr in [2, 4, 6, 8];
skew in [2, 4, 6, 8]; `

## Experiment of overall
### Real Datasets prepare
- Download the [IMDB](http://homepages.cwi.nl/~boncz/job/imdb.tgz) data tables to: `../train-test-data/imdbdataset-str`
- Download the [forest, power](http://archive.ics.uci.edu/) data tables to: `../train-test-data/forest_power-data-sql`
- [XTZX](https://www.xuetangx.com/). We have put the data and workload for the experiment into the repositorie.
Begin by doing a simple job on the table, removing some unused columns. For Forest We use ﬁrst 10 numeric attributes; For Power We used the 7 numeric attributes after the ﬁrst two attributes (date and time).
- Remember to put the tables in their respective folders that do not contain table headers, for example: `forest_power-data-sql/no_head`, `imdbdata-num/no_head`, `xtzx-data-sql/no_head`.


### Forest & Power
- Run the `forest.sh, power.sh` in each method folder to execute the code to get the result.


### Imdb
- First, the strings in the data tables should be converted to numbers.\
`cd CardinalityEstimationTestbed/Overall/imdb`\
`python data_str2num.py`
#### Varying Columns
- `cd Overall/[METHOD]`\
`python run_exp.py --cols [cols]`
- For example: \
`cd Overall/deepdb`\
`python run_exp.py --cols 4`\
AND
`cd Overall/xgboost_localnn`\
`python run_exp.py --cols 4 --model [nn OR xgb]`
#### Varying Domain Size
- First, the data of the distinct is generated and populated.\
`cd CardinalityEstimationTestbed/Overall/imdb/distinct`\
`python data_process.py`
- Then refer to `run.sh` in mscn and neurocard folder to execute the code to get the result.

#### Varying Join samples
- For example: \
`cd Overall/deepdb`\
`python run_exp.py --cols 4 --samples 3`

### XTZX
- `cd Overall/[METHOD]`\
`python run_exp.py --xt [cols]`
- For example: \
`cd Overall/deepdb`\
`python run_exp.py --xt 4`\
AND
`cd Overall/xgboost_localnn`\
`python run_exp.py --xt 4 --model [nn OR xgb]`

### Update
- Select 10% of the number of rows in each table and add them to the end of the table.
- Refer to `update.sh` in each method folder to execute the code to get the result.

## Citation
```
@article{sun2021learned,
  title={Learned cardinality estimation: A design space exploration and a comparative evaluation},
  author={Sun, Ji and Zhang, Jintao and Sun, Zhaoyan and Li, Guoliang and Tang, Nan},
  journal={Proceedings of the VLDB Endowment},
  volume={15},
  number={1},
  pages={85--97},
  year={2021},
  publisher={VLDB Endowment}
}
@inproceedings{zhang2023autoce,
  title={Autoce: An accurate and efficient model advisor for learned cardinality estimation},
  author={Zhang, Jintao and Zhang, Chao and Li, Guoliang and Chai, Chengliang},
  booktitle={2023 IEEE 39th International Conference on Data Engineering (ICDE)},
  pages={2621--2633},
  year={2023},
  organization={IEEE}
}
```
