#задача из списка величин (значение, погрешность) получить тело таблицы в формате LaTex

from uncertainties import ufloat
from uncertainties.umath import sqrt
import numpy as np
import matplotlib.pyplot as plt

import io


def ufloat_to_tex(*args, **kwargs):

    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return "$" + ((" \\pm ".join(contents.split("+/-")))[:-1]) + "$"


def make_table_and_print(n_round, arr_len, *arrs):
    
    for i in range(arr_len):
        for j in range(len(arrs)):
            if (j != len(arrs) - 1):
                
                if (arrs[j][i].s == 0):
                    print("$", arrs[j][i].n, "$", end = ' & ')
                else:
                    print(ufloat_to_tex(arrs[j][i]), end = ' & ')

            else:

                if (arrs[j][i].s == 0):
                    print("$", arrs[j][i].n, "$", end = '  \\\\ \\hline\n')
                else:
                    print(ufloat_to_tex(arrs[j][i]), end = '  \\\\ \\hline\n')