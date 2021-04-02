import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='mscn')

parser.add_argument('--version', type=str, help='datasets_dir', default='cols_4_distinct_1000_corr_5_skew_5')
parser.add_argument('--model', type=str, help='nn||xgb', default='nn')
args = parser.parse_args()
version = args.version
model = args.model

run = 'python run.py --train-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + 'train.sql' + ' --test-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + 'test.sql' + \
    ' --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + '_min_max_vals.csv ' + '--model ' + model + ' --version ' + version

os.chdir('/home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/xgboost')
os.system(run)




'''
python run.py --train-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/skew-sql/skew2/train-num.sql --test-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/skew-sql/skew2/test-num.sql --min-max-file /home/sunji/CardinalityEstimationBenchmark/learnedcardinalities-master/data/skew2_min_max_vals.csv --model xgb
'''
