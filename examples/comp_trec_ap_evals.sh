#!/usr/bin/env bash

echo "Differences on ap_bm25.res with p10 scores"

python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25.res -m metric_lists/precision_metrics | grep "P@10 " > tmp

awk '{print $1 " " $3}' tmp > tmp2
 sort -n tmp2 > p10.cwl

trec_eval qrels/trec_ap_51-200.qrels results/ap_bm25.res -q | grep "P_10 " > tmp

awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > p10.trec

diff p10.cwl p10.trec

echo "Differences between precision at 10 values is due to ties"
echo "TREC_EVAL ignores rank, and sorts by {score} and reverse {docid}."

echo ""
echo "Check difference  with AP scores"
python ../scripts/cwl_eval.py  qrels/trec_ap_51-200.qrels results/ap_bm25.res | grep "AP" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > ap.cwl


trec_eval qrels/trec_ap_51-200.qrels results/ap_bm25.res -q | grep "map " > tmp
awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > ap.trec

diff -s ap.cwl ap.trec

echo "Differences b/w AP values"
