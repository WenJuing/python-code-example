import numpy as np


def fill_nan(t1):
    '''消除数组中的nan，并用该列均值代替'''
    for i in range(t1.shape[1]):  # 遍历列
        col = t1[:, i]  # 获取列
        nan_num = np.count_nonzero(col != col)  # 获取该列nan个数
        if nan_num != 0:
            no_nan_col = col[col == col]  # 获取排除nan后的列
            col[col != col] = np.mean(no_nan_col)
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape(3, 4).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_nan(t1)
    print(t1)
