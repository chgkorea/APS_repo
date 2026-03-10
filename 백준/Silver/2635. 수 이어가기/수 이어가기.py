first_number = int(input())

result_length_array = [] # 결과물들을 담을 리스트
for second_candidate in range(first_number+1): # 0부터 n-1 까지 순회
    my_array = []
    my_array.append(first_number) # 수열의 첫 수 
    my_array.append(second_candidate) # 수열의 두번째 수
    n = 0
    flag = True
    while flag is True:
        new_number = my_array[n] - my_array[n + 1]
        if new_number < 0:
            flag = False
        else:
            my_array.append(new_number) # new_number 는 수열에 새로 추가되는 수
            n += 1
    result_length_array.append(len(my_array))

maximum_length_second = result_length_array.index(max(result_length_array))

longest = max(result_length_array) # 가장 길 때의 길이 변수
second_number = maximum_length_second # 가장 길 때의 두번째 수 저장 변수


print(longest) # 첫 정답 출력

result_list = []
flag2 = True # 결과 출력용 플래그
result_list.append(first_number)    
result_list.append(second_number) 
# 수열의 첫 두 수 입력
while flag2 is True:
    third_number = first_number - second_number
    if third_number < 0:
        flag2 = False
        break
    result_list.append(third_number) 
    first_number, second_number = second_number, third_number

for x in result_list:
    print(x, end = ' ')