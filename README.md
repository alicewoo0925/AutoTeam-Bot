# AutoTeam-Bot
디스코드 내 음성채널에 입장한 멤버들을 랜덤으로 팀을 나눠주는 봇입니다.

## 디스코드 봇 등록
1. [Discord Developer Portal](https://discord.com/developers/docs/intro)에서 "New Application"을 통해 새 앱 등록
2. 생성된 앱 >> Settings >> Bot
3. Build-A-Bot에서 Reset Token, Copy 눌러서 토큰 복사 (나중에 코드에 적용해야 합니다.)
4. Privileged Gateway Intents에서 SERVER MEMBERS INTENT 활성화, MESSAGE CONTENT INTENT 활성화

## 봇 초대 링크 생성
1. 생성된 앱 >> Settings >> OAuth2 >> URL Generator
2. Scope에서 bot 체크, Administrator 체크

## 봇 구동하기
1. autoteambot.py 다운로드
2. 복사한 토큰값을 'YOUR_TOKEN'에 붙여넣기
3. RUN 하면 봇이 온라인 상태가 되는 것을 확인할 수 있습니다.
* 24시간 상시 사용할 경우 서버 호스팅해야합니다.
* [discord 파이썬 라이브러리 설치방법](https://discordpy-ko.github.io/intro.html)

## 사용법
1. 참여자 전체가 같은 음성채널에 입장합니다.
2. 채팅채널에서 "!팀생성 (팀원숫자)" 입력해주세요. 이때 팀원숫자는 각 팀의 인원입니다.

### 예시
![image](https://github.com/alicewoo0925/AutoTeam-Bot/assets/48823257/e3aa1c1d-3eae-4ab6-9beb-79643c6f8355)

