python preprocessing.py --raw-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/cols-sql/4/test-only4-num.sql --min-max-file /home/sunji/CardinalityEstimationBenchmark/learnedcardinalities-master/data/column_min_max_vals.csv --datasets-dir /home/sunji/CardinalityEstimationBenchmark/Distinct-Value-High/ --output-dir JOB/cols-sql/4/test
python preprocessing.py --raw-file /home/sunji/CardinalityEstimationBenchmark/train-test-data/cols-sql/4/train-4-num.sql --min-max-file /home/sunji/CardinalityEstimationBenchmark/learnedcardinalities-master/data/column_min_max_vals.csv --datasets-dir /home/sunji/CardinalityEstimationBenchmark/Distinct-Value-High/ --output-dir JOB/cols-sql/4/train
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_40/
export PATH=$JAVA_HOME/bin:$PATH
java -classpath target/test-classes:target/quickSel-0.1-jar-with-dependencies.jar -Xmx32g -Xms1g edu.illinois.quicksel.experiments.JOBSpeedComparison /home/sunji/CardinalityEstimationBenchmark/quicksel/test/java/edu/illinois/quicksel/resources/JOB/cols-sql/4/ 5000