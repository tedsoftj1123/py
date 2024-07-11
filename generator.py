# generator는 itterable형식을 반환하는 함수를 의미한다.
# 일반적인 함수는 호출을 하고 함수 실행이 모두 끝난 후 결과값을 반환하였다면,
# generator를 사용하게되면 yeid구분을 만났을 때 함수 제어권을 호출자로 넘기게되고 next()를 통한 함수 호출이 될때 까지 대기상태를 유지한다.
def generator(n):
    for i in range(n):
        yield i


gen = generator(5)
print(gen)  # <generator object generator at 0x1043bf850>
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
print(next(gen))  # 더이상 iteration할 요소가 없으면 StopIteration예외가 발생한다

# 아래와같은 형식으로도 사용가능
gen2 = generator(10)
for i in gen2:
    print(i)

# List Comprehention과 비슷한 genration expression을 통해 generator함수를 만들 수 있음
gen3 = (i for i in range(5))


