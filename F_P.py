from Ztego import funk
import pandas as pd
table = pd.read_csv('D:\\pythonProject\\train.csv')

def dopasowywanie_string(table, column):
    for x in table[column]: ###fUNKCJA SKRACAJĄCA Długość imion!!!
        cond = table[column] == x
        if(len(x) > 20):
            spl = x.split()
            new_name = spl[1] + spl[2]
            table.loc[cond,column] = new_name
    return table[column]

def usuwanie_zbed_wie(table, column):
    num_row = 0
    for x in table[column]:
        num_row = num_row + 1
        if x == '[DATA]':
            break
    table = table.loc[num_row:]
    return table

def hex_to_bin(table, column):
    start_table = []
    for x in table[column]:
        my_hexdata = x

        scale = 16  ## equals to hexadecimal

        num_of_bits = 8

        bin_num = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        start_table.append(bin_num)
    start_table = pd.DataFrame({'data': start_table})
    return start_table

        # return ...







