from uncertainties import ufloat
from uncertainties.umath import sqrt, sin, log, tan
import numpy as np
import matplotlib.pyplot as plt



def get_values_and_errs_from_ufloat_arr(arr_ufloat):
    arr_values = [arr_ufloat[i].n for i in range(len(arr_ufloat))]
    arr_errs = [arr_ufloat[i].s for i in range(len(arr_ufloat))]

    return arr_values, arr_errs

def create_ufloat_arr(arr_values, arr_err):
    if (len(arr_err) != len(arr_values)):
        print("len is not equal")
        return np.zeros(len(arr_values))
    
    arr_ufloat = np.array([ufloat(0, 0) for _ in range(len(arr_values))])
    
    for i in range(len(arr_err)):
        arr_ufloat[i] = ufloat(arr_values[i], arr_err[i])

    return arr_ufloat

def print_ufloat(arr_ufloat, n_round = 10):
    print("значения")
    for i in range(len(arr_ufloat)):
        print(round(arr_ufloat[i].n, n_round))
    print("погрешности")
    for i in range(len(arr_ufloat)):
        print(round(arr_ufloat[i].s, n_round))


def do_unary_operation(arr_ufloat, unary_operation_name):
    
    res = np.array([ufloat(0, 0) for _ in range (len(arr_ufloat))])
    
    for i in range(len(arr_ufloat)):
        print(arr_ufloat[i])
        exec(f"res[{i}] = ({unary_operation_name}(arr_ufloat[{i}]))")

    return res
