python preprocessing.py --raw-file /home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/foresttest.sql --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/forest_min_max_vals.csv --datasets-dir /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/Corrskew2/forest --output-dir JOB/forest/test
python preprocessing.py --raw-file /home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/foresttrain.sql --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/forest_min_max_vals.csv --datasets-dir /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/Corrskew2/forest --output-dir JOB/forest/train
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_40/
export PATH=$JAVA_HOME/bin:$PATH
java -classpath target/test-classes:target/quickSel-0.1-jar-with-dependencies.jar -Xmx32g -Xms1g edu.illinois.quicksel.experiments.JOBSpeedComparison /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/quicksel/test/java/edu/illinois/quicksel/resources/JOB/forest/ 5000

# To modify the path of printerror

cd /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/quicksel/test/java/edu/illinois/quicksel/resources/
python print_errors.py --testpath forest/
