# CardinalityEstimationTestbed
CardinalityEstimationTestbed

## Experiment of synthetic
#### Generate_data_sql
`cd CardinalityEstimationTestbed\Synthetic`\
`python generate_data_sql.py --cols [COLUMNS_NUM] --distinct [DOMAIN_SIZE] --corr [CORRELATION] --skew [SKERNESS]`
#### Get_sql_truecard
`python get_truecard.py --version cols_[COLUMNS_NUM]_distinct_[DOMAIN_SIZE]_corr_[CORRELATION]_skew_[SKEWNESS]`
#### Get_result
`python get_result.py --cols [COLUMNS_NUM] --distinct [DOMAIN_SIZE] --corr [CORRELATION] --skew [SKERNESS] --method [METHOD]`
- Then experimental results of all methods can be obtained.
#### Parameters
- `[COLUMNS_NUM]` should be an integer between 1 and 9.
- `[DOMAIN_SIZE]` should be an integer between 10 and 20000.
- `[CORRELATION]` should be an integer between 1 and 9.
- `[SKEWNESS]` should be an integer between 1 and 9.\
- The parameter we use is

    cols in [2, 4, 6, 8]
    distinct in [10, 100, 1000, 10000]
    corr in [2, 4, 6, 8]
    skew in [2, 4, 6, 8]

## Experiment of overall
### Real Datasets download
- Download the [IMDB](http://homepages.cwi.nl/~boncz/job/imdb.tgz) data tables to: `../train-test-data/imdbdataset-str`
- Download the [forest, power](http://archive.ics.uci.edu/) data tables to: `../train-test-data/forest_power-data-sql`\
Begin by doing a simple job on the table, removing some unused columns. For Forest We use ﬁrst 10 numeric attributes; For Power We used the 7 numeric attributes after the ﬁrst two attributes (date and time).
### Imdb
- First, the strings in the data tables should be converted to numbers.\
`cd CardinalityEstimationTestbed\Overall\imdb`\
`python data_str2num.py`
#### Varying Columns
- Refer to `run.sh` in each method folder to execute the code to get the result.
#### Varying Domain Size
- First, the data of the distinct is generated and populated.\
`cd CardinalityEstimationTestbed\Overall\imdb\distinct`\
`python data_process.py`
- Then refer to `run.sh` in mscn and neurocard folder to execute the code to get the result.

### XTZX
- We open source this data set and workload: [XTZX](http://homepages.cwi.nl/~boncz/job/imdb.tgz).
- The method of reproduction of experiments on this data set is similar to the IMDB above.

### forest_power
- Start by generating training and testing queries for different columns.\
`cd CardinalityEstimationTestbed\Overall\forest_power`\
`python generate_sql.py`
- Then refer to `forest.sh, power.sh` in each method folder to execute the code to get the result.

### Update
- Select 10% of the number of rows in each table and add them to the end of the table.
- Refer to `update.sh` in each method folder to execute the code to get the result.
