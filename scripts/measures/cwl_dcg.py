import numpy as np
import math
from measures.cwl_metrics import CWLMetric


'''
Discounted Cumulative Gain: scaled so that the discount is a probability distribution

@article{Jarvelin:2002:CGE:582415.582418,
 author = {J\"{a}rvelin, Kalervo and Kek\"{a}l\"{a}inen, Jaana},
 title = {Cumulated Gain-based Evaluation of IR Techniques},
 journal = {ACM Trans. Inf. Syst.},
 volume = {20},
 number = {4},
 year = {2002},
 pages = {422--446},
 numpages = {25},
 url = {http://doi.acm.org/10.1145/582415.582418},

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
