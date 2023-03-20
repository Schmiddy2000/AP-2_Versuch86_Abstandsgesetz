import matplotlib.pyplot as plt
import numpy as np

import functions as f

# Data:

measurementTime = 180
Ru_array = np.array([182, 175, 196, 168, 173, 170, 912])
total_Ru_counts = sum(Ru_array)
print(total_Ru_counts)
total_Ru_Time = 11 * measurementTime

Ru_per_sec = total_Ru_counts / total_Ru_Time

Ru_error = np.sqrt(total_Ru_counts) / total_Ru_Time

Ru_error_60 = np.sqrt(Ru_per_sec * 60) / 60

print('Ru_Counts per second:', round(Ru_per_sec, 8), '+-', round(Ru_error, 8))
print('Ru_60 =', Ru_per_sec * 60, '+-', Ru_error_60)

sk_x = np.array([3.2, 3.5, 3.7, 4, 4.2, 4.7, 5.2, 5.7, 6.2, 7.2, 8.2, 9.2, 11.2, 13.2, 15.2, 18.2, 21.2, 24.2])

distance = sk_x - 0.5   # + 1.5 - 2

N_array = np.array([1883, 1690, 1517, 1326, 1210, 973, 824, 711, 608, 485, 387, 271, 233, 167, 154, 113, 106, 70])

R_errors = f.get_R_errors(N_array, 60)

finalR = f.getFinalR(N_array, Ru_per_sec, 60)
finalErrorR = f.getTotalErrorsForR(Ru_error_60, R_errors)

param_range = np.linspace(200, 600, 1000)
x_lin = np.linspace(2, 30, 1000)
popt, chi_min, plusDeltaA, minusDeltaA, chi_squareList = f.calculateChiSquare(distance, finalR, param_range,
                                                                              finalErrorR)

print(chi_min)

upperBestFit = f.model(x_lin, popt + 2.802802802802802)
lowerBestFit = f.model(x_lin, popt - 2.802802802802802)


# Plotting:

def makePlotWithChiSquare(plot_loglog, plot_chi_square):
    plt.figure(figsize=(14, 5))

    if plot_chi_square:
        plt.subplot(1, 2, 1)
        plt.title(r'Veranschaulichung $\chi^2$-Minimierung')
        plt.ylabel(r'$\chi^2$')
        plt.xlabel('Zu optimierendes Parameter p')
        plt.plot(param_range, chi_squareList, label=r'$\chi^2$')
        plt.grid()
        plt.legend()
        # plt.ylim(None, 110)

        plt.subplot(1, 2, 2)

    plt.title('Zählrate Cs-137 in Abhängigkeit vom Abstand')
    plt.ylabel('Zählrate $R$ in [s$^{-1}$]')
    plt.xlabel('Abstand in [cm]')
    plt.scatter(distance, finalR, marker='x', c='magenta', label='Messwerte')
    plt.errorbar(distance, finalR, yerr=finalErrorR, fmt='none', ecolor='black', capsize=5, capthick=0.8, elinewidth=1,
                 label='Fehler')
    plt.plot(x_lin, f.model(x_lin, popt), ls='--', c='black', lw=0.8,
             label='Best Fit der Form \n' + r'$y=\frac{p}{x^2}$')
    plt.fill_between(x_lin, upperBestFit, lowerBestFit, where=lowerBestFit > upperBestFit,
                     interpolate=True, color=myColor, alpha=alpha, label=myLabel)
    plt.fill_between(x_lin, upperBestFit, lowerBestFit, where=upperBestFit >= lowerBestFit,
                     interpolate=True, color=myColor, alpha=alpha)
    plt.legend()
    plt.grid()
    # plt.xlim()
    if plot_loglog:
        plt.loglog()
    plt.ylim(-3, 34)
    plt.xlim(None, 27.5)
    plt.subplots_adjust(left=0.085, bottom=0.1, right=0.95, top=0.88)

    return None


# makePlotWithChiSquare(True, True)
# plt.savefig('Cs-137_Linear_with_Chi_square_no_adjust_radiation_source.png', dpi=300)


def makeBasicPlotOne(plot_loglog):
    plt.figure(figsize=(12, 5))
    plt.title('Auftragung von $R$ gegen $x$ mit logarithmischen Achsen (Cs-137)')
    plt.xlabel('Distanz von Probe zu Zähler in [cm]')
    plt.ylabel('Zählrate R in [s${-1}$]')

    plt.scatter(distance, finalR, marker='x', label='Messdaten')
    plt.errorbar(distance, finalR, yerr=finalErrorR, fmt='none', ecolor='black', capsize=5, capthick=0.8)
    plt.plot(x_lin, f.model(x_lin, popt), ls='--', c='black', lw=0.8,
             label='Best Fit der Form \n' + r'$y=\frac{p}{x^2}$')
    if plot_loglog:
        plt.loglog()

    plt.fill_between(x_lin, upperBestFit, lowerBestFit, where=lowerBestFit > upperBestFit,
                     interpolate=True, color='pink', alpha=0.5, label='Konfidenzband')
    plt.fill_between(x_lin, upperBestFit, lowerBestFit, where=upperBestFit >= lowerBestFit,
                     interpolate=True, color='pink', alpha=0.5)

    plt.xlim(2.35, 27.5)
    plt.ylim(None, 45)
    plt.subplots_adjust(left=0.085, bottom=0.1, right=0.95, top=0.88)
    plt.legend()

    return None


makeBasicPlotOne(True)
plt.savefig('Cs-137_logarithmic_no_adjust_radiation_source.png', dpi=300)
plt.show()

