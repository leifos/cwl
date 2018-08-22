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

As a result, all metrics report approximations of the Expected Utility per Item (EU/I),
Expected Utility (EU), Expected Cost per Item (EC/I), Expected Cost (EC), and the Expected Number of Items to be Examined (I)

Note that:

EU = EU/I * I

and

EC = EC/I * I

