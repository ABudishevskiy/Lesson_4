# Дан массив. Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами.
# Функция должна иметь вид: def swap(target_list, item_index1, item_index2).
def swap(t, x1, x2):
    n = t
    k = t[x1]
    n[x1] = t[x2]
    n[x2] = k
    return n
a = [1, 2, 3, 4, 5, 6, 7]
print(swap(a, 1, 3))