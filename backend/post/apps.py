from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    # def ready(self):
    #     from .utils import backgroundApp
    #     backgroundApp()
