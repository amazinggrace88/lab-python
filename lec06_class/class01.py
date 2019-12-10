'''
객체 지향 프로그래밍 C++ etc

클래스(class) : 데이터인 변수 선언과 기능인 함수 선언을 한꺼번에 가지고 있는(둘다 저장 가능한) **데이터 타입**
                                                                : int, float, str .. 값을 저장할 때 사용한다. 변수에 저장할 수 있는 값
               즉, 프로그램에서 만들려고 하는 대상(객체)이 가져야 할 속성(데이터)와 기능(함수)를 묶은 **데이터 타입**

필드(field) : 클래스가 가지고 있는 데이터(변수) - 대략적으로만 설명함. 더 알아보기 (= 엠버변수)
메소드(method) : 클래스가 가지고 있는 함수

만들고 싶은 대상 - 오브젝트
대상의 구성 1) 데이터 - 변수 2) 기능 - 함수(메소드 : 클래스가 가지고 있는 함수를 특별하게 부르는 것)
ex_계산기 1) 숫자 2) 연산기능


--
TV 소프트웨어 작성
대상 텔레비전
1) TV 속성(데이터) : 채널, 음량, 전원
2) TV 기능(함수=메소드) : 채널 변경, 음량 변경, 전원 변경

교재 7장

'''


# 1) class 만들어보기
class BasicTV:
    """
    Basic TV 클래스(리모컨 역할)
    """
    # 클래스 내부에서 선언하는 변수 : field (들여쓰기 중요 in class) - 모든 객체의 기본값을 준다. 어떤 생성자를 부르던지 상관없이 모든 인스턴스에 대해 동일한 값으로 시작
    max_channel, min_channel = 5, 0
    max_volume, min_volume = 5, 0

    # __init__ : 생성자가 실행되었을 때 실행되는 메소드(함수)
    # self 의 의미 : 주소값 -> BasicTV. = Self. 와 같은 의미
    def __init__(self, power, channel, volume):  # __init__(self)를 꼭 써야함!
        print('BasicTV 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume  # volume 이라는 파라미터에 저장된 객체를 self.volume 에 저장한다

    # 클래스가 내부에서 정의하는 함수 : 메소드
    def powerOnOff(self):
        if self.power:  # power 변수가 true 이면
            self.power = False
            print('TV off')
        else:  # power 변수가 false 이면
            self.power = True
            print('TV on')
    # def 사이는 두 줄 띄워준다.

    # 기능 추가시 고려할 점
    # - 채널 0 - 1 = 999 (순환/범위있음) : 0 ~ 5 까지 범위 설정하기
    # - 볼륨 최댓값 5, 최솟값 0, : 더이상 올라가지 않게, 더이상 내려가지 않게
    # - powerOnOff TV 꺼질 때 작동되지 않음

    def channelUp(self):
        # TV가 켜져 있는 경우에만 채널 변경(+1)
        if self.power:
            if self.channel < self.max_channel:
                self.channel += 1
            # 현재 채널 값이 채널의 최댓값 보다 작으면 채널 +1
            else:
            # 현재 채널값이 채널의 최댓값과 같으면 0으로 순환(= min_channel)
                self.channel = self.min_channel
            print('Channel:', self.channel) # 순환되지 않거나 채널 +1 되거나 모두 print


    def channelDown(self):
        # TV가 켜져 있는 경우에만 채널 변경(-1)
        if self.power:
            if self.channel > self.min_channel:
                self.channel -= 1
            else:
            # 현재 채널값이 채널의 최솟값과 같으면 5으로 순환(=max_channel)
                self.channel = self.max_channel
            print('Channel:', self.channel)


    def volumeUp(self):
        self.volume += 1
        print('volume:', self.volume)


    def volumeDown(self):
        self.volume -= 1
        print('volume:', self.volume)


#     클래스의 엠버변수가 되려면 들여쓰기 (4칸) 해야함
#     파이썬 함수들은 대문자가 아닌 _로 만들기 (단어와 단어를 분리)
#         ------------클래스 설계(정의) 끝


# 클래스의 객체(인스턴스)를 생성해서 변수에 저장 -> 생성자(constructor) 호출 -> 객체(object) 생성
tv1 = BasicTV(False, 0, 0)
# 출력: BasicTV(=생성자) 호출하면서 heap 상에 메모리를 확보한다.
#      확보한 메모리의 주소를 __init__을 호출할 때 self 에 준다.
# cf. ctrl + 마우스 BasicTV에 갖다대면, __init__() : 생성자로 이동

# 객체 생성의 과정
# stack : python interpreter 가 관리
# tv 1 - 주소 저장(1개)

# heap : 메모리 주소 + 객체 1개 저장
# --------------
# self.power = False : self 를 찾아서 power 에 false 를 저장한다.
# self.channel = 0
# self.volume = 0
# self : 저장장소(주소)
# powerOnOff()
# channelUp()
# ChannelDown()
# -------------- 하나의 객체로 묶여서 저장된다 (주소도 1개 = self 에 저장됨)




# 2) class instance 호출
print(tv1)  # <__main__.BasicTV object at 0x0000020ADF851B48> 현재 파일에서 직접 실행되는 모델 __main__.BasicTV object
print(tv1.power)  # tv1을 참조하면 power 라는 값이 있고 그 값은 false 이다.
print(tv1.volume)  # 객체(인스턴스).변수


# 함수와 메소드의 차이점 : self
#                     클래스가 가지는 모든 메소드는 항상 첫번째 파라미터 = self - self 에 값을 주지 않아도 된다.
# 작동 과정
# tv1(객체)가 주소를 가지고 powerOnOff(tv1)으로 들어가서 self 가 된다.(파라미터 값이 된다)
tv1.powerOnOff()  # power 가 tv1에서 false 인 상태, method 로 들어가서 powerOnOff 함수로 들어간다. - TV on 출력 + tv1의 power = true로 바뀌고 출력

tv1.channelUp()  # channel = 0인 상태 + 1
tv1.channelUp()  # channel = 1인 상태 + 1
tv1.channelDown()  # channel = 2인 상태 - 1

tv1.powerOnOff()  # power 가 tv1에서 true 인 상태, method 로 들어가서 powerOnOff 함수로 들어간다. - TV off 출력 + tv1의 power = false로 바뀌고 출력

tv1.powerOnOff()
print(tv1.channel)  # channel = 1인 상태에서 꺼졌다 다시 켜지면 1로 저장되었던 것이 그대로 출력

# channelup function test
if __name__ == '__main__':
    tv3 = BasicTV(False, 0, 0)
    print('전원상태 : ', tv3.power)
    tv3.channelUp()  # 전원 꺼진 상태에서 channel + 1
    tv3.powerOnOff()  # TV 킨다
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()  # 최댓값 5를 지나서 0으로 순환

# 3) class instance 호출 2 : 다른 객체 만들기
tv2 = BasicTV(True, 100, 5)  # tv1과 완전히 다른 tv2 생성
tv2.channelDown()  # tv2에서 channelDown 을 호출하였다.


