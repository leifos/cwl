import numpy as np
import math
from measures.cwl_metrics import CWLMetric
import logging

'''
Time Biased Gain
#TODO(leifos) add reference to Smucker & Clarke

'''

class TBGCWLMetric(CWLMetric):
    def __init__(self, halflife=224):
        super(CWLMetric, self).__init__()
        self.metric_name = "TBG H@{0} ".format(halflife)
        self.h = halflife

    def c_vector(self, gains, costs):

        wvec = self.w_vector(gains, costs)

        cvec = []
        for i in range(0,len(wvec)-1):
            cvec.append( wvec[i+1]/ wvec[i])

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
        ccosts = np.cumsum(costs)
        start = 0
        norm = self.norm_constant()
        for i in range(0,len(ccosts)-1):
            weight_i = self.area_under_decay(start, ccosts[i])/norm
            start = ccosts[i]
            wvec.append(weight_i)
        wvec.append( 0.0 )

        logging.debug("{0} {1} {2} {3}".format(self.ranking.topic_id,self.metric_name, "wvec", wvec[0:10]))
        return np.array(wvec)


    def integral_decay(self, x):
        h = self.h
        return (h * (2.0 ** (-x/h)) )/ math.log(2.0, math.e)

    def area_under_decay(self, x1, x2):
        return self.integral_decay(x1)-self.integral_decay(x2)


    def norm_constant(self):
        return self.integral_decay(0)
