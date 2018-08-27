#!/usr/bin/env bash

#python ../scripts/cwl_eval.py qrels/test_qrel_file results/test_result_file -m metric_lists/precision_metrics
python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25.res -m metric_lists/precision_metrics > ap_bm25.tsv
python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_pl2.res -m metric_lists/precision_metrics > ap_pl2.tsv
python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25.res -m metric_lists/rbp_metrics > rbp_ap_bm25.tsv
python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_pl2.res -m metric_lists/rbp_metrics > rbp_ap_pl2.tsv
python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_bm25.res -m metric_lists/inst_metrics > inst_ap_bm25.tsv
python ../scripts/cwl_eval.py qrels/trec_ap_51-200.qrels results/ap_pl2.res -m metric_lists/inst_metrics > inst_ap_pl2.tsv

#python ../scripts/cwl_eval.py qrels/trec_aq_303-689.qrels results/aq_bm25.res -m metric_lists/precision_metrics > aq_bm25.tsv
