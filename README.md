# C/W/L Evaluation Script
An evaluation script based on the C/W/L framework
that is TREC Compatible and provides a replacement
for INST_EVAL, RBP_EVAL, TBG_EVAL, UMeasure, TREC_EVAL


Usage: cwl_eval.py <gain_file> <result_file> -c <cost_file> -m <metrics_file>

Usage: cwl_eval.py <gain_file> <result_file>

Usage: cwl_eval.py -h

<gain_file>   : A TREC Formatted Qrel File with relevance scores used as gains
                Four column tab/space sep file with fields: topic_id unused doc_id gain

<cost_file>   : Costs associated with element type

<cost_file>   : If not specified, costs default to one for all elements
                Two column tab/space sep file with fields: element_type element_cost

<result_file> : A TREC Formatted Result File
                Six column tab/space sep file with fields: topic_id element_type doc_id rank score run_id

<metrics_file>: The list of metrics that are to be reported
                If not specified, a set of default metrics will be reported
                Tab/space sep file with fields: metric_name params



**Example without using a cost file.**

python cwl_eval.py test_qrel_file test_result_file


**Example with using a cost file.**

Example: python cwl_eval.py test_qrel_file test_result_file -c cost_file


**Output**
A seven column tab/space seperated file that contains:

- Topic ID
- Metric Name
- Expected Utility Per Item (EU/I)
- Expected Utility (EU)
- Expected Cost per Item (EC/I)
- Expected Cost (EC)
- Expected Number of Items to be Examined (I)






Metrics within CWL EVAL
-----------------------
For each of the metrics provided in cwl_eval.py, the user model for each
measure has been extracted and encoded within the C/W/L framework.

All weightings have been converted to probabilities.

As a result, all metrics report a series of values (not a single value):
 - Expected Utility per Item (EU/I),
 - Expected Utility (EU) or (ETU),
 - Expected Cost per Item (EC/I),
 - Expected Cost (EC) or (ETC)
 - Expected Number of Items to be Examined (I)

However, all the values are instrinically related, such that:

EU = EU/I * I

and

EC = EC/I * I

and

ER = EU/EC

where ER is the expected rate of gain over cost.

If the cost per item is 1.0, then the expected cost per item is 1.0,
and the expected cost EC will be equal to I.

Costs can be specified in whatever unit is desired. i.e seconds, characters, words, etc.

**List of Metrics**

- RR - Reciprocal Rank
- ERR - Expected Reciprocal Rank
- BPM-Static - Bejewelled Player Model  - Static
- BPM-Dynamic - Bejewelled Player Model - Dynamic
- UMeasure - U-Measure
- TBG - Time Biased Gain
- P@k - Precision At k
- RBP - Rank Biased Precision
- IFT-C1 - Information Foraging Theory (Goal)
- IFT-C2 - Information Foraging Theory (Rate)
- IFT-C1-C2 - Information Foraging Theory (Goal and Rate)
- INST T
- INSQ T
- DCG@k - Discounted Cumulative Gain at k

**Sample Output from cwl_eval.py**

| T1 | P@20                                              | 0.150 | 3.000 | 1.000 | 20.000 | 20.000 |
|----|---------------------------------------------------|-------|-------|-------|--------|--------|
| T1 | P@10                                              | 0.300 | 3.000 | 1.000 | 10.000 | 10.000 |
| T1 | P@5                                               | 0.360 | 1.800 | 1.000 | 5.000  | 5.000  |
| T1 | P@1                                               | 1.000 | 1.000 | 1.000 | 1.000  | 1.000  |
| T1 | RBP@0.5                                           | 0.566 | 1.132 | 1.000 | 2.000  | 2.000  |
| T1 | RBP@0.9                                           | 0.214 | 2.136 | 1.000 | 10.000 | 10.000 |
| T1 | SDCG-k@10                                         | 0.380 | 1.726 | 1.000 | 4.544  | 4.544  |
| T1 | SDCG-k@5                                          | 0.461 | 1.358 | 1.000 | 2.948  | 2.948  |
| T1 | RR                                                | 1.000 | 1.000 | 1.000 | 1.000  | 1.000  |
| T1 | AP                                                | 0.397 | 1.907 | 1.000 | 4.800  | 4.800  |
| T1 | INST-T=2                                          | 0.401 | 1.303 | 1.000 | 3.242  | 3.247  |
| T1 | INST-T=1                                          | 0.680 | 1.071 | 1.000 | 1.574  | 1.575  |
| T1 | INSQ-T=2                                          | 0.316 | 1.428 | 1.000 | 4.509  | 4.525  |
| T1 | INSQ-T=1                                          | 0.465 | 1.198 | 1.000 | 2.572  | 2.576  |
| T1 | BPM-Static-T=1-K=1000                             | 1.000 | 1.000 | 1.000 | 1.000  | 1.000  |
| T1 | BPM-Static-T=1000-K=10                            | 0.300 | 3.000 | 1.000 | 10.000 | 10.000 |
| T1 | BPM-Static-T=1.2-K=10                             | 0.400 | 1.200 | 1.000 | 3.000  | 3.000  |
| T1 | BPM-Dynamic-T=1-K=1000-hb=1.0-hc=1.0              | 1.000 | 1.000 | 1.000 | 1.000  | 1.000  |
| T1 | BPM-Dynamic-T=1000-K=10-hb=1.0-hc=1.0             | 0.300 | 3.000 | 1.000 | 10.000 | 10.000 |
| T1 | BPM-Dynamic-T=1.2-K=10-hb=1.0-hc=1.0              | 0.400 | 1.200 | 1.000 | 3.000  | 3.000  |
| T1 | U-L@50                                            | 0.109 | 2.772 | 1.000 | 25.500 | 25.500 |
| T1 | U-L@10                                            | 0.338 | 1.860 | 1.000 | 5.500  | 5.500  |
| T1 | TBG-H@22                                          | 0.083 | 2.676 | 1.000 | 32.242 | 32.242 |
| T1 | IFT-C1-T@2.0-b1@0.9-R1@1                          | 0.456 | 1.323 | 1.000 | 2.903  | 2.903  |
| T1 | IFT-C1-T@2.0-b1@0.9-R1@10                         | 0.308 | 2.078 | 1.000 | 6.738  | 6.738  |
| T1 | IFT-C1-T@2.0-b1@0.9-R1@100                        | 0.289 | 2.224 | 1.000 | 7.698  | 7.698  |
| T1 | IFT-C2-A@0.2-b2@0.9-R2@1                          | 0.463 | 1.255 | 1.000 | 2.711  | 2.711  |
| T1 | IFT-C2-A@0.2-b2@0.9-R2@10                         | 0.293 | 2.040 | 1.000 | 6.965  | 6.965  |
| T1 | IFT-C2-A@0.2-b2@0.9-R2@100                        | 0.197 | 2.994 | 1.000 | 15.208 | 15.208 |
| T1 | IFT-C1-C2-T@2.0-b1@0.9-R1@10-A@2.0-b2@0.9-R2@10   | 0.329 | 1.804 | 1.000 | 5.487  | 5.487  |
| T1 | IFT-C1-C2-T@2.0-b1@0.9-R1@100-A@2.0-b2@0.9-R2@100 | 0.289 | 2.223 | 1.000 | 7.697  | 7.697  |
