import mysql.connector

def dataIO(func):
    def wrapper():
        print('Output 작업시작----------------------')
        # MySQL 데이터베이스 연결 정보
        db_config = {
        "host": "your_host",
        "user": "your_username",
        "password": "your_password",
        "database": "your_database_name",
        }
        # 데이터베이스 연결
        conn = mysql.connector.connect(**db_config)
        # 커서 생성
        cursor = conn.cursor()
        # SELECT 쿼리 작성
        select_query = "select S.name, K.name from (SELECT DISTINCT S.site_id, K.keyword_id FROM user_UserSite S CROSS JOIN user_UserKeyword K) SK inner join service_site S inner join service_keyword K;"
        # 쿼리 실행
        cursor.execute(select_query)
        # 결과 가져오기
        data = cursor.fetchall()

        print(func.__name__, 'start')
        #작업 결과를 바로 적용. return값 양식
#       data_to_insert = [
#           ("Site A", "Keyword A", ...),
#           ("Site B", "Keyword B", ...),
#           ("Site C", "Keyword C", ...)
#       ]  
        data_to_insert = func(data)

        print('Input 작업시작----------------------')
        # INSERT 쿼리 작성
        insert_query = "INSERT INTO Post (title, content, url, site, keyword, date) VALUES (%s, %s, %s, %s, %s, %s)"
        # 여러 개의 데이터 INSERT
        cursor.executemany(insert_query, data_to_insert)
        # 쿼리 실행
        cursor.execute(insert_query,)








