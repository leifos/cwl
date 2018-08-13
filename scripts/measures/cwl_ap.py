import numpy as np
import math
from measures.cwl_metrics import CWLMetric


'''
Average Precision

#todo(leifos): Can we do GAP and other variations of AP?
'''

class APCWLMetric(CWLMetric):
    def __init__(self):
        super(CWLMetric, self).__init__()
        self.metric_name = "AP     "

    def c_vector(self, gains, costs=None):
        '''
        Doesn't metric need to know all the relevant items??
        :param gains:
        :param costs:
        :return:
        '''
        cvec = []
        for i in range(0,len(gains)):

            bot = np.sum(gains[i:len(gains)]/(i+1.0))
            top = np.sum(gains[(i+1):len(gains)]/(i+1.0))

            if top > 0.0:
                cvec.append(top/bot)
            else:
                cvec.append(0.0)

        cvec = np.array(cvec)

        return cvec
