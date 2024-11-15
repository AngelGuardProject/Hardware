import RPi.GPIO as GPIO
import time
import requests

# GPIO 핀 설정
SOUND_SENSOR_PIN = 24  # KY-037의 D0 핀을 라즈베리파이의 GPIO 24번 핀에 연결
UUID = 0

# GPIO 모드 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)  # KY-037 디지털 핀을 입력 모드로 설정


def push():
    notification_data = {"title": "아이 울음 감지", "body": "아이 상태를 확인해 주세요"}
    url = f"http://34.47.76.73:3000/push/send/{UUID}"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=notification_data, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()  # Return the response in JSON format
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

print('started')
try:
    while True:
        # KY-037의 D0 핀에서 소리 감지 여부 확인
        sound_detected = GPIO.input(SOUND_SENSOR_PIN)
        # print(sound_detected)

        if sound_detected == GPIO.HIGH:
            response = push()
            if response:
                print(time.strftime("%H:%M:%S", time.localtime()) ," res:", response)
                time.sleep(10)  # 타이머 10초 대기 후 반복문으로 복귀
        time.sleep(0.01)  # 0.1초 대기 (반응 속도 조절)

except KeyboardInterrupt:
    print("종료 중...")

finally:
    GPIO.cleanup()  # GPIO 설정 초기화
