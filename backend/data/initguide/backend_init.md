# backend django integration

### 1. 가상환경 생성
- 각자의 방식으로 파이썬 가상환경을 생성한다. 버전등의 예상치 못한 문제가 생긴다면 그때가서 해결하도록 한다.  
### 2. settings.py와 secrets.json
1. 먼저 mysql설치 후, mysql query상에서 **create database db명**을 통해 db를 생성하도록 한다.
2. 그 이후 아래와 같이 secrets.json파일이 구성되어 있는데, 이때 수정해야할 부분은 다음과 같다.
```json
{
    "SECRET_KEY": "django-insecure-+9%)il(6q8v0*=8v##43+-4z1d3oks38&0jn$tppyzdc6v-^st",
    "DATABASE_ENGINE" : "django.db.backends.mysql",
    "DATABASE_NAME" : "이 부분을 설정한 db명으로 수정한다.",
    "DATABASE_USER" : "root",
    "DATABASE_PASSWORD" : "db커넥션 비밀번호", 
    "DATABASE_HOST" : "localhost", 
    "DATABASE_PORT" : "3306"
}
```

### 3. db migration
원래 과정대로 하면 makemigrations 이후에 migrate를 하지만 makemigrations는 쿼리문을 생성하고, migrate는 쿼리문을 적용해준다. 쿼리문이 이미 형성되어 있기 때문에 makemigrations를 건너뛰고 migrate만 해준다.
```cmd
python backend/manage.py migrate
```

### 4. load data
백업용 테스트 데이터를 미리 만들어 놨는데, 이를 db에 바로 로드할 수 있다. 아래의 코드를 입력하면 미리 만들어둔 백업 데이터가 db에 로드된다. 한번 로드되면 db에 등록이 된 상태이기 때문에 추가적으로 불러올 필요는 없다.
```
python backend/manage.py loaddata backend/data/user.json backend/data/category.json backend/data/site.json backend/data/keyword.json backend/data/usersite.json backend/data/userkeyword.json
```
* 만약에 codec 뭐시기 오류가 발생한다면 backend/data경로에 있는 json파일들의 인코딩방식을 utf-8로 변경해주면 된다.

### 5. 서버실행
모두가 잘 알고있는 방법이다.
```
python backend/manage.py runserver
```

### 6. admin
admin을 사용하기 위해서는 superuser가 필요하다. 현재 4번 과정에서 load되는 데이터에 superuser데이터도 있다. 하지만 자신만의 데이터를 생성하고 싶다면 아래와 같다.
```cmd
python backend/manage.py createsuperuser
```
입력 후, 자신이 원하는 id와 비밀번호로 저장이 된다. 이 때 비밀번호가 암호화되어서 저장되는데 까먹지 않도록 한다.

**admin페이지 url : localhost:8000/admin**
![Alt text](backend/data/image/image.png)
![Alt text](backend/data/image/image-1.png)
위 url에서 로그인하여 들어오면 데이터를 직접 관리할 수 있는 화면이 뜬다.

### 7. swagger
**localhost:8000/swagger** : 어떤 url에 어떤 형식으로 데이터를 입력해야 하는지 정리해놨다.
try it out을 클릭하면 요청을 시도해볼수 있다.
![Alt text](backend/data/image/image-2.png)
실행 예시는 위와 같다. 실제 데이터 요청 시엔 request URL을 통해 요청한다.

**localhost:8000/redoc** : 문서의 형식으로 api를 확인할 수 있다.
![Alt text](backend/data/image/image-3.png)

---
**번외 - db데이터를 초기화하고 싶다**
1. mysql work bench 혹은 mysql client에서 쿼리 작성
    ```sql
    use chongr;
    delete from chongr.테이블명;
    ```
    - delete를 사용할 것. 모든테이터를 delete하는 쿼리의 경우 migration데이터도 삭제되기 때문에 이후에 'python backend/manage.py migrate'를 다시 한 번 해준다. 
    - truncate와 drop은 테이블 구조에 영향을 미치기 때문
    <br/>
    - **뭔가 꼬였다 싶으면 아래의 방법도 나쁘지 않다.**
    아예 정리하고 다시 만드는 방법이다.
        ```sql
        drop database chongr;
        create database chongr;
        ```
        이것은 상당히 좋지않은 방법이지만 가장 간단한 방법이다. 왜냐하면 우리에겐 dump해둔 데이터들과 형성된 쿼리문이 있기 때문이다.
        이후, 터미널로 돌아온다. 그리고 3번으로 돌아가 4번 과정까지 다시 한다.
<br/>

2. admin에서 삭제
    admin에서 원하는 데이터를 골라서 삭제하기
<br/>

3. 진우석에게 연락하기
    외래키관계나 다대다관계의 테이블의 경우 원활한 삭제가 어려울 수 있음
    문의
    **010-7318-4456**

---
**테스트 유저 데이터**
```json
    //일반 유저의 비밀번호 암호화는 현재 로직을 구현안한 상태
    //test1유저는 전남대학교 학생이고, 현재 공지사항 카테고리의 전남대학교, 취업 카테고리의 잡코리아를 등록하였다. 또한 장학금, 은행을 키워드로 등록하였다.
    {
    "email": "test1@gmail.com",
    "username": "test1",
    "password": "1234"
    }
    //test2유저는 직장인이고, 뉴스 카테고리의 동아일보와 조선일보를 사이트로 등록하였다. 그리고 삼성전자와 윤석열을 키워드로 등록하였다.
    {
    "email": "test2@gmail.com",
    "username": "test2",
    "password": "1234"
    }
```
