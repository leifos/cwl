import numpy as np
import math
import logging

logging.basicConfig(filename='cwl.log',level=logging.DEBUG)


class CWLMetric(object):

    def __init__(self):
        self.expected_utility = 0.0
        self.expected_cost = 0.0
        self.expected_total_utility = 0.0
        self.expected_total_cost = 0.0
        self.expected_items = 0.0
        self.metric_name = "Def"
        self.ranking = None


    def c_vector(self, gains, costs=None):
        # precision for k = len(gains)
        cvec = np.ones(len(gains))
        return cvec

    def l_vector(self, gains, costs=None):
        cvec = self.c_vector(gains, costs)
        logging.debug("{0} {1} {2} {3}".format(self.ranking.topic_id, self.metric_name, "cvec", cvec[0:11]))

        cshift = np.append(np.array([1.0]), cvec[0:-1])
        lvec = np.cumprod(cshift)
        #tmp = np.subtract(np.ones(len(cvec)),cvec)
        lvec = np.multiply(lvec,(np.subtract(np.ones(len(cvec)),cvec)))
        logging.debug("{0} {1} {2} {3}".format(self.ranking.topic_id, self.metric_name, "lvec", lvec[0:11]))
        #print(self.metric_name, "lvec", lvec[0:10])
        return lvec

    def w_vector(self, gains, costs=None):
        cvec = self.c_vector(gains, costs)
        #print(cvec)
        cvec = cvec[0:-1]
        #print("cvec-1", cvec)
        cvec_prod = np.cumprod(cvec)
        #print(cvec_prod)
        cvec_prod = np.pad(cvec_prod,(1,0),'constant',constant_values=(1.0))
        #print(cvec_prod)
        w1 = np.divide(1.0, np.sum(cvec_prod))
        #print(w1)
        #print(cvec_prod[1:len(cvec_prod)])
        w_tail = np.multiply(cvec_prod[1:len(cvec_prod)],w1)
        #print(w_tail)
        wvec = np.append(w1, w_tail)
        logging.debug("{0} {1} {2} {3}".format(self.ranking.topic_id,self.metric_name, "wvec", wvec[0:11]))
        return wvec

    def pad_vector(self, vec1, n, val):
        """
        Pads vector 1 to be the same size as vector 2
        :param vec1:
        :param vec2:
        :return:
        """

        if len(vec1) < n:
            vec1 =  np.pad(vec1,(0,n-len(vec1)), 'constant', constant_values=(val))
        return vec1

    def pad_vector_zeros(self, vec1, n):
        if len(vec1) < n:

            return self.pad_vector(vec1, n, 0.0)

    def pad_vector_ones(self, vec1, n):
        if len(vec1) < n:
            return self.pad_vector(vec1,n, 1.0)


    def measure(self, ranking):

        self.ranking = ranking
        gains = np.array(ranking.gains)
        costs = np.array(ranking.costs)
        gains = self.pad_vector_zeros(gains, 1000)
        costs = self.pad_vector_ones(costs, 1000)

        #create the c / w / l vectors for the gain vector

        wvec = self.w_vector(gains, costs)
        lvec = self.l_vector(gains, costs)

        #gains = self.pad_vector(gains, wvec)
        #costs = self.pad_vector(costs, wvec)
        cum_gains = np.cumsum(gains)
        cum_costs = np.cumsum(costs)
        
        self.expected_utility = np.sum( np.dot(wvec, gains) )
        self.expected_total_utility = np.sum(np.dot(lvec, cum_gains))

        self.expected_cost = np.sum( np.dot(wvec, costs) )
        self.expected_total_cost = np.sum(np.dot(lvec, cum_costs))
        self.expected_items = 1.0 / wvec[0]

        return self.expected_total_utility

    def report(self):
        print("{0} {1} {2:.3f} {3:.3f} {4:.3f} {5:.3f} {6:.3f}".format(self.ranking.topic_id, self.metric_name, self.expected_utility,self.expected_total_utility,self.expected_cost,self.expected_total_cost, self.expected_items))








'''
http://dl.acm.org/citation.cfm?id=2838938
@inproceedings{moffat2015inst,
    title={INST: An Adaptive Metric for Information Retrieval Evaluation},
    author={Moffat, Alistair and Bailey, Peter and Scholer, Falk and Thomas, Paul},
    booktitle={Proceedings of the 20th Australasian Document Computing Symposium (ADCS'15)$\}$},
    year={2015},
    organization={ACM--Association for Computing Machinery$\}$}
'''
