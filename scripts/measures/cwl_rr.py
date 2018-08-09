import numpy as np
from measures.cwl_metrics import CWLMetric

'''
Reciprocal Rank

and 

ERR
'''


class RRCWLMetric(CWLMetric):

    def __init__(self):
        super(CWLMetric, self).__init__()
        self.metric_name = "RR     "

    def c_vector(self, gains, costs=None):

        cvec = []
        found_gain = False
        for g in gains:
            if (g > 0.0) and not found_gain:
                cvec.append(1.0)
                found_gain = True
            else:
                cvec.append(0.0)

        cvec = np.array(cvec)
        return cvec


class ERRCWLMetric(CWLMetric):

    def __init__(self):
        super(CWLMetric, self).__init__()
        self.metric_name = "ERR     "

    def c_vector(self, gains, costs=None):
        '''

        :param gains: all gains must be between one and zero
        :param costs: cost vectors can be any real value, i.e. can be greater than one, but is not used for ERR.
        :return: the continuation vector for ERR
        '''

        cvec = np.subtract(np.ones(len(gains))-gains)

        return cvec
