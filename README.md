# Basic-RPi-2024
부경대학교 2024 IoT 개발자 과정 - 라즈베리파이 학습 리포지토리 (안성주 T)

# day01 
- 라즈베리파이 개념

  ![구조](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/001.png)

  ![핀맵](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/002.png)

- **옴의 법칙** : V = IR 

    ![옴의법칙](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/003.png)

    - 전류(암페어,A) : 전하의 흐름
    - 전압(볼트(V)) :  전기장 안에서 전하가 갖는 전위의 차이
    - 저항 : 전기회로에서 전류가 흐르는 것을 방해하는 정도 
    
- 키르히호프의 법칙
  - 1법칙은 전하량 보존 법칙으로 도선이 갈라지거나 합쳐질 때 전류값이 보존된다
  - 2법칙은 에너지 보존 법칙으로 루프(loop) 회로에서 전지가 만든 전위차는 저항에서 감소한 전위차와 같다는 것

![키르히호프](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/004.png)

- GND(0, 그라운드) 역할 (<-> VCC : 1)
  - 전류를 모이게 한다.
  - 전압의 기준이 되는 역할 (=기준 전압)

- GPIO 설정 함수 (python)
  - GPIO.setmode(GPIO.BOARD) -> wPi
  - GPIO.setmode(GPIO,BCM) -> BCM
  - GPIO.setup(channel, GPIOmode) 
    - channel 핀번호, mode IN/OUT
  - GPIO.cleanup

- GPIO 출력 함수 
  - GPIO.output(channel, state) 
    - channel 핀번호, state HIGH/LOW or 1/0 or TRUE/FALSE

- GPIO 입력 함수
  - GPIO.input(channel)
    - channel : 핀번호, 반환값 H/L or 1/0 or T/F

- 시간지연함수 
  - time.sleep(secs)

- 풀업 저항(PULL UP)과 풀다운 저항(PULL DOWN) 쉽게 이해하기
    - 플로팅 현상 : 스위치가 연결되면 전류가 정상적으로 흐르나, 스위치가 연결되지 않은 상태에서 전류가 흐르는지 흐르지 않는지 알 수 없는 상태가 된 것을 말한다. 

    ![플로팅](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/005.png)

    - 풀업 저항(PULL UP) : 저항을 앞에 붙여줘서 플로팅 현상을 해결하는 방법
        - 풀업 저항에서 스위치가 열린 상태일 때(OFF)
        : 입력 핀으로 전류가 흐르게 되고, 전원 전압과 같은 5v전압이 걸리게 됨 => 입력핀은 HIGH 값이 읽힘 

        ![풀업스위치](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/006.png)

        - 풀업 저항에서 스위치가 닫힌 상태일 때(ON)
        : 모든 전류는 GND쪽으로 흐름. 입력핀에는 0v 전압이 걸리게 된다. 

        ![풀업스위치](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/006-2.png)

        ![정리](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/007.png)

    - 풀다운 저항(PULL DOWN) : 풀업 저항과는 반대로 밑에다가 저항을 연결하는 방식 
        - 풀다운 저항에서 스위치가 열린 상태일 때(OFF)
        : 스위치가 열린 상태에서는 어디에도 전류가 흐르지 않고 입력핀에는 0v 전압이 걸리게 됨 

        ![풀다운스위치](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/008.png)

        - 풀다운 저항에서 스위치가 닫힌 상태일 때(ON)
        : 밑의 저항으로 인해 전류는 모두 입력핀 쪽으로 흐르고, 입력핀에는 전원 전압과 같은 5v가 걸리게 됨

        ![풀다운스위치](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/009.png)

        ![총정리](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/010.png)

- 인터럽트(interrupt)
    - 우선순위

- 부저 실습
    - 음계, 주파수

    ![부저](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/001.jpg)

# day02 
- 적외선 센서 연결 
  - 앞에 인지 되면 출력 

