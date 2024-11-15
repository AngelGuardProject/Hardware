import pyaudio
import numpy as np
import time

# PyAudio 설정
audio = pyaudio.PyAudio()

# 오디오 스트림 생성
stream = audio.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True,
                    frames_per_buffer=2048)

# 사인파 테스트 신호 생성 함수
def generate_sine_wave(frequency, duration, rate=44100):
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone.astype(np.float32)

# 도레미파솔라시도 주파수 목록 (C4 ~ C5)
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
duration = 0.5  # 각 음을 0.5초 동안 재생

# 각 음을 순서대로 재생
for freq in frequencies:
    sine_wave = generate_sine_wave(freq, duration)
    for i in range(0, len(sine_wave), 2048):
        stream.write(sine_wave[i:i+2048].tobytes())
    time.sleep(0.1)  # 음 사이에 약간의 휴지기 줄여서 더 부드럽게

# 스트림 종료
stream.stop_stream()
stream.close()
audio.terminate()

print("도레미파솔라시도 출력 완료")
