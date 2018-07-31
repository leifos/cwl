__author__ = "Leif @leifos Azzopardi"


import os
import sys
import re
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


def usage(args):
    print("Usage: {0} <gain_file> <result_file> <cost_file> <metrics_file>".format(args[0]))
    print("Usage: {0} <gain_file> <result_file>".format(args[0]))

    print("<gain_file>   : A TREC Formatted Qrel File with relevance scores used as gains")
    print("                Four column tab/space sep file with fields: topic_id unused doc_id gain")

    print("<cost_file>   : Costs associated with element type")
    print("<cost_file>   : If not specified, costs default to one for all elements")

    print("                Two column tab/space sep file with fields: element_type element_cost")
    print("<result_file> : A TREC Formatted Result File")
    print("                Six column tab/space sep file with fields: topic_id element_type doc_id rank score run_id")
    print("<metrics_file>: The list of metrics that are to be reported")
    print("                If not specified, a set of default metrics will be reported")
    print("                Tab/space sep file with fields: metric_name params")


if __name__ == "__main__":
    filename = None
    if len(sys.argv) >= 2:
        qrels = sys.argv[1]

    if len(sys.argv)==3:
        results = sys.argv[2]
    else:
        usage(sys.argv)
        exit(1)

    if os.path.exists( results ) and os.path.exists(qrels):
        main(results,qrels)
    else:
        usage(sys.argv)
