import numpy as np


def get_R_errors(N, t_intervall): return np.sqrt(N) / t_intervall


def sk_to_real_x(x):
    pass


def getTotalErrorsForR(dRu, dR): return np.sqrt(dRu ** 2 + dR ** 2)


def getFinalR(N, Ru_per_second, R_measurement_time):
    R_per_second = N / R_measurement_time
    return R_per_second - Ru_per_second

