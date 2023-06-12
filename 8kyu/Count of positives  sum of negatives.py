def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    positive_list = []
    negative_list = []
    final_list = []
    for n in arr:
        if n > 0:
            positive_list.append(n)
        elif n < 0:
            negative_list.append(n)
    final_list.append(len(positive_list))
    final_list.append(sum(negative_list))
    return final_list
