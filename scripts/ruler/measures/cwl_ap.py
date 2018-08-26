import numpy as np
import math
from ruler.measures.cwl_metrics import CWLMetric


'''
(Graded) Average Precision

#todo(leifos): Add Reference to AP and GAP.

#todo(leifos): Still need to convert Paul's verision of AP from R to Python..


@inproceedings{Robertson:2010:EAP:1835449.1835550,
 author = {Robertson, Stephen E. and Kanoulas, Evangelos and Yilmaz, Emine},
 title = {Extending Average Precision to Graded Relevance Judgments},
 booktitle = {Proceedings of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval},
 series = {SIGIR '10},
 year = {2010},
 location = {Geneva, Switzerland},
 pages = {603--610},
 numpages = {8},
 url = {http://doi.acm.org/10.1145/1835449.1835550}
} 

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
