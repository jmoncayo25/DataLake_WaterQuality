def remove_ith_symbol(df_obj_ith, i):
    if i == 0:
        return df_obj_ith[1:]
    return df_obj_ith[0] + remove_ith_symbol(df_obj_ith[1:], i - 1)
