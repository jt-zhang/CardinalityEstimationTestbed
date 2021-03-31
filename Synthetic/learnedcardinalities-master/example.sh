cd mscn
'python preprocessing.py --datasets-dir /home/zhangjintao/Benchmark3/csvdata_sql --raw-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + \
    'train.sql' + ' --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + '_min_max_vals.csv ' + '--table ' + version + ' --alias cdcs'
'python preprocessing.py --datasets-dir /home/zhangjintao/Benchmark3/csvdata_sql --raw-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + \
    'test.sql' + ' --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + '_min_max_vals.csv ' + '--table ' + version + ' --alias cdcs'
cd ..
python train.py --min-max-file /home/sunji/CardinalityEstimationBenchmark/learnedcardinalities-master/data/skew4_min_max_vals.csv --queries 10000 --epochs 100 --batch 1024 --hid 256 --train-query-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/skew-sql/skew4/train-num.sql --test-query-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/skew-sql/skew4/test-num.sql --train
python train.py --min-max-file /home/sunji/CardinalityEstimationBenchmark/learnedcardinalities-master/data/skew4_min_max_vals.csv --queries 10000 --epochs 100 --batch 1024 --hid 256 --train-query-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/skew-sql/skew4/train-num.sql --test-query-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/skew-sql/skew4/test-num.sql

'python preprocessing.py --datasets-dir /home/zhangjintao/Benchmark3/csvdata_sql --raw-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + \
    'train.sql' + ' --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + '_min_max_vals.csv ' + '--table ' + version + ' --alias cdcs'
'python preprocessing.py --datasets-dir /home/zhangjintao/Benchmark3/csvdata_sql --raw-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + \
    'test.sql' + ' --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + '_min_max_vals.csv ' + '--table ' + version + ' --alias cdcs'
'python train.py --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + \
    '_min_max_vals.csv --queries 10000 --epochs 100 --batch 1024 --hid 256 --train-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + \
    'train.sql --test-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + 'test.sql --train'
'python train.py --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/' + version + \
    '_min_max_vals.csv --queries 10000 --epochs 100 --batch 1024 --hid 256 --train-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + \
    'train.sql --test-query-file /home/zhangjintao/Benchmark3/sql_truecard/' + version + 'test.sql'