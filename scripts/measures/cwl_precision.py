import numpy as np
from measures.cwl_metrics import CWLMetric

class PrecisionCWLMetric(CWLMetric):

    def __init__(self, k=10):
        super(CWLMetric, self).__init__()
        self.metric_name = "P@{0}    ".format(k)
        self.k = k

    def c_vector(self, gains, costs=None):
        # precision for k = len(gains)
        cvec = np.ones(self.k-1)
        cvec = self.pad_vector(cvec, gains)
        return cvec
