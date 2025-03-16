# Lab helper
##### this is project that is maden for helping student with their physics labs

### 0. What is ufloat
##### Ufloat is a class object that represents a pair of floats: **value** and **error**.
##### In this repo **numpy arrays** where elements are objects of **ufloat** class are used so it is very simple to obtain new values with errors
##### For example you have  numpy arrs for Resistance (*R*), Electric current (*I*) to get Voltage (*U*) you should write:
####
```python
U = I * R
```
##### And you will get an **ufloat numpy arr** for Voltage


### 1. Data read
##### There is an example of **excel file** "lab4.4.2.xlsx" to store your experemental results. For further data processing in python write like in **example**:
####
```python
ufloat_value = get_ufloat_arr_from_excel(excel_filename, sheet_name, "value", "error") 
```

##### Remember that for further correct operation it is necessary that all arrays have the **same** length
##### If value don't have any error create a collumn with zeros like in **example**

### 2. Make table
To make the table body in **LaTeX** format use:
```python
make_table_and_print(0, len(ufloat_value_1), ufloat_value_1, ufloat_value_2, ufloat_value_3)
```

numpy arrs *ufloat_value_i* must be the **same size** and **type**: numpy arr of *ufloat values* 
there are any numbers of **numpy arrs**

Example of using this function:

```LaTex
$ 255.0 $ & $ 45.0 $ & $38 \pm 5$  \\ \hline
$ 255.0 $ & $ 10.0 $ & $59 \pm 5$  \\ \hline
$ 252.0 $ & $ 37.0 $ & $7 \pm 5$  \\ \hline
$ 247.0 $ & $ 12.0 $ & $32 \pm 5$  \\ \hline
$ 246.0 $ & $ 41.0 $ & $13 \pm 5$  \\ \hline
$ 239.0 $ & $ 34.0 $ & $51 \pm 5$  \\ \hline
$ 295.0 $ & $ 43.0 $ & $21 \pm 5$  \\ \hline
$ 297.0 $ & $ 43.0 $ & $45 \pm 5$  \\ \hline
$ 299.0 $ & $ 41.0 $ & $41 \pm 5$  \\ \hline
$ 300.0 $ & $ 49.0 $ & $36 \pm 5$  \\ \hline
$ 278.0 $ & $ 38.0 $ & $56 \pm 5$  \\ \hline
```

### 3. Draw graphic

To make the graphic you should divide **values** and **errs** with using function:

```python
values, errs = get_values_and_errs_from_ufloat_arr(ufloat_arr)
```

Then use **matplotlib** like in example to draw the graphic

### 4. Get mnk approximation

##### 2 methods of mnk approximation is supported.
##### If you know that the line must pass through zero you should use `mnk_linear` function to get **angle coefficient**
##### Else you should use `mnk` function to get **angle_coefficient** and **free_coefficient**

### 5. Unary operations

###### In order to calculate new values that require unary operators in their calculations, it is necessary to calculate intermediate quantities with one unary operator as follows:

```python
ufloat_value_sin = do_unary_operation(ufloat_value, "sin")
```

##### Instead of `sin`, you can substitute any unary function over **ufloat** defined in the **uncertainties.umath** library
