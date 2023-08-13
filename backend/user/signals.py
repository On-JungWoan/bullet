# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
from service.models import Keyword
@receiver(post_save, sender=User.keywords.through)
@receiver(post_delete, sender=User.keywords.through)
def update_keyword_count(sender, instance, **kwargs):
    # 유저별 소유한 keyword 개수를 업데이트하는 시그널 핸들러
    user = User.objects.get(id=instance.user_id)
    user.keywordCount = user.keywords.count()
    user.save(update_fields=['keywordCount'])

@receiver(post_delete, sender=User.keywords.through)
def delete_keyword(sender, instance, **kwargs):
    print("삭제 시그널 작동")
    # 유저가 키워드를 삭제할 때, 해당 키워드를 구독하고 있는 유저가 0명이면 키워드를 삭제하는 시그널 핸들러
    if sender.objects.filter(keyword_id=instance.keyword_id).exists() == False:
        Keyword.objects.get(id=instance.keyword_id).delete()

@receiver(post_save, sender=User.sites.through)
@receiver(post_delete, sender=User.sites.through)
def update_site_count(sender, instance, **kwargs):
    # 유저별 소유한 site 개수를 업데이트하는 시그널 핸들러
    user = User.objects.get(id=instance.user_id)
    user.siteCount = user.sites.count()
    user.save(update_fields=['siteCount'])