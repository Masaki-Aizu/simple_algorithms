import random as rd

def select_small(ls):
    smallest = ls[0]
    smallest_index = 0

    for i in range(1, len(ls)):
        if smallest > ls[i]:
            smallest = ls[i]
            smallest_index = i
    
    return smallest_index

def selection_sort(ls):
     small_ls = []
     for i in range(len(ls)):
         small_ls.append(ls.pop(select_small(ls)))

     return small_ls

ls_range = input('生成するリストの長さを入力してください:')

ls = [rd.randint(0, 100) for i in range(int(ls_range))]

print(ls)
print()
print(selection_sort(ls))