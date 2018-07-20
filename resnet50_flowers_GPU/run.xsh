#!/bin/bash

export MKL_NUM_THREADS=1
export OMP_NUM_THREADS=1
cudaid=${resnet50_cudaid:=0,1,2,3} 
export CUDA_VISIBLE_DEVICES=$cudaid 
# GPU Test
#flowers 64
python ../resnet50_net/train.py --use_gpu=true --reduce_strategy="AllReduce" --batch_size=64 --model=resnet_imagenet --pass_num=5 --gpu_id=$cudaid
python ../resnet50_net/get_gpu_data.py --batch_size=64 --data_set=flowers --reduce_strategy="AllReduce"
python ../resnet50_net/train.py --use_gpu=true --reduce_strategy="Reduce" --batch_size=64 --model=resnet_imagenet --pass_num=5 --gpu_id=$cudaid
python ../resnet50_net/get_gpu_data.py --batch_size=64 --data_set=flowers  --reduce_strategy="Reduce"
for pid in $(ps -ef | grep nvidia-smi | grep -v grep | cut -c 9-15); do
    echo $pid
    kill -9 $pid
done

# Single card
cudaid=${resnet50_cudaid:=0} # use 0-th card as default
export CUDA_VISIBLE_DEVICES=$cudaid 
# GPU Test
#flowers 64
python ../resnet50_net/train.py --use_gpu=true --batch_size=64 --model=resnet_imagenet --pass_num=5 --gpu_id=$cudaid
python ../resnet50_net/get_gpu_data.py --batch_size=64 --data_set=flowers
for pid in $(ps -ef | grep nvidia-smi | grep -v grep | cut -c 9-15); do
    echo $pid
    kill -9 $pid
done