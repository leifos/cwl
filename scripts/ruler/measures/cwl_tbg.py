import numpy as np
import math
from ruler.measures.cwl_metrics import CWLMetric


'''
Time Biased Gain
#TODO(leifos) add reference to Smucker & Clarke

H is the halflife which stipulates how quickly the gain decays over time

@inproceedings{Smucker:2012:TCE:2348283.2348300,
 author = {Smucker, Mark D. and Clarke, Charles L.A.},
 title = {Time-based Calibration of Effectiveness Measures},
 booktitle = {Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval},
 series = {SIGIR '12},
 year = {2012},
 location = {Portland, Oregon, USA},
 pages = {95--104},
 numpages = {10},
 url = {http://doi.acm.org/10.1145/2348283.2348300},
} 


'''

class TBGCWLMetric(CWLMetric):
    def __init__(self, halflife=224):
        super(CWLMetric, self).__init__()
        self.metric_name = "TBG-H@{0} ".format(halflife)
        self.h = halflife
        self.bibtex = """
        @inproceedings{Smucker:2012:TCE:2348283.2348300,
        author = {Smucker, Mark D. and Clarke, Charles L.A.},
        title = {Time-based Calibration of Effectiveness Measures},
        booktitle = {Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval},
        series = {SIGIR '12},
        year = {2012},
        location = {Portland, Oregon, USA},
        pages = {95--104},
        numpages = {10},
        url = {http://doi.acm.org/10.1145/2348283.2348300},
        } 
        """

    def name(self):
        return "TBG-H@{0} ".format(self.h)

    def c_vector(self, ranking):

        wvec = self.w_vector(ranking)

        cvec = []
        for i in range(0,len(wvec)-1):
            if(wvec[i]>0.0):
                cvec.append( wvec[i+1]/ wvec[i])
            else:
                cvec.append(0.0)

        cvec.append(0.0)
        cvec = np.array(cvec)

        return cvec


    def w_vector(self, ranking):

        wvec = []
        ccosts = np.cumsum(ranking.costs)
        start = 0.0

        norm = self.integral_decay(0.0)
        wvec.append(norm)

        for i in range(0,len(ccosts)-1):
            weight_i = self.integral_decay(ccosts[i])
            norm = norm + weight_i
            wvec.append(weight_i)

        wvec = np.divide(np.array(wvec), norm)
        return wvec

    def integral_decay(self, x):
        h = self.h
        return (h * (2.0 ** (-x/h)) )/ math.log(2.0, math.e)
