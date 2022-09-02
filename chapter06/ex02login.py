# 사전을 언제 써야하는가?
# 

# 회원 DB를 기반으로 로그인 시스템을 프로그래밍한다.
# id/password --> 여러개...
# 리스트 튜플 딕셔너리 중에 무엇을 써야할까?

# 1)리스트로 저장한다면, 이중 리스트가 된다
# [ [id1, pwd1], [id2, pwd2], ... ]
# 2)튜플로 저장한다면
# ( (id1, pwd1), (id2, pwd2), ... )
# -> 리스트, 튜플은 루프를 돌려서 id가 일치하는 지 찾아야함

# 3) 딕셔너리로 저장한다면
# ( id1: pwd1, id2: pwd2, ... )
# ->바로 찾을 수 있음 (loop안해도 바로 찾을 수 있다! 이게 가장 중요한 장점.)
# => 정보를 빨리 찾을 때 딕셔너리가 유용!

users = {       # 회원 DB
    'hong' : '1234',
    'kim' : '2345',
    'lee' : 'abcd',
    'park' : 'ABCD'
}
# value는 어떤 값이든 제한 없음. 값이든, 튜플, 사전이라도 가능함

# 최대 3번 할 수 있도록 설정 -> loop를 만듬. 성공했을 땐 break
for i in range(3):
    id = input('ID 입력 : ')
    user_password = input('Password 입력 : ')

    # password = users [id] 
    #[id] 변수 id가 가지 값을 key로 하라. 즉 users에서 해당 키값(입력한 id)에 대응하는 밸류를 password로 선언.
    # 없는 아이디를 입력한다면 KeyError.
    password = users.get(id) 
    # print(password, user_password) # 확인용

    if not password:
        print('존재하지 않는 아이디 입니다.')
        # 존재하지 않는 아이디를 입력하면 password가 None이다
        # None은 False이다. 이를 이용해 조건문 생성 
    # if users.get(id) == None :
    #     print('존재하지 않는 아이디 입니다.')

    if user_password == password:
        print('로그인 성공')
        break
    else : 
        print('로그인 실패')
    

# 아이디 존재x
# ID 입력 : hello
# Password 입력 : hi
# None hi
# 존재하지 않는 아이디 입니다.
# 로그인 실패

# 아이디 존재, 비밀번호 틀렸을 때
# ID 입력 : hong
# Password 입력 : 123
# 1234 123
# 로그인 실패

# 아이디 o, 비밀번호 o
# ID 입력 : kim
# Password 입력 : 2345
# 2345 2345
# 로그인 성공

