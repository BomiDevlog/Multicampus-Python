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