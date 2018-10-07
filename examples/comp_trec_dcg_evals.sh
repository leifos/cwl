#!/usr/bin/env bash

echo "Differences on ap_bm25.res with dcg scores"

python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25.res  | grep "SDCG" > tmp

awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > sdcg.cwl
awk '{print $2}' sdcg.cwl > sdcg.csv

trec_eval -m all_trec qrels/trec_ap_51-200.qrels results/ap_bm25_resorted.res -q | grep "ndcg_cut_10 " > tmp

awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > ndcg.trec
awk '{print $2}' ndcg.trec > ndcg.csv

diff -s sdcg.csv ndcg.csv
