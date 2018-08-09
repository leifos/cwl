import numpy as np
from measures.cwl_metrics import CWLMetric

class RBPCWLMetric(CWLMetric):

    def __init__(self, theta=0.9):
        super(CWLMetric, self).__init__()
        self.metric_name = "RBP@{0}".format(theta)
        self.theta = theta

    def c_vector(self, gains, costs=None):
        # precision for k = len(gains)
        #gains =
        cvec = np.dot(np.ones(len(gains)), self.theta)
        return cvec
