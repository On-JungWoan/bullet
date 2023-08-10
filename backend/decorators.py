import mysql.connector
import environ
from .config import settings
# env = environ.Env()
# environ.Env.read_env('secrets.env')

def dataIO(func):
    def wrapper(*args, **kwargs):
        print('Output 작업시작----------------------')
        # MySQL 데이터베이스 연결 정보
        db_config = {
            "host": settings.DATABASES.get('default').get('HOST'),
            "user": settings.DATABASES.get('default').get('USER'),
            "password": settings.DATABASES.get('default').get('PASSWORD'),
            "database": settings.DATABASES.get('default').get('NAME'),
        }
        # 데이터베이스 연결
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # SELECT 쿼리 작성
        select_query='''select S.name, K.name, C.name from (SELECT DISTINCT S.site_id, K.keyword_id FROM user_usersite S
                        INNER JOIN user_userkeyword K where S.user_id=K.user_id) SK 
                        inner join service_site S inner join service_keyword K inner join service_category C
                        where SK.site_id = S.id and SK.keyword_id = K.id and C.id = S.category_id;'''
        # 쿼리 실행
        cursor.execute(select_query)
        # 결과 가져오기
        data = cursor.fetchall()
        print(data)
        # 인자값 전달
        print(func.__name__, 'start')
        #작업 결과를 바로 적용. return값 양식
#       data_to_insert = [
#           ("Site A", "Keyword A", ...),
#           ("Site B", "Keyword B", ...),
#           ("Site C", "Keyword C", ...)
#       ]


        output = func(data)
        title = list(output.keys())
        data_to_insert = tuple(
            title + [val for val in output[title[0]].values()]
        )
        # output 예시
        #
        # ('[모집공고]\xa02023 LINC 3.0 ... 공고', '「2023 LINC 3.0 혁신기술연... 지원하고자 한다.', 'https://www.jnu.ac.k...&key=57254', 'jnu', ['공고'], '2023-08-04')


        print('Input 작업시작----------------------')
        # INSERT 쿼리 작성
        insert_query = "INSERT INTO post_post (title, content, url, site, keyword, date) VALUES (%s, %s, %s, %s, %s, %s)"
        # 여러 개의 데이터 INSERT
        cursor.executemany(insert_query, data_to_insert)

        cursor.close()  

    return wrapper