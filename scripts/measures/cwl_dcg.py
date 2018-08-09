import numpy as np
import math
from measures.cwl_metrics import CWLMetric


'''
Scaled Discounted Cumulative Gain

'''

class SDCGCWLMetric(CWLMetric):
    def __init__(self, k):
        super(CWLMetric, self).__init__()
        self.metric_name = "SDCG@{0} ".format(k)
        self.k = k

    def c_vector(self, gains, costs=None):

        cvec = []
        for i in range(1,len(gains)+1):
            if i < self.k:
                cvec.append(math.log(i+1,2)/math.log(i+2,2))
            else:
                cvec.append(0.0)

        cvec = np.array(cvec)

        return cvec
