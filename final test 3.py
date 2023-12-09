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
    

