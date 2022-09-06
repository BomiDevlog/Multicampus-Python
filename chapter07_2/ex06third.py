# 써드 파티 모듈
# C:\ProgramData\Anaconda3\Lib\site-packages
# numpy 데이터분석 c++
# pandas 엑셀 데이터 분석
# PIL 파이썬 이미지 라이브러리 - 이미지 파일 핸들링.


from PIL import Image
image = Image.open("/temp/pinksky.jpeg")
image.show()

# ----------- 가상환경

# 자바의 경우
# mqttex MavenProject - jdbc - paho 
# mqttex2 MavenProject - jdbc - paho :  
# 동일한 것이지만 프로젝트마다 묶어주어야함
# 장점 : 라이브러리 버전을 선택해서 다르게 사용할 수 있다. 1.2버전. 1.5버전

# 파이썬의 경우
# 라이브러리를 전역레벨에서 다운받음
# python -전역레벨 PIL 1벌  - ex01.py, ex02.py
# -> 가상 환경 메커니즘으로 해결
# F1 -> interpreter 선택 -> base 선택
# F1이 안된다면 ctrl + shift + p

# Windows Power shell의 약자 PS. cmd 커맨드창. 
# windows는 2가지 종류의 명령창있음.
# 아나콘다는 디폴트가 cmd라서. PS에서는 가상환경 진입이 안 된 상태.

# PS C:\python> conda activate
# PS C:\python> 

# powershell은 휴지통버튼. 
# 다시 실행하면 
# (base) C:\python>conda activate base
# (base) C:\python>
# base 가상환경 진입.


# 런코드 ->가상환경 진입보다 코드실행이 먼저 이루어져서 에러
# 다시한번 런코드 누름 -> 이미지 파일 뜬다

'''
현재 가상환경 확인하기
(base) C:\python>conda env list
# conda environments:
#
base                  *  C:\ProgramData\Anaconda3


(base) C:\python>

가상환경 만들기
(base) C:\python>conda create --name python_study python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 4.14.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\PC\.conda\envs\python_study

  added / updated specs:
    - python=3.9


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2022.07.19 |       haa95532_0         123 KB
    certifi-2022.6.15          |   py39haa95532_0         153 KB
    openssl-1.1.1q             |       h2bbff1b_0         4.8 MB
    pip-22.1.2                 |   py39haa95532_0         2.5 MB
    python-3.9.13              |       h6244533_1        17.1 MB
    setuptools-63.4.1          |   py39haa95532_0         1.0 MB
    sqlite-3.39.2              |       h2bbff1b_0         805 KB
    ------------------------------------------------------------
                                           Total:        26.5 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.07.19-haa95532_0     
  certifi            pkgs/main/win-64::certifi-2022.6.15-py39haa95532_0
  openssl            pkgs/main/win-64::openssl-1.1.1q-h2bbff1b_0
  pip                pkgs/main/win-64::pip-22.1.2-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.13-h6244533_1
  setuptools         pkgs/main/win-64::setuptools-63.4.1-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.39.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2     
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)?
대괄호가 있는 것이 디폴트, yes가 디폴트라서 엔터하면 yes라고 인식



'''

# 가상환경 목록 보기
'''
(base) C:\python>conda env list
# conda environments:
#
base                  *  C:\ProgramData\Anaconda3
python_study             C:\Users\PC\.conda\envs\python_study 
python_study2            C:\Users\PC\.conda\envs\python_study2
python_study3            C:\Users\PC\.conda\envs\python_study3
'''

# conda deactivate 현재 가상환경에서 벗어남. (터미널에서만.)
# conda activate 가상환경이름 (예)conda activate python_study

# 가상환경이기에 PIL없다고 인식.
# pip install 패키지명  => 외부라이브러리 설치
# 모듈명은 PIL인데 패키지명은 pillow이다.
# -> PIL사용가능함
'''
(base) C:\python>pip install PIL
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement PIL (from versions: none)
ERROR: No matching distribution found for PIL

(base) C:\python>pip install pillow
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pillow in c:\programdata\anaconda3\lib\site-packages (9.0.1)
'''
# C:\Users\PC\.conda\envs에서 확인

# 실전프로젝트에서 프로젝트하나당 가상환경하나
# 프로젝트마다 파이썬의 가상환경을 만들어 버전을 관리할 수 있다.

# ---------
# 다음날 다시 여는 법
'''
C:\python>cd chapter07_2

C:\python\chapter07_2>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 9EF2-0B7F

 C:\python\chapter07_2 디렉터리

2022-09-05  오후 04:42    <DIR>          .
2022-09-05  오후 04:42    <DIR>          ..
2022-09-05  오후 03:42               852 ex01util.py
2022-09-05  오후 03:40               708 ex01내가만드는모듈.py
2022-09-05  오후 03:33               170 ex02모듈의사용.py
2022-09-05  오후 04:04               690 ex03sys.py
2022-09-05  오후 04:08               326 ex04random.py
2022-09-05  오후 04:45               493 ex05package.py
2022-09-05  오후 05:50             5,068 ex06써드파티모듈.py
2022-09-05  오후 04:15    <DIR>          mypack
2022-09-05  오후 03:34    <DIR>          __pycache__
               7개 파일               8,307 바이트
               4개 디렉터리  77,225,353,216 바이트 남음

C:\python\chapter07_2>python ex06써드파티모듈.py
  File "C:\python\chapter07_2\ex06써드파티모듈.py", line 113
    '''
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 678-679: truncated \UXXXXXXXX escape

