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