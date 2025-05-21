# point : 계수 정렬은 데이터의 범위가 큰 경우 메모리 이슈로 사용하는 것이 적절하지 않을 수 있다.
# 반대로, 데이터의 범위가 작되 동일한 데이터가 계속해서 등장하는 경우 (예 : 학생들의 시험 성적) 효과적이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0 for _ in range(max(array)+1)]
for x in array:
    count[x] += 1
for i in range(len(count)):
    for _ in range(count[i]): print(i, end=" ")