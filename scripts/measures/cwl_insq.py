import numpy as np
import math
from measures.cwl_metrics import CWLMetric


class INSQCWLMetric(CWLMetric):

    def __init__(self, T=1.0):
        super(CWLMetric, self).__init__()
        self.metric_name = "INSQ T={0}    ".format(T)
        self.T = T

    def c_vector(self, gains, costs=None):
        # precision for k = len(gains)
        cg = np.cumsum(gains)
        cvec = []
        for i in range(0, len(cg)):
            ci = (((i+1.0)+ (2.0 *self.T)-1.0) / ((i+1.0)+ (2.0 * self.T)))**2.0
            cvec.append(ci)

        cvec = np.array(cvec)
        return cvec
