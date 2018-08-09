__author__ = "Leif @leifos Azzopardi"


import os
import sys
import re
import argparse
#from measures.tar_rulers import TarRuler, TarAggRuler
from seeker.trec_qrel_handler import TrecQrelHandler
from measures.cwl_ruler import Ranking, CWLRuler



def main(results_file, qrel_file):

    qrh = TrecQrelHandler(qrel_file)

    cwl_ruler = CWLRuler()

    curr_topic_id = None

    ranking = None

    with open(results_file,"r") as rf:
        while rf:
            line = rf.readline()
            if not line:
                break
            (topic_id, element_type, doc_id, rank, score, run_id) = line.split()
            doc_id = doc_id.strip()

            if (topic_id == curr_topic_id):
                # build vectors
                ranking.add(doc_id, element_type)
            else:
                if curr_topic_id is not None:
                    #Perform the Measurements
                    ranking.report()
                    cwl_ruler.measure(ranking)
                    cwl_ruler.report()

                # new topic
                curr_topic_id = topic_id
                # reset seen list

                ranking = Ranking(curr_topic_id, qrh)
                ranking.add(doc_id, element_type)

        #Perform the Measurements on the last topic
        ranking.report()
        cwl_ruler.measure(ranking)
        cwl_ruler.report()


        #Perform aggregration over all topics

        #Compute residuals?


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser(description="CWL Evaluation Metrics")
    arg_parser.add_argument("gain_file", help="A TREC Formatted Qrel File with relevance scores used as gains. Gain values should be between zero and one. Four column tab/space sep file with fields: topic_id unused doc_id gain")
    arg_parser.add_argument("result_file", help="TREC formatted results file. Six column tab/space sep file with fields: topic_id element_type doc_id rank score run_id")
    arg_parser.add_argument("-c", "--cost_file", help="Costs associated with each element type specified in result file.", required=False)
    arg_parser.add_argument("-m", "--metrics_file", help="The list of metrics that are to be reported. If not specified, a set of default metrics will be reported. Tab/space sep file with fields: metric_name params", required=False)

    args = arg_parser.parse_args()

    gain_file = args.gain_file
    result_file = args.result_file

    if not os.path.exists( result_file ):
        print("Result File Not Found")
        quit(1)
    if not os.path.exists(gain_file):
        print("Gain/Qrel Not Found")
        quit(1)
    main(result_file, gain_file)
