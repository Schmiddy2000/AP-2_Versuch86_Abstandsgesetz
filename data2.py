import matplotlib.pyplot as plt
import numpy as np

import functions as f

measurement_time2 = 60
Ru_per_sec = 0.9979798
Ru_error = 0.02245062

Ru_error_60 = Ru_error * 60

sk_x2 = np.array([3.4, 3.9, 4.4, 4.9, 5.4, 5.9, 6.4, 7.4, 8.4, 9.4, 11.4, 13.4, 15.4, 18.4, 21.4, 24.4, 29.4, 39.4,
                  54.4])

N_array2 = np.array([55.2, 46.87, 41.61, 37.59, 34.66, 31.56, 28.37, 22.36, 17.88, 14.58, 9.978, 7.391, 5.427,
                     3.805, 2.702, 1.994, 1.386, 0.707, 0.318]) * 1e3
N_error2_first = np.zeros(10) + 10
N_error2_second = np.zeros(len(N_array2) - 10)
N_error2 = np.concatenate((N_error2_first, N_error2_second))

R_errors2 = f.get_R_errors(N_array2 + N_error2, 60)

finalR2 = f.getFinalR(N_array2, Ru_per_sec, 60)
finalErrorR2 = f.getTotalErrorsForR(Ru_error_60, R_errors2)

print(finalErrorR2 - Ru_error)


def makePlotTwo(plot_loglog):
    plt.figure(figsize=(12, 5))
    plt.title('Auftragung von $R$ gegen $x$ mit linearen Achsen (Beta)')
    plt.xlabel('Distanz von Probe zu Zähler in [cm]')
    plt.ylabel('Zählrate R in [s${-1}$]')

    plt.scatter(sk_x2, finalR2, marker='x')
    plt.errorbar(sk_x2, finalR2, yerr=finalErrorR2, fmt='none', ecolor='black', capsize=5, capthick=0.8)
    if plot_loglog:
        plt.loglog()
