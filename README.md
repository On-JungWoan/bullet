## 1. commit prefix

### 1-1. 코드 관련

```
feat: 기능 개발 및 기능 수정
fix: 기존에 작성된 코드 오류 개선 혹은 버그 패치
refactor: 기존 코드 구조 개선
etc: 주석 추가, 코드 살짝 변경 등 영향을 미치지 않는 수정
```

### 1-2. 기타 작업 관련

```
docs: 문서 수정 
test: test 작업 개발 및 수정
conf: 환경설정 수정
build: 빌드 관련
init: 프로젝트 생성 후 첫 커밋
merge: pull 충돌 수정
```

### 1-3. 파일 관련

```
rename: 파일 이름 및 변수명 변경
delete: 파일 삭제
move: 파일 위치 이동
```

### 1-4. 플랫폼 및 라이브러리 추가

```
add: 개발 편의성, 새로운 라이브러리 등 도입
```

<br>

## 2. GIT 명령어

협업하면서 필요한 명령어. <>는 이해를 돕기 위해 추가한 것이므로 제거하고 사용.

> e.g. <브랜치_이름> -> 브랜치_이름

### 2-0. Pull

<div align="center" style="color:red;">
    <strong>!!master 브랜치 코드가 변경된 경우 꼭 본인의 분기와 동기화 시켜줘야 함!!</strong>
</div>

<br>

```
git pull origin master
```

### 2-1. Clone

```
git clone <git 주소> --branch <branch 이름>
```

### 2-2. 현재 작업환경 확인

해당 작업은 필수는 아님. 정상적으로 push나 pull을 할 수 없는 경우 원인 확인용도로 사용하면 됨.

```
# 현재 작업 branch 확인 (본인 branch 이름이 출력되면 정상)
git branch

# 연결 remote 확인 (origin만 연결되어 있으면 됨)
git remote -v

# git config list 확인 (user.name, user.email등이 제대로 저장되어 있는지 확인)
git config -l

# 간혹 user.name과 password를 입력하라고 하는 경우 git config에 credential.helper를 store로 바꾸어 놓으면 됨
git config user.credential store
```

### 2-3. commit과 push

```
git add *
git commit -m "prefix : 커밋메시지 입력"
git push origin <본인 branch 이름>
```

### 2-4. Pull requests

github 홈페이지 Pull requests 탭 참조

