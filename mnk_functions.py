from uncertainties import ufloat
from uncertainties.umath import sqrt
import numpy as np
import matplotlib.pyplot as plt

import io

# y = angle_coeff * x + free_coeff
def mnk(list_x, list_y):
    '''
    list_x : list[ufloat]
    list_y : list[ufloat]
    Returns (angle_coeff : ufloat, free_coeff : ufloat)
    '''

    n = len(list_x)

    list_xx = [ list_x[i] * list_x[i] for i in range(n) ]
    list_xy = [ list_x[i] * list_y[i] for i in range(n) ]
    list_yy = [ list_y[i] * list_y[i] for i in range(n) ]

    avg_x = np.average(list_x)
    avg_y = np.average(list_y)
    avg_xx = np.average(list_xx)
    avg_xy = np.average(list_xy)
    avg_yy = np.average(list_yy)

    angle_coeff_val = (avg_xy - avg_x*avg_y) / ( avg_xx - avg_x**2 )
    angle_coeff_mnk_err = sqrt( ( (avg_yy - avg_y**2)/(avg_xx - avg_x**2) - angle_coeff_val**2 ) / (n-2) )
    angle_coeff = ufloat(angle_coeff_val.n, sqrt( angle_coeff_val.s**2 + angle_coeff_mnk_err.n**2 ))

    free_coeff_val = avg_y - angle_coeff_val * avg_x
    free_coeff_mnk_err = angle_coeff_mnk_err * sqrt(avg_xx)
    free_coeff = ufloat(free_coeff_val.n, sqrt( free_coeff_val.s**2 + free_coeff_mnk_err.n**2 ))

    return angle_coeff, free_coeff

# y = angle_coeff * x
def mnk_linear(list_x, list_y):
    '''
    list_x : list[ufloat]
    list_y : list[ufloat]
    Returns angle_coeff : ufloat
    '''

    n = len(list_x)

    list_xx = [ list_x[i] * list_x[i] for i in range(n) ]
    list_xy = [ list_x[i] * list_y[i] for i in range(n) ]
    list_yy = [ list_y[i] * list_y[i] for i in range(n) ]

    avg_x = np.average(list_x)
    avg_y = np.average(list_y)
    avg_xx = np.average(list_xx)
    avg_xy = np.average(list_xy)
    avg_yy = np.average(list_yy)

    angle_coeff_val = avg_xy / avg_xx
    angle_coeff_mnk_err = sqrt( ( avg_yy/avg_xx - angle_coeff_val**2 )/(n-1) )
    angle_coeff = ufloat(angle_coeff_val.n, sqrt( angle_coeff_val.s**2 + angle_coeff_mnk_err.n**2 ))

    return angle_coeff

