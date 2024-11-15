# Angelguard 라즈베리파이 HW 모빌 코드
* only work on ubuntu linux
    - 다른 리눅스는 테스트 해보지 않음

- 각 기능들은 리눅스의 서비스로 등록되어 모빌이 켜질 시 자동으로 작동된다.

```bash
# rstp 작동용 
ffmpeg -f v4l2 -i /dev/video0 -f alsa -ac 1 -ar 44100 -i plughw:1,0 -c:v libx264 -preset ultrafast -c:a aac -f rtsp rtsp://louk342.iptime.org:8554/live.sdp
```

- 참고 주소 :
    - RTSP : rtsp://louk342.iptime.org:8554/live.sdp