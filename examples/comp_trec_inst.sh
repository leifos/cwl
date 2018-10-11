#!/usr/bin/env bash

echo "Differences on ap_bm25.res with inst scores using inst_eval.py"

python /Users/leif/Code/inst_eval/inst_eval.py qrels/test_qrel_file results/test_result_file TperQuery1 > tmp

grep "inst_min" tmp > tmp2
awk '{print $2 " " $3}' tmp2 > tmp3
sort -n tmp3 | grep -v "all" > inst.inst
awk '{print $2}' inst.inst > inst.inst.csv

python ../scripts/cwl_eval.py qrels/test_qrel_file results/test_result_file  -m metric_lists/test_metrics | grep "INST" > tmp

awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > inst.cwl
awk '{print $2}' inst.cwl > inst.cwl.csv

diff -s inst.inst.csv inst.cwl.csv
