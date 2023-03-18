import numpy as np


def get_R_errors(N, t_intervall): return np.sqrt(N) / t_intervall


def sk_to_real_x(x):
    pass


def getTotalErrorsForR(dRu, dR): return np.sqrt(dRu ** 2 + dR ** 2)


def getFinalR(N, Ru_per_second, R_measurement_time):
    R_per_second = N / R_measurement_time
    return R_per_second - Ru_per_second


def model(x, a): return a / ((x + 0) ** 2)


def calculateChiSquare(x_array, y_array, parameter_range, y_err):
    chi_squareList = []
    for parameter in parameter_range:
        nominator = (y_array - model(x_array, parameter)) ** 2
        variance = y_err ** 2
        chi_square = sum(nominator / variance)
        chi_squareList.append(chi_square)

    chi_min = min(chi_squareList)
    myIndex = chi_squareList.index(chi_min)
    a = parameter_range[myIndex]

    plusCounter = 0
    minusCounter = 0

    while chi_squareList[myIndex + plusCounter] - chi_squareList[myIndex] < 1:
        plusCounter += 1

    while chi_squareList[myIndex + minusCounter] - chi_squareList[myIndex] < 1:
        minusCounter -= 1

    plusDeltaA = parameter_range[myIndex + plusCounter]
    minusDeltaA = parameter_range[myIndex + minusCounter]
    print('Delta_+ of a is at the position:', plusDeltaA, 'with a value of:', plusDeltaA - a)
    print('Delta_- of a is at the position:', minusDeltaA, 'with a value of:', a - minusDeltaA)
    print('a is:', a)

    return a, chi_min, plusDeltaA, minusDeltaA, chi_squareList


