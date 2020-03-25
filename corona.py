import numpy as np
from scipy import interpolate

x = np.arange(0,24)
x_last = x[:-1]
y = np.array([
    1, 1, 1, 1, 7, 11, 14,
    17, 20, 28, 34, 45, 59, 63,
    93, 114, 147, 199, 253, 306, 367,
    438, 495, 658
])
f = interpolate.interp1d(x, y, fill_value='extrapolate')

y_diff = y[1:] - y[:-1]
f_diff = interpolate.interp1d(x[:-1], y_diff, fill_value='extrapolate')

if __name__ == '__main__':
    # print(y_diff)
    f_23 = interpolate.interp1d(x[:-1], y[:-1], fill_value='extrapolate')
    # print(f_23(24))

    f_23_diff = interpolate.interp1d(x_last[:-1], y_diff[:-1], fill_value='extrapolate')

    # print(f_23_diff(23))
    # print("f_diff: " , f_diff(24))