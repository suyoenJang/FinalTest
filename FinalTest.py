#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222063 이름 : 장수연

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution():
    answer = 0
    while True:
        my_string = input("my_string을 입력하세요: ")
        if not(1 <= len(my_string) <= 100):
            print("다시 입력하세요. (1 ≤ my_string 의 길이 ≤ 100)")
            continue
        # my_string의 길이가 1보다 작거나 100보다 크면 False값이 나오므로 continue에의해 input으로 다시 되돌아 간다.
        elif not my_string.islower(): 
            print("다시 입력하세요. (영소문자만 가능합니다.)")
            continue
        #문자열 전체가 모두 소문자가 아니므로 False값이 출력되어 continue에의해 input으로 되돌아 간다.

        target = input("target을 입력하세요: ")
        if not(1 <= len(target) <= 100):
            print("다시 입력하세요. (1 ≤ target 의 길이 ≤ 100)")
            continue
        # target의 길이가 1보다 작거나 100보다 크면 False값이 나오므로 continue에의해 input으로 다시 되돌아 간다.
        elif not target.islower():
            print("다시 입력하세요.(영소문자만 가능합니다.)")
            continue
        #문자열 전체가 모두 소문자가 아니므로 False값이 출력되어 continue에의해 input으로 되돌아 간다.
        if target in my_string:
            return 1
        else:
            return answer
        #my_string 문자열안에 target이 있으면 1을 return하고 없으면 0을 return한다. (맨 위에 asnwer = 0을 입력함.)
print("result : ", solution())
#위의 프로그램을 출력한다.

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):

    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z', '':" "} 
    # 출력시 공백을 넣고 싶어서 마지막에 공백에 관한 모스부호 추가
    
    
    answer = ''
    word = letter.split(' ') #모스를 구별하기 위해 공백을 기준으로 나눈것 
    

    for morse_word in word:
        if morse_word in morse:
            answer += morse[morse_word] 

    return answer
# 공백을 기준으로 나눈 모스부호를 morse의 리스트에 있는 단어들(morse_word)들과 하나씩 대입해보고 'answer += morse[morse_word]'를 통해 맞는 단어를 연결하는 것이다.
while True:
    letter = input("input morse: ")
    if not(1 <= len(letter) <= 1000):
        print("reinput morse: (1 <= 모스부호 길이 <= 1000 )")
        continue
    
    letter = solution(letter) # 입력한 모스부호를 위의 프로그램에 적용한 것을 letter로 정의한다.
    print("모스부호 해독 결과: ", letter) #결과를 print한다.
    
#letter = ".--. .- ... -   .. ...   .--- ..- ... -   .--. .- ... -" / "past is just past"

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    alphabet = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    # 알파벳과 숫자를 연결한다.
    answer = ''
    age =  str(age) #age(숫자)를 문자로 바꿔준다.

    for i in range(len(age)):
        answer += alphabet[age[i]] 
    return answer 
    #문자열 age의 길이만큼 for문을 실행시키며, 입력한 숫자와 맞는 알파벳이 나오면 answer에 return한다.
age = input("age: ") #나이(숫자)를 입력한다.
print(solution(age))
 #프로그램 solution(age)에 입력한 숫자에따른 출력값을 print한다.

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

import math
# 표준 라이브러리 중 math를 써야 하므로 import로 입력한다.
def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1): 
    # r1과 r2가 모두 정수이므로 가장 작은 정수인 1로 하여 1부터 r2>r1이므로 #r2+1까지 for문을 반복한다.
    # i 는 x=i를 의미한다.
    # 1 ~ r2까지 x = i인 직선의 교점을 구하는 것이다.
        if i< r1:
            s = math.ceil(math.sqrt((r1**2 - i**2)))
            #math.sqrt() 함수는 괄호안의 값에 제곱근 씌운값을 출력한다.
            # float형이므로 음수가 들어올 수 없다. 따라서 i가 r1보다 #작으므로 .sqrt를 사용할 수 있다. 
            #math.ceil()은 괄호 안의 값을 반올림한 값으로 출력한다.
            #.ceil로 출력한 값은 정수(int형)이다.
            #따라서 s는 r1보다 큰 정수중에 가장 r1과 가까운 정수를 의미한다.
        else:
            s = 0
            #만약 i >= r1 이라면 r1과 i의 교점이 없어 r2보다 작으면서 #r1보다 큰 정수들중 r1과 가장 가까운 정수를 구할 수 없게 된다. 

        e = math.floor(math.sqrt((r2**2 - i**2)))
        # math.floor()는 괄호 안의 값을 반내림한 값을 출력한다.
        # e는 r2보다 작은 정수 중 가장 큰 정수를 의미한다.
        answer = (answer + e - s + 1) * 4
        # answer값은 교점의 개수를 의미하며 e-s+1는 r2보다 작은 정수들 중 #가장 큰 정수 와 r1보다 큰 정수들 중 가장 작은 정수사이의 개수를 #의미한다. 
        # x, y축을 기준으로 4등분을 하여 구한 값이므로 마지막에 *4를 하여 총 #개수를 구한다.

    return answer
while True:
    a = int(input("r1: "))
    b = int(input("r2: "))
    #input()으로 입력한 값은 문자열 형태인데 solution()은 정수형 값을 입력해야 하므로 a, b값을 정수형으로 바꿔주기 위해 앞에 int()를 입력했다.
    if not(1<= a < b):
        print("다시 입력하세요.(1<=a<b<=1,000,000)")
    elif not(a < b <= 1000000):
        print("다시 입력하세요.(1<=a<b<=1,000,000)")
    else:
        break
    # while문을 이용하여 (1<=r1<r2<=1,000,000)조건을 위반했을때 다시 입력하도록 했다.

result = solution(a, b)
print("result: ", result)
# r1과 r2 값을 입력받아 solution(r1,r2)에 적용하여 print()로 출력한다.
a = int(input("r1: "))
b = int(input("r2: "))
#input()으로 입력한 값은 문자열 형태인데 solution()은 정수형 값을 입력해야 하므로 a, b값을 정수형으로 바꿔주기 위해 앞에 int()를 입력했다.
result = solution(a, b)
print("result: ", result)
# r1과 r2 값을 입력받아 solution(r1,r2)에 적용하여 print()로 출력한다.

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
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