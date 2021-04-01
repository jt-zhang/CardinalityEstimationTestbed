python preprocessing.py --raw-file /home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/powertest.sql --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/power_min_max_vals.csv --datasets-dir /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/Corrskew2/power --output-dir JOB/power/test
python preprocessing.py --raw-file /home/zhangjintao/Benchmark3/otherdataset/csvdata_sql/powertrain.sql --min-max-file /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/learnedcardinalities-master/data/power_min_max_vals.csv --datasets-dir /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/Corrskew2/power --output-dir JOB/power/train
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_40/
export PATH=$JAVA_HOME/bin:$PATH
java -classpath target/test-classes:target/quickSel-0.1-jar-with-dependencies.jar -Xmx32g -Xms1g edu.illinois.quicksel.experiments.JOBSpeedComparison /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/quicksel/test/java/edu/illinois/quicksel/resources/JOB/power/ 5000

# To modify the path of a Print Error

cd /home/zhangjintao/Benchmark3/CardinalityEstimationBenchmark/quicksel/test/java/edu/illinois/quicksel/resources/
python print_errors.py --testpath ./power/
