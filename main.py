# def count_positives_sum_negatives(arr):
#     if arr == [] or arr is None:
#         return []
#     count_positives = 0
#     sum_negatives = 0
#     for num in arr:
#         if num > 0:
#             count_positives += 1
#         elif num < 0:
#             sum_negatives += num
#     return [count_positives, sum_negatives]
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, -11, -12, -13, -14, -15]))

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = sum(1 for i in arr if i > 0)
    neg = sum(i for i in arr if i < 0)
    return [pos, neg]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

