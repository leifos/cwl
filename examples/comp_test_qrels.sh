#!/usr/bin/env bash

echo "Check difference on test_result_file  and test_qrel_file with p10 scores"
python ../scripts/cwl_eval.py  qrels/test_qrel_file results/test_result_file -m metric_lists/precision_metrics | grep "P@10\t" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > p10.cwl
trec_eval qrels/test_qrel_file results/test_result_file -q | grep "P_10 " > tmp
awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > p10.trec
diff -s p10.cwl p10.trec

echo "No Differences when the ranking/scores are unique"


echo ""
echo "Check difference  with AP scores"
python ../scripts/cwl_eval.py  qrels/test_qrel_file results/test_result_file -m metric_lists/test_metrics | grep "\tAP" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > ap.cwl


trec_eval qrels/test_qrel_file results/test_result_file -q | grep "map " > tmp
awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > ap.trec

diff -s ap.cwl ap.trec

echo "No Differences when the ranking/scores are unique"


echo ""
echo "Check difference  with TrAP scores"
python ../scripts/cwl_eval.py  qrels/test_qrel_file results/test_result_file -m metric_lists/test_metrics | grep "TrAP" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > ap.cwl


trec_eval qrels/test_qrel_file results/test_result_file -q | grep "map " > tmp
awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > ap.trec

diff -s ap.cwl ap.trec

echo "No Differences when the ranking/scores are unique"
