import numpy as np
from measures.cwl_metrics import CWLMetric

'''
Bejewelled Player Model (BPM)

Static 

Gains are assumed to be scaled to be between: 0.0 - 1.0
thus rel_max = 1.0

'''


class BPMCWLMetric(CWLMetric):

    def __init__(self, T=1, K=10):
        super(CWLMetric, self).__init__()
        self.metric_name = "BPM-Static T={0} K={1}".format(T,K)
        self.T = T # E_b the total amount of benefit desired
        self.K = K # E_c the total amount of cost or documents willing to be examined

    def c_vector(self, gains, costs):

        c_gain = np.cumsum(gains)
        c_cost = np.cumsum(costs)
        #print(c_gain[0:11])
        #print(c_cost[0:11])

        # GAIN Constraint
        rr_cvec = np.zeros(len(gains))
        i = 0
        # continue until the gain accumulated exceeds T
        while i < len(gains) and (c_gain[i] < self.T):
            rr_cvec[i] = 1.0
            i = i + 1
        #print(self.T, self.K)
        #print("rrvec", rr_cvec[0:11])
        # COST Constraint
        p_cvec = np.zeros(len(costs))
        i = 0
        # continue until the costs accumulated exceeds K
        while i < len(costs) and (c_cost[i] < self.K):
            p_cvec[i] = 1.0
            i = i + 1

        #print("pvec", p_cvec[0:11])
        # combine the two continuation bectors
        bpm_cvec = np.zeros(len(costs))
        i = 0
        while i < len(costs):
            if (rr_cvec[i] == 1.0) and (p_cvec[i] == 1.0):
                bpm_cvec[i] = 1.0
            i = i + 1
        #print("bpm", bpm_cvec[0:11])
        return bpm_cvec




class BPMDCWLMetric(CWLMetric):

    def __init__(self, T=1, K=10, hb=1.0, hc=1.0, gain_med = 0.5):
        super(CWLMetric, self).__init__()
        self.metric_name = "BPM-Dynamic T={0} K={1}".format(T,K)
        self.T = T # E_b the total amount of benefit desired
        self.K = K # E_c the total amount of cost or documents willing to be examined
        self.hb = hb # the scaling factor to adjust the T constraint by
        self.hc = hc # the scaling factor to adjust the K constraint by
        self.gain_med = gain_med # i.e. rel_med to adjust the T and K by

    def c_vector(self, gains, costs):

        c_gain = np.cumsum(gains)
        c_cost = np.cumsum(costs)
        #print(c_gain[0:11])
        #print(c_cost[0:11])

        # GAIN Constraint
        rr_cvec = np.zeros(len(gains))
        i = 0
        T = self.T
        # continue until the gain accumulated exceeds T
        while i < len(gains) and (c_gain[i] < T):
            rr_cvec[i] = 1.0
            # Now Update T, depending on gain[i]
            T = T + self.hb * (gains[i] - self.gain_med )

            i = i + 1
        #print(self.T, self.K)
        #print("rrvec", rr_cvec[0:11])
        # COST Constraint
        p_cvec = np.zeros(len(costs))
        i = 0
        K = self.K
        # continue until the costs accumulated exceeds K
        while i < len(costs) and (c_cost[i] < K):
            p_cvec[i] = 1.0
            # Now Update K, depending on gain[i]
            T = T + self.hc * ( gains[i] - self.gain_med)

            i = i + 1

        #print("pvec", p_cvec[0:11])
        # combine the two continuation bectors
        bpm_cvec = np.zeros(len(costs))
        i = 0
        while i < len(costs):
            if (rr_cvec[i] == 1.0) and (p_cvec[i] == 1.0):
                bpm_cvec[i] = 1.0
            i = i + 1
        #print("bpm", bpm_cvec[0:11])
        return bpm_cvec
