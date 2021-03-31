#!/bin/bash
for i in 2 4 6 8
do
    for j in 10 100 1000 10000
    do
        for k in 2 4 6 8
        do
            for l in 2 4 6 8
            do
                python3 train_model.py --num-gpus=1 --dataset=cols_${i}_distinct_${j}_corr_${k}_skew_${l} --epochs=100 --residual --direct-io --warmups=2000 --layers=5 --fc-hiddens=256  --column-masking
                python3 eval_model.py --dataset=cols_${i}_distinct_${j}_corr_${k}_skew_${l} --glob="cols_${i}_distinct_${j}_corr_${k}_skew_${l}*.pt" --num-queries=1000 --residual --direct-io --layers=5 --fc-hiddens=256 --column-masking
	    done
        done
    done
done
    
