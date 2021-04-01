# CardinalityEstimationTestbed
CardinalityEstimationTestbed

## Experiment of synthetic
#### Generate_data_sql
`cd CardinalityEstimationTestbed\Synthetic`\
`python generate_data_sql.py --cols ' + str(cols) + ' --distinct ' + str(distinct) + ' --corr ' + str(corr) + ' --skew ' + str(skew)`
#### Get_sql_truecard
`python get_truecard.py --version cols_' + str(cols) + '_distinct_' + str(distinct) + '_corr_' + str(corr) + '_skew_' + str(skew)`
#### Get_result
`python get_result.py`

## Experiment of overall

### Imdb
- First, the strings in the data table should be converted to numbers.\
`cd CardinalityEstimationTestbed\Overall\imdb`\
`python data_str2num.py`
#### Cols
- Start by generating training test queries for different columns.\
`cd CardinalityEstimationTestbed\Overall\imdb\cols`\
`python generate_sql.py`
- Data tables and queries paths need to be configured, and some methods need Schemafile to be rewritten.
- Then refer to `run.sh` in each method folder to execute the code to get the result.
#### Distinct
- First, the data of the distinct is generated and populated.\
`cd CardinalityEstimationTestbed\Overall\imdb\distinct`\
`python data_process.py`
- Next, generate training test queries of different distinct.\
`python sql_generate.py`
- Data tables and queries paths need to be configured, and some methods need Schemafile to be rewritten.
- Then refer to `run.sh` in each method folder to execute the code to get the result.

### Forest_&_power
- Start by generating training test queries for different columns.\
`cd CardinalityEstimationTestbed\Overall\forest_&_power`\
`python generate_sql.py`
- Data tables and queries paths need to be configured, and some methods need Schemafile to be rewritten.
- Then refer to `run.sh` in each method folder to execute the code to get the result.
