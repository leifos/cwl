#!/usr/bin/env bash

echo "Differences on ap_bm25.res with p10 scores"

python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25.res -m metric_lists/precision_metrics | grep "P@10\t" > tmp

awk '{print $1 " " $3}' tmp > tmp2
 sort -n tmp2 > p10.cwl

trec_eval qrels/trec_ap_51-200.qrels results/ap_bm25.res -q | grep "P_10 " > tmp

awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > p10.trec

diff p10.cwl p10.trec

echo "Differences between precision at 10 values is due to ties"
echo "TREC_EVAL ignores rank, and sorts by {score} and reverse {docid}."


echo "Differences on ap_bm25_resorted.res with p10 scores"

python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25_resorted.res -m metric_lists/precision_metrics | grep "P@10\t" > tmp

awk '{print $1 " " $3}' tmp > tmp2
 sort -n tmp2 > p10_resorted.cwl

diff -s p10_resorted.cwl p10.trec

echo "No differences when result file is sorted a priori to match TREC EVAL sorting."
echo " i.e. sort -k1b,1 -k5nr,5 -k3r,3 ap_bm25.res > ap_bm25_resorted.res "

echo ""
echo "Check difference  ap_bm25.res with AP scores"
python ../scripts/cwl_eval.py  qrels/trec_ap_51-200.qrels results/ap_bm25.res | grep "AP" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > ap.cwl


trec_eval qrels/trec_ap_51-200.qrels results/ap_bm25.res -q | grep "map " > tmp
awk '{print $2 " " $3}' tmp > tmp2
sort -n tmp2 | grep -v "all" > ap.trec

diff -s ap.cwl ap.trec

echo "Differences b/w AP values"

echo ""
echo "Now re-sort the TREC result file like TREC_EVAL does.... and try again"
echo ""
echo "Check difference on ap_bm25_resorted.res with AP scores"
python ../scripts/cwl_eval.py  qrels/trec_ap_51-200.qrels results/ap_bm25_resorted.res -m metric_lists/test_metrics | grep "/tAP" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > ap_resorted.cwl

diff -s ap_resorted.cwl ap.trec




echo ""
echo "Now try with TrAP - which considers the total number of relevant documents - like AP in TREC does"
echo ""
echo "Check difference on ap_bm25_resorted.res with TrAP scores"
python ../scripts/cwl_eval.py  qrels/trec_ap_51-200.qrels results/ap_bm25_resorted.res -m metric_lists/test_metrics | grep "TrAP" > tmp
awk '{print $1 " " $3}' tmp > tmp2
sort -n tmp2 > tr_ap_resorted.cwl

diff -s tr_ap_resorted.cwl ap.trec

echo "Hmmm... Rounding Error for Topic 186... or is it something deeper"
