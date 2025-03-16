#this is an example how to use this lab helper. Try to understand how it works and adapt the example to your needs

import pandas as pd
from uncertainties import ufloat
from uncertainties.umath import sqrt, tan, sin
from mnk_functions import mnk, mnk_linear
from ufloat_functions import get_values_and_errs_from_ufloat_arr
from tex_functions import make_table_and_print
from math import pi

import numpy as np
import matplotlib.pyplot as plt

from excel_func import get_ufloat_arr_from_excel, print_ufloat

# Загрузка файла Excel
excel_filename = "lab4.4.2.xlsx"
sheet_name = "P1"

gr = get_ufloat_arr_from_excel(excel_filename, sheet_name, "Градусы", "Eps_0") 
min = get_ufloat_arr_from_excel(excel_filename, sheet_name, "Минуты", "Eps_0") 
sec = get_ufloat_arr_from_excel(excel_filename, sheet_name, "Секунды", "eps") 
Lambda = get_ufloat_arr_from_excel(excel_filename, sheet_name, "Длина волны", "Eps_0")[:6] 

print(gr)
print(min)
print(sec)

make_table_and_print(0, len(gr), gr, min, sec)

gr_table = gr[:6]
min_table = min[:6]
sec_table = sec[:6]

gr = gr + min / 60 + sec / 3600
print(gr)

sin_gr = np.array([ufloat(0,0) for _ in range(len(gr))])

for i in range(len(gr)):
    sin_gr[i] = sin(pi * gr[i] / 180)


print(sin_gr)
print(Lambda)


y1 = sin_gr[:6]
x1 = Lambda

print(y1)


angle_coeff_1, free_coeff_1 = mnk(x1, y1)


plot_x1, plot_x1_err = get_values_and_errs_from_ufloat_arr(x1)
plot_y1, plot_y1_err = get_values_and_errs_from_ufloat_arr(y1)

_, ax = plt.subplots()

ax.errorbar(plot_x1, plot_y1, xerr=plot_x1_err, yerr=plot_y1_err, fmt='.', color = 'green')
ax.axline((0, free_coeff_1.n), slope=angle_coeff_1.n, c='green')

ax.grid()

ax.set_xlabel("длина волны (нм)")
ax.set_ylabel("sin(phi)")


#plt.legend()

plt.show()
