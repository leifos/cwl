__author__ = "Leif Azzopardi"

from measures.cwl_metrics import *
from measures.cwl_precision import *
from measures.cwl_rbp import *
from measures.cwl_rr import *
from measures.cwl_ap import *
from measures.cwl_dcg import *
from measures.cwl_inst import *
from measures.cwl_insq import *
from measures.cwl_tbg import *
from measures.cwl_bpm import *
from measures.cwl_umeasure import *
from measures.cwl_ift import *

class Ranking(object):
    def __init__(self, topic_id, gain_handler, cost_dict=None):
        self.topic_id = topic_id
        self.qgains = gain_handler
        self.qcosts = cost_dict
        self.gains = []
        self.costs = []
        #self.seen = {}

    def add(self, doc_id, element_type):
        gain = self.qgains.get_value(self.topic_id, doc_id)
        self.gains.append(gain)
        cost = self.get_cost(doc_id, element_type)
        self.costs.append(cost)

    def get_cost(self, doc_id, element_type):
        if self.qcosts is None:
            return 1.0
        else:
            if element_type in self.qcosts:
                return self.qcosts[element_type]
            else:
                return 1.0
        # Add in object accessor to map element type to costs for the docid
        return 1.0

    def report(self):
        #print(self.topic_id,self.gains)
        #print(self.topic_id,self.costs)
        pass


class CWLRuler(object):

    def __init__(self, metrics_file=None):
        #add the metrics to the list
        self.metrics = [
                         PrecisionCWLMetric(20),
                         PrecisionCWLMetric(10),
                         PrecisionCWLMetric(5),
                         PrecisionCWLMetric(1),
                         RBPCWLMetric(0.5),
                         RBPCWLMetric(0.9),
                         SDCGCWLMetric(10),
                         SDCGCWLMetric(5),
                         RRCWLMetric(),
                         APCWLMetric(),
                         INSTCWLMetric(2),
                         INSTCWLMetric(1),
                         INSQCWLMetric(2),
                         INSQCWLMetric(1),
                         BPMCWLMetric(1,1000),
                         BPMCWLMetric(1000,10),
                         BPMCWLMetric(1.2,10),
                         BPMDCWLMetric(1,1000),
                         BPMDCWLMetric(1000,10),
                         BPMDCWLMetric(1.2,10),
                         UMeasureCWLMetric(50),
                         UMeasureCWLMetric(10),
                         TBGCWLMetric(22),
                         IFTGoalCWLMetric(2.0, 0.9, 1),
                         IFTGoalCWLMetric(2.0, 0.9, 10),
                         IFTGoalCWLMetric(2.0, 0.9, 100),
                         IFTRateCWLMetric(0.2, 0.9, 1),
                         IFTRateCWLMetric(0.2, 0.9, 10),
                         IFTRateCWLMetric(0.2, 0.9, 100),
                         IFTGoalRateCWLMetric(2.0,0.9,10, 0.2, 0.9, 10),
                         IFTGoalRateCWLMetric(2.0,0.9,100, 0.2, 0.9, 100),
                         ]

        '''
                         PrecisionCWLMetric(20),
                         PrecisionCWLMetric(10),
                         PrecisionCWLMetric(5),
                         PrecisionCWLMetric(1),
                         RBPCWLMetric(0.5),
                         RBPCWLMetric(0.9),
                         SDCGCWLMetric(10),
                         SDCGCWLMetric(5),
                         RRCWLMetric(),
                         APCWLMetric(),
                         INSTCWLMetric(2),
                         INSTCWLMetric(1),
                         INSQCWLMetric(2),
                         INSQCWLMetric(1)
                         
                         ]
        '''


    def measure(self, ranking):
        for metric in self.metrics:
            metric.measure(ranking)

    def report(self):
        for metric in self.metrics:
            metric.report()

