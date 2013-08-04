
from django.conf import settings


class config(object):
    width = 100
    height = 100

    upload_to = 'avatars'
    save_format = 'png'
    save_quality = 90

    select_area_width = 400
    select_area_height = 250


settings_config = getattr(settings, 'AWESOME_AVATAR', {})

for key, value in settings_config.items():
    if key in config.__dict__:
        setattr(config, key, value)
    else:
        raise KeyError('Incorect option name of AWESOME_AVATAR in settings.py ({})'.format(key))