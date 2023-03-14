## 함수 선언부
def add_func(n1, n2) :
    retValue = n1 + n2
    return retValue

def sub_func(n1, n2) :
    retValue = n1 - n2
    return retValue

def gop_func(n1, n2) :
    retValue = n1 * n2
    return retValue

def na_func(n1, n2) :
    retValue = n1 /n2
    return retValue

## 전역 변수부
num1, num2, result = 100, 200, 0


## 메인 코드부
#더하기 기능
result = add_func(num1, num2)
print(num1, '+' , num2 , '=' , result)

result = sub_func(num1, num2)
print(num1, '-' , num2 , '=' , result)

result = gop_func(num1, num2)
print(num1, '*' , num2 , '=' , result)

result = na_func(num1, num2)
print(num1, '/' , num2 , '=' , result)