C:\python\chapter07_2>python ex06thirdmodule.py
  File "C:\python\chapter07_2\ex06thirdmodule.py", line 113
    '''
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 678-679: truncated \UXXXXXXXX escape

C:\python\chapter07_2>conda activate base

(base) C:\python\chapter07_2>python ex08.py
python: can't open file 'C:\python\chapter07_2\ex08.py': [Errno 2] No such file or directory

(base) C:\python\chapter07_2>ptyhon ex06thirdmodule.py
'ptyhon'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.

(base) C:\python\chapter07_2>python ex06third.py
  File "C:\python\chapter07_2\ex06third.py", line 113
   
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 678-679: truncated \UXXXXXXXX escape

(base) C:\python\chapter07_2>conda activate python_study

(python_study) C:\python\chapter07_2>conda deactivate

(base) C:\python\chapter07_2>
'''
# 가상환경없었음 -> base -> python study -> base 직전의 가상환경으로 돌아감
# ->base나가서 가상환경ㅇ없는 곳으로 돌아감
# => 가상환경 관리를 stack으로 이루어지고 있다. 

# 디폴트터미널은 커맨드창으로설정. 파워셀에서 안되는 명령어들있어서.

'''
(base) C:\python\chapter07_2>java -v
Unrecognized option: -v
Error: Could not create the Java Virtual Machine.
Error: A fatal exception has occurred. Program will exit.

(base) C:\python\chapter07_2>java --version
openjdk 14 2020-03-17
OpenJDK Runtime Environment (build 14+36-1461)
OpenJDK 64-Bit Server VM (build 14+36-1461, mixed mode, sharing)

(base) C:\python\chapter07_2>--는 옵션의 풀네임 -는 이니셜 하나 명명관례
'''

# 가상환경 만들기
# conda create --name data_science python=3.8
# 목록 확인 conda env list
# 활성화 conda activate data_science    
# 비활성화  conda deactivate

# 가상환경 목록 파일 C:\Users\PC\.conda에 environments.txt

# 가상환경 삭제 conda remove --name python_study3 --all
# all옵션을 안주면 목록에서만 삭제되고 파일은 그대로 남음!
# 현재 사용중인 가상환경은 삭제되지 않고 에러발생! 지금 사용중이니까!

# ---------
# 외부 모듈 관리 pip
# pip는 가상환경 진입해서 사용하는 것

# 활성화 (가상환경 진입)conda activate data_science 
# pip freeze 설치한 패키지 목록 확인 :wincertstore패키지 0.2버전이 있음
# pip install pillow 패키지 설치
# pip freeze 다시 패키지 목록확인
# pip uninstall pillow 설치한 패키지를 삭제
# pip freeze 다시 패키지 목록확인
'''
(base) C:\python\chapter07_2>conda activate data_science

(data_science) C:\python\chapter07_2>pip freeze
certifi @ file:///C:/Windows/TEMP/abs_e9b7158a-aa56-4a5b-87b6-c00d295b01fanefpc8_o/croots/recipe/certifi_1655968940823/work/certifi
wincertstore==0.2

(data_science) C:\python\chapter07_2>pip install pillow
Collecting pillow
  Downloading Pillow-9.2.0-cp38-cp38-win_amd64.whl (3.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 10.5 MB/s eta 0:00:00
Installing collected packages: pillow
Successfully installed pillow-9.2.0

(data_science) C:\python\chapter07_2>pip freeze
certifi @ file:///C:/Windows/TEMP/abs_e9b7158a-aa56-4a5b-87b6-c00d295b01fanefpc8_o/croots/recipe/certifi_1655968940823/work/certifi
Pillow==9.2.0
wincertstore==0.2

(data_science) C:\python\chapter07_2>pip uninstall pillow
Found existing installation: Pillow 9.2.0
Uninstalling Pillow-9.2.0:
  Would remove:
    c:\users\pc\.conda\envs\data_science\lib\site-packages\pil\*
    c:\users\pc\.conda\envs\data_science\lib\site-packages\pillow-9.2.0.dist-info\*        
Proceed (Y/n)? y
  Successfully uninstalled Pillow-9.2.0

(data_science) C:\python\chapter07_2>pip freeze\
ERROR: unknown command "freeze\" - maybe you meant "freeze"

(data_science) C:\python\chapter07_2>pip freeze
certifi @ file:///C:/Windows/TEMP/abs_e9b7158a-aa56-4a5b-87b6-c00d295b01fanefpc8_o/croots/recipe/certifi_1655968940823/work/certifi
wincertstore==0.2

(data_science) C:\python\chapter07_2>cd ..

(data_science) C:\python>cd chapter07_2

(data_science) C:\python\chapter07_2>
'''

# 창을 끄고 다시 실행하면 
# 가상환경진입 전에 실행해서 에러남
# 다시 실행하면 됨

# -------

