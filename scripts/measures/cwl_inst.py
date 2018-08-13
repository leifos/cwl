import numpy as np
import math
from measures.cwl_metrics import CWLMetric


'''
# INST is from Moffat et al., Australasian Document Computing Symposium 2015
C.fn.INST <- function(T) {
  # depends on rank and how much of what we expected has been seen so far
  function(R, i) {
    Ti <- T-cumsum(R)
    ((i+T+Ti-1) / (i+T+Ti)) ** 2
  }
}
'''

class INSTCWLMetric(CWLMetric):

    def __init__(self, T = 1.0):
        super(CWLMetric, self).__init__()
        self.metric_name = "INST T={0}    ".format(T)
        self.T = T

    def c_vector(self, gains, costs=None):
        # precision for k = len(gains)
        cg = np.subtract(self.T, np.cumsum(gains))
        cvec = []
        for i in range(0, len(cg)):
            ci = (((i+1.0)+self.T+cg[i]-1.0) / ((i+1.0)+self.T+cg[i]))**2.0
            cvec.append(ci)

        cvec = np.array(cvec)
        return cvec
