import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


x = np.arange(0,30)
x_last = x[:-1]
y = np.array([
    1, 1, 1, 1, 7, 11, 14,
    17, 20, 28, 34, 45, 59, 63,
    93, 114, 147, 199, 253, 306, 367,
    438, 495, 658, 840, 1036, 1264, 1534,
    1836, 2337
])

if __name__ == '__main__':
    f = interpolate.interp1d(x, y, fill_value='extrapolate', kind='quadratic')

    y_diff = y[1:] - y[:-1]
    f_diff = interpolate.interp1d(x[:-1], y_diff, fill_value='extrapolate', kind='quadratic')

    x_gr = np.arange(0, len(x) + 28)
    y_gr = [f(x) for x in x_gr]

    fig = plt.figure()
    plt.plot(x_gr, y_gr)
    plt.show()

    