- 가상환경 만들기 
  - python -m venv 가상환경이름
  - source ./env/bin/activate
  - 그러면 기존 pi@raspi:~/Documents/GitHub/Basic-RasPi-2024/day02 $ 
  가상환경은 (env) pi@raspi:~/Documents/GitHub/Basic-RasPi-2024/day02 $ 로 뜸 (env가 내가 설정한 이름)
  - 빠져나오기 : deactivate

- 라즈베리파이 GPIO 확인
    - putty 명령창에 sudo git clone https://github.com/WiringPi/WiringPi 입력하여 WiringPi 복사
    - WirionPi 경로로 들어가서 ls입력후 build 확인
    - sudo ./build 입력 후 설치
    - gpio readall 입력으로 확인

- 거리 센서 
  - 거리에 따른 출력 값 
  - 초음파 센서 + 부저 mix 
    ```python
        try:
            while True:
                distance = measure()
                if distance <= 5:
                    Buzz.start(50)
                    for i in range(0, len(melody)) :
                        Buzz.ChangeFrequency(melody[i])
                        time.sleep(0.3)
                    Buzz.stop()
                    print("Distance is 5cm under!! : %.2f cm" %distance)
                    time.sleep(1)
                else:
                    print("Distance: %.2f cm" %distance)
    ```


# day03
  - 릴레이 모듈(자동제어)
    - 릴레이는 전자석의 원리와 전자기유도원리를 이용하여 전류를 흐르게 하거나 차단하는 장치이다. 쉽게 말해서 전류의 흐름을 제어하는 장치
  
  ![릴레이](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/011.png)

  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/41b95337-f0be-406a-8867-b5bcad40999b

- 스텝모듈

  ![스텝모듈](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/012.png)

  ![스텝모듈](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/001.gif)

  - 위 그림은 스텝 모터의 구동 원리를 설명하는 그림입니다. 회전체에는 여러 개의 자석이 반대되는 극성 순서로 달려있습니다. 고정체에는 전자석이 90도 간격으로 있습니다. 180도 떨어진 전자석 2개가 한 쌍으로 다른 방향에 전류가 들어왔다가 다시 90도 떨어진 전자석으로 전류가 들어갑니다. 고정체의 전자석의 극에 따라 회전체의 자석이 끌리면서 회전하게 됩니다.

  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/cdb39ff6-41e2-4cf9-a3f6-cfdba8eb791a


- 가상환경 옵션주기
  - python -m venv --system-site-packages env
  - 접속 source ./env/bin/activate 
  - 이 경우 pip list 하면 모든 라이브러리들이 들어와있는 것을 확인 가능 

- 파이썬 기초적인 웹 구동 코드 (flask01.py)
```python
from flask import Flask  #name이름을 통한 flask객체 생성 
 
app = Flask(__name__)@@

@app.route("/")          #라우팅을 위한 뷰 함수 등록 
def hello():
  return "hello world"

if __name__ == "__main__":  #터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다 
app.run(host="0.0.0.0", debug=True) #실행을 위한 명령문으로 보면 된다 
```
  - 구동시 터미널
    ![웹구동](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/013.png)

    - 접속시 아래와 같이 확인 가능 
    192.168.5.2 - - [24/Jun/2024 14:26:48] "GET / HTTP/1.1" 200 -
    - 포트번호 변경가능 
    app.run(host="0.0.0.0", port="10123", debug=True)
    - 터미널 구동시 코드 수정하면?
    ![웹구동코드수정](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/014.png)

- 정적 라우팅(flask02.py)

  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/6c54d3af-81ff-4fad-81b5-710b272e7f5e

- 불 켜고 끄기 (flask03.py / flask04.py)
  - URL 접속을 /led/on, /led/off 로 접속하면 led를 on, off 할 수 있는 웹페이지를 만들어보기 

- 클라이언트 - 서버 - 데이터 (데이터 값 주기)
  - get 방식 
  ```python
  from flask import Flask, request
 
  app = Flask(__name__)
 
  @app.route("/")
  def get():
    value1 = request.args.get("이름","user")
    value2 = request.args.get("주소","부산")
    return value1 + ":" + value2


  if __name__ == "__main__":
    app.run(host="0.0.0.0", port="10111", debug=True)
  ```
  ![기본](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/015.png)

  ![사용](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/016.png)


