import random as rd
from statistics import median

def quick_sort(ls):
    if len(ls) < 2:
        return ls
    else:
        pivot = ls[0]
    
        less_ls = [i for i in ls[1:] if i <= pivot]
        great_ls = [i for i in ls[1:] if i > pivot]

        return quick_sort(less_ls) + [pivot] + quick_sort(great_ls)

ls_len, ls_range= input('リストの長さと範囲を入力してください').split()

ls = [rd.randint(0, int(ls_range)) for i in range(int(ls_len))]

print(ls)
print()
print(quick_sort(ls))