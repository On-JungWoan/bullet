# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, UserKeyword, UserSite
import asyncio
#from post.utils import send_notification
@receiver(post_save, sender=UserKeyword)
@receiver(post_delete, sender=UserKeyword)
def update_keyword_count(sender, instance, **kwargs):
    # 유저별 소유한 keyword 개수를 업데이트하는 시그널 핸들러
    user = User.objects.get(id=instance.user_id)
    user.keywordCount = len(UserKeyword.objects.filter(user = user))
    user.save(update_fields=['keywordCount'])


@receiver(post_save, sender=User.sites.through)
@receiver(post_delete, sender=User.sites.through)
def update_site_count(sender, instance, **kwargs):
    # 유저별 소유한 site 개수를 업데이트하는 시그널 핸들러
    user = User.objects.get(id=instance.user_id)
    user.siteCount = user.sites.count()
    user.save(update_fields=['siteCount'])
