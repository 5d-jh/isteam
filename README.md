# ISTeam
 * 에디터: Visual Studio Code
 * Python 버전: => 3.7
 * 프레임워크: Django
 
## 실행방법
```sh
python3 -m venv venv
```

에디터 좌측 하단에 `Python 3.7.x (venv:venv)`로 바뀌었는지 확인

```sh
pip install -r requirements.txt
```

프로젝트 최상단에 `.env`파일 생성 후 다음과 같이 작성 (예시)
```
DATABASE_NAME=isteam
DATABASE_USER=root
DATABASE_PASS=1234
DATABASE_HOST=localhost
```

좌측 디버거 탭(벌레모양+플레이버튼) 클릭 후 상단의 플레이버튼 클릭시 실행 가능