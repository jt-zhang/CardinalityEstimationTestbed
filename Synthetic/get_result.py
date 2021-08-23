import os

# os.chdir('/home/zhangjintao/Benchmark3')
# cols_4_distinct_1000_corr_5_skew_5
import os

for cols in [2, 4, 6, 8]:
    for distinct in [10, 100, 1000, 10000]:
        for corr in [2, 4, 6, 8]:
            for skew in [2, 4, 6, 8]:

                version = 'cols_' + str(cols) + '_distinct_' + str(distinct) + '_corr_' + str(corr) + '_skew_' + str(skew)

                # mscn
                os.system('python run_mscn.py --version ' + version)

                # xgb
                os.system('python run_xgb_nn.py --version ' + version + ' --model xgb')
                
                # nn
                os.system('python run_xgb_nn.py --version ' + version + ' --model nn')
                
                # deepdb
                os.system('python run_deepdb.py --version ' + version)
                
                # naru
                os.chdir('./naru')
                os.system('python train_model.py --version '  + version + ' --num-gpus=1 --dataset=dmv --epochs=70 --warmups=8000 --bs=2048 --residual --layers=5 --fc-hiddens=256 --direct-io --column-masking')
                os.system('python eval_model.py --testfilepath ../sql_truecard/ --version '  + version + ' --table '  + version + ' --alias cdcs --dataset=dmv --glob=\'<ckpt from above>\' --num-queries=1000 --residual --layers=5 --fc-hiddens=256 --direct-io --column-masking')
                os.chdir('..')
                
                # bayesian
                os.chdir('./bayesian')
                os.system('python3 eval_model.py --dataset=' + version + ' --num-queries=60 --run-bn')
                os.chdir('..')

                # kde
                os.chdir('./kde')
                os.system('python train_and_test.py --train-query-file ../sql_truecard/' + version + 'train.sql --test-query-file ../sql_truecard/' + version + 'test.sql --single-data-dir ../csvdata_sql --database overall --sample-num=5000 --train-num 1000 --use-gpu --retrain --seed 11')
                os.chdir('..')

                print('cols_' + str(cols) + '_distinct_' + str(distinct) + '_corr_' + str(corr) + '_skew_' + str(skew) + 'is OK.')'''
