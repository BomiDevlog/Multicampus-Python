#키워드 인자 (keyword argument) 이름을 함께 명시하여 값 전달.
# 이름이 지정되어 있기때문에 순서 상관없음.
# 단점: 타이핑 양이 늘어남
# 장점: 순서상관없음.어떤 매개변수를 넘겨주는지 정확하게 알수있음.
# 예. print(1,2, end=' '). 이때 end=' '가 키워드 인자.
# 특히 딥러닝에서 함수인자가 많아져서 키워드 인자 방식을 많이 사용한다.

#<-> 위치 기반 positional argument : 순서대로 매핑
# 장점: 간결함(타이핑 양이 적음)
# 단점: 가독성이 떨어짐 (이 값이 뭐지? 순서가 어땠더라? 다시 함수를 찾아보아야함)

# 두 가지 방법을 혼용해서 사용 가능 
# 단, 위치 기반 인자를 먼저 나열하고, 뒤에 키워드 인자를 나열.

def func(shape, width=1, height=1, radius=1):
    # shape 디폴트값이 주어지지 않음 -> 필수 인자
    # width, height, radius는 값이 주어짐 -> 옵션
    if shape == 0 :     # shape값이 0이면 사각형 면적을 반환
        return width * height
    if shape == 1 : #shape값이 1이면 원의 면적을 반환
        return 3.14 * radius ** 2

print("rect area =", func(0, width=10, height=2))
print("circle area=", func(1,radius=5))

print(func(0, height=3))

# 키워드 인자의 특징 : 디폴트값이 있는 경우 중간에 있는 인수 생략 가능


# 자바는 웹 서버 
# c++는 장치제어
# 파이썬은 인공지능, 데이터분석