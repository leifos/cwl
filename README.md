# C/W/L Evaluation Script
An evaluation script based on the C/W/L framework that is TREC Compatible and provides a replacement for INST_EVAL, RBP_EVAL and TREC_EVAL


Usage: cwl_eval.py <gain_file> <result_file> <cost_file> <metrics_file>
Usage: cwl_eval.py <gain_file> <result_file>
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
