import re

# 수식을 입력받는다.
# 수식이라고 이해하는 것보다 입력받은 문자열을 정수 리스트로 쪼갠다고 생각하는 것이 간편하다.
text = list(map(int, re.findall('[-+]?\d+', input())))

# 처음으로 음수가 등장하는 index를 저장한다(neg_idx).
# neg_idx 뒤의 모든 정수를 음수로 변환한 후 배열의 정수를 모두 더한 것이 이 문제의 답이다.
for neg_idx in range(len(text)): 
    if text[neg_idx] < 0:
        break

# neg_idx 뒤의 모든 정수를 음수로 변환한 후 합계한다.
result = [x if idx <= neg_idx else -abs(x) for idx, x in enumerate(text)]
print(sum(result))