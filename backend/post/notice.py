from datetime import timedelta
import asyncio
import datetime
import mysql.connector
from pathlib import Path
import os
import json
import firebase_admin
from firebase_admin import messaging, credentials
from config.settings import FIREBASE_PATH
import requests as r


#정해진 시간동안 비동기로 자고있다가 깨어나는 함수. 
async def send_notification(db_config):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    select_query = "SELECT * FROM post_notification ORDER BY time;"
    cursor.execute(select_query)
    data = cursor.fetchall()
    print(data," db checking..")
    if len(data) > 0:
        post_data = data[0]
        post_time = datetime.datetime.strptime(post_data[1],"%Y-%m-%d %H:%M:%S.%f")
        post_interval = post_data[2]
        # 유저에게 알림을 보냄
        current_time = datetime.datetime.now()
        #보내야하는 최초의 시간까지 남은 시간 계산
        remaining_seconds = (post_time - current_time).total_seconds()
        if remaining_seconds > 0:
            #알림을 보낼 최초의 시간까지 쳐자게 만듬
            print(f"Waiting for {remaining_seconds} seconds until {post_time}")
            await asyncio.sleep(remaining_seconds)
            #시간이 지난 후, 알림을 보낼 메시지를 가져온다.
            #param : 사용하던 커서, 유저 아이디
            messages = find_message(cursor, post_data[3])
            print(messages)
            #추후에 유저 아이디가 아닌 프론트 완성 시 유저의 파이어베이스 토큰으로 교환할 예정
            #param : 유저 아이디, 제목, 내용, 링크 
            if messages is not None:
                if messages is not list:
                    result = send_to_firebase_cloud_messaging(messages[0], messages[1])
                else:
                    for message in messages:
                        result = send_to_firebase_cloud_messaging(message[0], message[1])
                print(result)
        else:
            print("Target time has already passed.")


        # 알림을 보내고 난 후에 다음 시간으로 업데이트
        next_time = post_time + timedelta(minutes=post_interval)
        update_query = f"UPDATE post_notification SET time = '{next_time}' WHERE id = {post_data[0]};"
        cursor.execute(update_query)
        conn.commit()

        cursor.close()
        conn.close()
        return "Notification sent successfully."
    else:
        print("No notification to send.")
        await asyncio.sleep(100)
#비동기 함수를 실행시키는 함수. 새로운 프로세스는 같은 환경이 아니기 때문에 native sql과 connector사용
def notice_main():
    print(Path(__file__).resolve().parent.parent)
    secret_file = os.path.join(Path(__file__).resolve().parent.parent,'secrets.json')
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    #비밀 변수를 가져오거나 명시적 예외를 반환한다.
    # JSON 문자열을 파싱하여 db_config 딕셔너리로 변환
    db_config = {
        "host": secrets["DATABASE_HOST"],
        "user": secrets["DATABASE_USER"],
        "password": secrets["DATABASE_PASSWORD"],
        "database": secrets["DATABASE_NAME"],
    }
    while True:
    # 함수 실행
        asyncio.run(send_notification(db_config))


if __name__ == '__main__':
    notice_main()


#파이어베이스 클라우드 메시징을 통해 유저에게 알림을 보낸다.
def send_to_firebase_cloud_messaging(token, count):
    #firebase_init()
    registration_token = token
    url = "https://exp.host/--/api/v2/push/send"

    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "to": registration_token,
        "title": "알림",
        "body": f"새 소식이 {count}개 도착했습니다."
    }

    response = r.post(url, headers=headers, json=data)
    print(response)
    return response

#유저에게 해당하는 사이트, 키워드에 대한 첫번째 포스트만 가져온다. 리팩토링해야함.
def find_message(cur, user_id):
    #유저 아이디로 구분하는데 기기가 여러개일 경우 행이 여러개가 출력될 수 있음
    select_query = '''SELECT ud.fcmtoken, COUNT(*) FROM user_user AS u
        join user_device AS ud ON u.id = ud.user_id
		join user_userkeyword uk on uk.user_id = u.id
		join service_category c on uk.category_id = c.id
		join service_site s on s.category_id = c.id
		join user_usersite us on s.id = us.site_id
        join post_post p on (uk.name = p.keyword and s.code = p.site)
        WHERE u.id = %d
        GROUP BY ud.id;'''
    cur.execute(select_query, (user_id,))
    data = cur.fetchone()
    print(data)
    return data

