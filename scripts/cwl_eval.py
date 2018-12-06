__author__ = "Leif @leifos Azzopardi"


import os
import argparse
from seeker.trec_qrel_handler import TrecQrelHandler
from ruler.cwl_ruler import RankingMaker, Ranking, CWLRuler

def read_in_cost_file(cost_file):

    costs = dict()
    with open(cost_file, "r") as cf:
        while cf:
            line = cf.readline()
            if not line:
                break
            (element_type, cost) = line.split()
            element_type = element_type.strip()
            costs[element_type] = float(cost)

    return costs


def check_file_exists(filename):
    if filename and not os.path.exists(filename):
        print("{0} Not Found".format(filename))
        quit(1)


def main(results_file, qrel_file, cost_file=None, metrics_file=None, bib_file=None, colnames = False):

    qrh = TrecQrelHandler(qrel_file)

    costs = None
    # read in cost file - if cost file exists
    if cost_file:
        costs = read_in_cost_file(cost_file)
    cwl_ruler = CWLRuler(metrics_file)

    curr_topic_id = None
    ranking_maker = None

    if colnames:
        print("Topic\tMetric\tEU/I\tEU\tEC/I\tEC\tI")

    with open(results_file,"r") as rf:
        while rf:
            line = rf.readline()
            if not line:
                break
            (topic_id, element_type, doc_id, rank, score, run_id) = line.split()
            doc_id = doc_id.strip()

            if (topic_id == curr_topic_id):
                # build vectors
                ranking_maker.add(doc_id, element_type)
            else:
                if curr_topic_id is not None:
                    #Perform the Measurements
                    #ranking.report()
                    cwl_ruler.measure(ranking_maker.get_ranking())
                    cwl_ruler.report()

                # new topic
                curr_topic_id = topic_id

                # reset seen list

                ranking_maker = RankingMaker(curr_topic_id, qrh, costs)
                ranking_maker.add(doc_id, element_type)

        #Perform the Measurements on the last topic
        #ranking_maker.report()
        cwl_ruler.measure(ranking_maker.get_ranking())
        cwl_ruler.report()


        #Perform aggregration over all topics

        #Compute residuals?
    if bib_file:
        cwl_ruler.save_bibtex(bib_file)

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser(description="CWL Evaluation Metrics")
    arg_parser.add_argument("gain_file", help="A TREC Formatted Qrel File with relevance scores used as gains. Gain values should be between zero and one. Four column tab/space sep file with fields: topic_id unused doc_id gain")
    arg_parser.add_argument("result_file", help="TREC formatted results file. Six column tab/space sep file with fields: topic_id element_type doc_id rank score run_id")
    arg_parser.add_argument("-c", "--cost_file", help="Costs associated with each element type specified in result file.", required=False)
    arg_parser.add_argument("-m", "--metrics_file", help="The list of metrics that are to be reported. If not specified, a set of default metrics will be reported. Tab/space sep file with fields: metric_name params", required=False)
    arg_parser.add_argument("-b", "--bib_file", help="If specified, then the BibTeX for the measures used will be saved to the filename given.", required=False)
    arg_parser.add_argument("-n", "--colnames", help="Includes headings in the output", required=False, action="store_true")


    args = arg_parser.parse_args()

    gain_file = args.gain_file
    result_file = args.result_file

    cost_file = None
    if args.cost_file:
        cost_file = args.cost_file

    metrics_file = None
    if args.metrics_file:
        metrics_file = args.metrics_file

    bib_file = None
    if args.bib_file:
        bib_file = args.bib_file

    colnames = False
    if args.colnames:
        colnames = True

    check_file_exists(result_file)
    check_file_exists(gain_file)
    check_file_exists(cost_file)
    check_file_exists(metrics_file)

    main(result_file, gain_file, cost_file, metrics_file, bib_file, colnames)
