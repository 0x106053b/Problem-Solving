# point : 삽입 정렬은 데이터가 대부분 정렬되어 있을 때 최적의 시간 복잡도를 가진다.
# 반면, 퀵 정렬은 데이터가 대부분 정렬되어 있을 때 시간 복잡도가 커진다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# (1)
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     print(f"\npivot : {pivot} / left : {left} / right : {right}")
#
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right: # 교차한 경우
#             array[pivot], array[right] = array[right], array[pivot]
#         else: # 교차하지 않은 경우
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
#
# quick_sort(array, 0, len(array)-1)



# -------------------------------------------------------------------------------



# (2)

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))