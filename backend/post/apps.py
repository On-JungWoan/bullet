from django.apps import AppConfig
from config import settings
import os
class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import utils
            utils.start()