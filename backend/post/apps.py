from django.apps import AppConfig
from config import settings
import os
import asyncio
class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    def ready(self):
        from .utils import proc1_main
        from .crawler import crawler_main
        # proc1_main()
        # crawler_main()
