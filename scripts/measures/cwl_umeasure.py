import numpy as np
import math
from measures.cwl_metrics import CWLMetric
import logging

'''
U-Measure
#TODO(leifos) add reference to Zhou and Sakai (2013)



'''

class UMeasureCWLMetric(CWLMetric):
    def __init__(self, L=1000):
        super(CWLMetric, self).__init__()
        self.metric_name = "U L@{0} ".format(L)
        self.L = L

    def c_vector(self, gains, costs):

        wvec = self.w_vector(gains, costs)

        cvec = []
        for i in range(0,len(wvec)-1):
            if(wvec[i]>0.0):
                cvec.append( wvec[i+1]/ wvec[i])
            else:
                cvec.append(0.0)

        cvec.append(0.0)
        cvec = np.array(cvec)
        return cvec


    def w_vector(self, gains, costs):
        """

        :param gains:
        :param costs:
        :return:
        """
        wvec = []
        # to get the positions, cumulative sum the costs..
        # costs are assumed to length of each document
        ccosts = np.cumsum(costs)
        start = 0
        norm = 0.0
        for i in range(0,len(ccosts)-1):
            weight_i = self.pos_decay(start)
            start = ccosts[i]
            wvec.append(weight_i)
            norm = norm + weight_i
        wvec.append( 0.0 )

        # now normalize the wvec to sum to one.
        wvec = np.divide(np.array(wvec), norm)
        print(wvec[-20:-10])
        logging.debug("{0} {1} {2} {3}".format(self.ranking.topic_id,self.metric_name, "wvec", wvec[0:10]))
        return wvec


    def pos_decay(self, pos):
        return max(0.0, (1.0 - (pos / self.L)))
