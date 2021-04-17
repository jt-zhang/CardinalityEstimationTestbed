# CardinalityEstimationTestbed
CardinalityEstimationTestbed

## Experiment of synthetic
#### Generate_data_sql
`cd CardinalityEstimationTestbed\Synthetic`\
`python generate_data_sql.py --cols [COLUMNS_NUM] --distinct [DOMAIN_SIZE] --corr [CORRELATION] --skew [SKERNESS]`
#### Get_sql_truecard
`python get_truecard.py --version cols_[COLUMNS_NUM]_distinct_[DOMAIN_SIZE]_corr_[CORRELATION]_skew_[SKEWNESS]`
#### Get_result
`python get_result.py` Then experimental results of all methods can be obtained.\
If only experimental results of some methods should be obtained, other methods can be commented out in `get_result.py`.


## Experiment of overall
### Real Datasets download
- Download the [IMDB](http://homepages.cwi.nl/~boncz/job/imdb.tgz) data tables to: `../train-test-data/imdbdataset-str`
- Download the [forest, power](http://archive.ics.uci.edu/) data tables to: `../train-test-data/forest_&_power-data-sql`\
Begin by doing a simple job on the table, removing some unused columns. For Forest We use ﬁrst 10 numeric attributes; For Power We used the 7 numeric attributes after the ﬁrst two attributes (date and time).
### Imdb
- First, the strings in the data tables should be converted to numbers.\
`cd CardinalityEstimationTestbed\Overall\imdb`\
`python data_str2num.py`
#### Varying \#Columns
- Start by generating training and testing queries queries for different columns.\
`cd CardinalityEstimationTestbed\Overall\imdb\cols`\
`python generate_sql.py`
- Then refer to `run.sh` in each method folder to execute the code to get the result.
#### Varying Domain Size
- First, the data of the distinct is generated and populated.\
`cd CardinalityEstimationTestbed\Overall\imdb\distinct`\
`python data_process.py`
- Next, generate training and testing queries of different distinct.\
`python sql_generate.py`
- Then refer to `run.sh` in each method folder to execute the code to get the result.

### Forest_&_power
- Start by generating training and testing queries for different columns.\
`cd CardinalityEstimationTestbed\Overall\forest_&_power`\
`python generate_sql.py`
- Then refer to `forest.sh, power.sh` in each method folder to execute the code to get the result.
