__author__ = "Leif Azzopardi"

from measures.cwl_metrics import CWLMetric, PrecisionCWLMetric, RBPCWLMetric, SDCGCWLMetric, RRCWLMetric
from measures.cwl_metrics import APCWLMetric
class Ranking(object):
    def __init__(self, topic_id, gain_handler, cost_handler=None):
        self.topic_id = topic_id
        self.qgains = gain_handler
        self.qcosts = cost_handler
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
        # Add in object accessor to map element type to costs for the docid
        return 1.0

    def report(self):
        print(self.topic_id,self.gains)
        print(self.topic_id,self.costs)



class CWLRuler(object):

    def __init__(self, metrics_file=None):
        #add the metrics to the list
        self.metrics = [ CWLMetric(), PrecisionCWLMetric(20),
                         PrecisionCWLMetric(5), PrecisionCWLMetric(1),
                         RBPCWLMetric(0.5), RBPCWLMetric(0.9),
                         SDCGCWLMetric(10),SDCGCWLMetric(5),
                         RRCWLMetric(), APCWLMetric()]

    def measure(self, ranking):
        for metric in self.metrics:
            metric.measure(ranking)

    def report(self):
        for metric in self.metrics:
            metric.report()

