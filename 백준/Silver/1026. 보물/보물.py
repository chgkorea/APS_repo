from collections import deque

def make_alt_arr1():
    answer = [0] * n

    for action_time in range(n):
        current_ele = min(arr1)
        target_idx = arr2.index(max(arr2))
        answer[target_idx] = current_ele
        arr1.remove(current_ele)
        arr2[target_idx] = -1

    return answer


n = int(input())

arr1 = deque(map(int, input().split()))
arr2 = list(map(int, input().split()))
copied = arr2[:]

# print(arr1)
# print(arr2)

arr3 = make_alt_arr1()

result = 0
for i in range(n):
    result += copied[i]*arr3[i]

print(result)