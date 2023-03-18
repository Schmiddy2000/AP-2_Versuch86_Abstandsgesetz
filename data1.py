import matplotlib.pyplot as plt
import numpy as np

import functions as f

# Data:

measurementTime = 180
Ru_array = np.array([182, 175, 196, 168, 173, 170, 912])
total_Ru_counts = sum(Ru_array)
total_Ru_Time = 11 * measurementTime

Ru_per_sec = total_Ru_counts / total_Ru_Time

Ru_error = np.sqrt(total_Ru_counts) / total_Ru_Time

Ru_error_60 = np.sqrt(Ru_per_sec * 60) / 60

print('Ru_Counts per second:', round(Ru_per_sec, 8), '+-', round(Ru_error, 8))
print('Ru_60 =', Ru_per_sec * 60, '+-', Ru_error_60)


sk_x = np.array([3.2, 3.5, 3.7, 4, 4.2, 4.7, 5.2, 5.7, 6.2, 7.2, 8.2, 9.2, 11.2, 13.2, 15.2, 18.2, 21.2, 24.2])

N_array = np.array([1883, 1690, 1517, 1326, 1210, 973, 824, 711, 608, 485, 387, 271, 233, 167, 154, 113, 106, 70])

R_errors = f.get_R_errors(N_array, 60)


finalR = f.getFinalR(N_array, Ru_per_sec, 60)
finalErrorR = f.getTotalErrorsForR(Ru_error_60, R_errors)


# Plotting:

def makePlotOne(plot_loglog):
    plt.figure(figsize=(12, 5))
    plt.title('Auftragung von $R$ gegen $x$ mit linearen Achsen (Cs-137)')
    plt.xlabel('Distanz von Probe zu Zähler in [cm]')
    plt.ylabel('Zählrate R in [s${-1}$]')

    plt.scatter(sk_x, finalR, marker='x')
    plt.errorbar(sk_x, finalR, yerr=finalErrorR, fmt='none', ecolor='black', capsize=5, capthick=0.8)
    if plot_loglog:
        plt.loglog()

    return None
