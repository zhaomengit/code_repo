#!/bin/bash

for k in $(ls .)
do
    if [ -d $k ];then
        cd $k
        echo "进入仓库--$k"
        echo ".......$k git pull start......" 
        git pull
        echo ".......$k git pull sucess ......" 
        cd ..
        echo -e "离开仓库--$k\n"
    fi
done

