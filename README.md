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
