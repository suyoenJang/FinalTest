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