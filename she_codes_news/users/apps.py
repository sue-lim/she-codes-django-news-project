from django.apps import AppConfig

# declare class for the configuration and the behaviour of the app which will be added to she_codes_news-settings.py 
# in this case the name given is 'user'
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
