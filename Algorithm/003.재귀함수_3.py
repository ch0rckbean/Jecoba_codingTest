# 문제 접근 방법
# 1. 반복문의 경우: Bottom-up (작은 문제에서 출발)
# 2. 재귀의 경우: Top-down (큰 문제에서 출발)
# 재귀의 경ㅇ 꼭 종료 조건 있어야

# 반복문
x = 0
for i in range(11):
    x += 1
print(x)

# 재귀함수


def f(n):
    if n <= 1:
        return 1
    else:
        return n + f(n-1)


print(f(10))

while True:
    if input('##') == 'exit':
        break
    if input('##') == 'hi':
        print('hello world')
    else:
        continue


def console():
    if input('##') == 'exit':
        return None
    console()


console()

# 2진수 구하기 - 반복문
t = int((input('2진수로 바꿀 숫자를 입력하세요: ')))
result = ''
while True:
    if t % 2 == 0:
        result += '0'
    else:
        result += '1'
    t = t//2
    if t == 1:
        result += str(t)
        print(result[::-1])
        break


def 이진수구하기(입력값):
    if 입력값 < 2:
        return str(입력값)
    else:
        return str(이진수구하기(입력값//2))+str(입력값 % 2)


이진수구하기(11)

# 문자열 뒤집기


def 문자열뒤집기(문자열):
    if 문자열 == '':
        return None
    else:
        문자열뒤집기(문자열[1:])
        print(문자열[0])


print(문자열뒤집기('보석바는요구르트맛'))

result2 = ''
for i in '메로나마싯다':
    result2 = i+result2
print(result2)

# 각 자릿수의 합
x = 0
for i in '9985':
    x += int(i)
    print(x)


def sum(s):
    if s=='':
        return 0
    else:
        return int(s[0]) + int(sum(s[1:]))

sum('1234')
