# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,ㄴ
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    numbers = list(map(str,numbers)) #리스트의 숫자를 문자열로 바꿔준다.
    numbers.sort(key = lambda x : x*3, reverse = True)
    #'key = lambda x : x*3'는 리스트의 각 숫자를 세번 반복하여 문자열들을 비교하고 numbers.sort( , reverse = True)으로 리스트를 큰 순서대로 정렬한다.
    #예로들어서 '23'과 '2'을 비교한다고 가정하면, '23'과 '2'을 세번 반복하면 '232323'과 '222'이 되는데 첫자리끼리 비교하면 '2'로 같기때문에 다음 두번째 자리끼리 비교한다. 두번째 자리는 각각 '3'과 '2'이므로 23이 2보다 큰수로 인식되어 리스트에서는 ['23','2']가 된다.
    answer = ''.join(numbers)
    # 정렬된 문자열을 이어붙여 하나의 문자로 만든다.
    return str(int(answer))
    #문자를 정수로 바꾼후 다시 문자열로 만들어 앞에 붙는 '0'을 제거한다.
numbers = [*map(int,input().split())]
#input(),split()은 입력한 것을 공백을 기준으로 구분해서 리스트로 바꿔준다.
#map함수를 통해 각 원소를 정수로 바꾼다.
number = solution(numbers)
print(number)