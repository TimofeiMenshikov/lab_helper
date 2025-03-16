import pandas as pd
import numpy as np
from uncertainties import ufloat

from ufloat_functions import create_ufloat_arr


def get_ufloat_arr_from_excel(excel_filename, sheet_name, value_name, err_name):
    
    df = pd.read_excel(excel_filename, sheet_name = sheet_name)
    
    values = df[value_name]
    errs = df[err_name]

    return create_ufloat_arr(values, errs)


