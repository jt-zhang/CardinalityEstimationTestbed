import os

os.chdir('/home/zhangjintao/Benchmark3')
# cols_4_distinct_1000_corr_5_skew_5
import os

for cols in [2, 4, 6, 8]:
    for distinct in [10, 100, 1000, 10000]:
        for corr in [2, 4, 6, 8]:
            for skew in [2, 4, 6, 8]:
                version = 'cols_' + str(cols) + '_distinct_' + str(distinct) + '_corr_' + str(corr) + '_skew_' + str(skew)

                # mscn
                # os.system('python run_mscn.py --version ' + version)

                # xgb
                # os.system('python run_xgb_nn.py --version ' + version + ' --model xgb')

                # nn
                # os.system('python run_xgb_nn.py --version ' + version + ' --model nn')

                # deepdb
                os.system('python run_deepdb.py --version ' + version)

                print('cols_' + str(cols) + '_distinct_' + str(distinct) + '_corr_' + str(corr) + '_skew_' + str(skew) + 'is OK.')
