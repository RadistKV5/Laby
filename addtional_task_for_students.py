# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    item = item
    list_ = l
    count = 0
    for i in range(len(list_)):
        if list_[i] == item:
            count += 1
    return count
