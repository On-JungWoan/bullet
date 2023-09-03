from datetime import timedelta
import asyncio
import datetime
from post.models import Notification


async def send_notification():
    instance = Notification.objects.filter().order_by('-time')[0]
    # 유저에게 알림을 보냄
    current_time = datetime.datetime.now().time()
    remaining_seconds = (instance.time.hour - current_time.hour) * 3600 + (instance.time.minute - current_time.minute) * 60

    if remaining_seconds > 0:
        print(f"Waiting for {remaining_seconds} seconds until {instance.time}")
        await asyncio.sleep(remaining_seconds)
        #알림을 보냄
    else:
        print("Target time has already passed.")

    # 알림을 보내고 난 후에 다음 시간을 업데이트
    next_time = instance.time + timedelta(minutes=instance.interval_minutes)
    instance.time = next_time
    instance.save()
    return send_notification()

    

