
def selection_sort(unsorted_list):
    indexing_length = range(0, len(unsorted_list)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_value]:
                min_value = j

            if min_value != i:
                unsorted_list[min_value], unsorted_list[i] = unsorted_list[i], unsorted_list[min_value]

    return unsorted_list


list_example = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 8, 7, 5, 4, 2, 1]

print(selection_sort(list_example))
