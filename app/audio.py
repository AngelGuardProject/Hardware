import asyncio
import websockets
import pyaudio

SERVER_URI = 'ws://louk342.iptime.org:3020'  # WebSocket 서버 주소

# 오디오 스트리밍 설정
CHUNK = 4096  # 버퍼 크기를 안드로이드와 맞춤
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# PyAudio 설정
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# WebSocket 서버에 연결하여 오디오 데이터를 수신하고 출력하는 함수
async def receive_audio():
    try:
        async with websockets.connect(SERVER_URI) as websocket:
            print("서버에 연결됨")
            while True:
                data = await websocket.recv()
                stream.write(data)
    except websockets.exceptions.ConnectionClosed:
        print("서버 연결 종료")
    except KeyboardInterrupt:
        print("스트림 취소")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

# WebSocket 클라이언트 연결 및 실행
async def main():
    await receive_audio()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("클라이언트가 사용자에 의해 종료되었습니다.")
