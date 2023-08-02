# signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import User
@receiver(m2m_changed, sender=User.keywords.through)
def update_keyword_count(sender, instance, **kwargs):
    # 유저별 소유한 keyword 개수를 업데이트하는 시그널 핸들러
    instance.keyword_count = instance.keywords.count()
    instance.save()