# day04 
- LED 불켜기 심화 
  - flask06.py : html에 작성 및 버튼형 구현 

https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/83bf3168-eb48-4e30-8c64-d1680e8d3d44

  - flask07.py : html에 작성 및 레드, 블루, 그린 각각 불켜짐 버튼 구현 
    - 아예 꺼짐 미작동... 색상이 들어오는 현상 

    ![flask07.py](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/018.png)

  - templates 폴더 / index 및 day04 / flask08.py
    
- CAM 활용하기 
  - cam01.py : 실행시 사진 찍기 
  ```python
    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file("test1.jpg")
  ```

  ![cam01.py](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/019.png)

  - cam03.py(인제), cam04.py(근아)  : 스위치 버튼을 누를시 사진 찍기 및 찍은 시간 출력 

  ![스위치연결](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/002.jpg)

  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/4ca595a7-80d8-4d0e-acb1-eb1ac1a19091

- 4Digit 7세그먼트 구조와 외형
  ![4Digit](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/020.png)

  - 예를 들어 2를 표시하고 싶으면 a b g e d 를 사용 
  - 총 4개의 숫자의 불을 켜는 방법은 
  첫번째 번호 COM1, 두번째 번호 COM2 ...

  1. 4-digit 규격의 공통 음극(Common Cathod)방식 
    - 그림 (a)는 4-digit 규격의 공통 음극 방식 7세그먼트의 핀 번호와 핀 이름을 나타내고 있습니다. 공통 단자인 COM1,2,3,4에 모두 마이너스(-) 신호를 가하고, 데이터 신호인 a ~ g, dp에 모두 플러스(+) 신호를 가하면 모든 7세그먼트는 켜지게 됩니다. 이때 데이터 신호(a ~ g,dp)중에 하나라도 마이너스(-) 신호로 바뀌면 해당 세그먼트(공통으로 묶인 4개)는 꺼집니다.

  ![공통 음극](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/021.png)

  2.  4-digit 규격의 공통 양극(Common Anode)방식
    - 그림 (b)는 4-digit 규격의 공통 양극 방식 7세그먼트의 핀 번호와 핀 이름을 나타내고 있습니다. 공통 단자인 COM1,2,3,4에 모두 플러스(+) 신호를 가하고, 데이터 신호인 a ~ g, dp에 모두 마이너스(-) 신호를 가하면 모든 7세그먼트는 켜지게 됩니다. 이때 데이터 신호(a ~ g,dp)중에 하나라도 플러스(+) 신호로 바뀌면 해당 세그먼트(공통으로 묶인 4개)는 꺼집니다.

  ![공통 양극](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/021.png)

  ![표준디스플레이모양](https://raw.githubusercontent.com/hyeily0627/Basic-RPi-2024/main/images/022.png)

- seg01.py: 0 ~ 9까지의 숫자를 순차적으로 뜨게 하기

# day05
- seg02.py : 01 코드를 좀 더 쉽게 구현? 나름..? 

- seg04.py : 0 ~ 9까지의 숫자를 스위치를 눌렀을때 뜨도록 하기 (순차적으로)

  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/3b0dd8bc-641d-4134-b1f9-ea5aff745085

- seg05.py : 코드 실행시 패널에 0 ~ 9999 순차적으로 진행
  - seg05_01.py : 코드 더 깔끔하게! 


  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/a2c3a442-731e-4ead-8ab5-8d4a19b24277



- seg06.py : 실행시 1234가 뜨도록 하기 (스위치 사용해서는 왜 안될까용?)
  - seg06_01.py : 스위치를 누를때만 1234가 뜨도록 함 


  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/7b920bca-1a98-497b-a0a3-763f4eb1f6bc



- seg07.py : 스위치 사용시 0부터 9999까지 순차 증가 


  https://github.com/hyeily0627/Basic-openHardware-RPi-2024/assets/156732476/7f640904-123d-414a-8a9a-64d3a08b6b18


- seg08.py : 입력한 숫자를 4자리 패널에 뜨게 하기 (0~9999)

