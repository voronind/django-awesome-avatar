from awesome_avatar.settings import config
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from awesome_avatar import forms

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from PIL import Image
except ImportError:
    import Image


class AvatarField(models.ImageField):
    def __init__(self, *args, **kwargs):

        self.width = kwargs.pop('width', None)
        self.height = kwargs.pop('height', None)

        kwargs['upload_to'] = kwargs.get('upload_to', config.upload_to)

        super(AvatarField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AvatarField}
        defaults.update(kwargs)
        return super(AvatarField, self).formfield(**defaults)

    def save_form_data(self, instance, data):
        # if data and self.width and self.height:
        file_ = data['file']
        if file_:

            image = Image.open(StringIO(file_.read()))

            # ratio_x = max(1, float(image.size[0]) / config.select_area_width)
            # ratio_y = max(1, float(image.size[1]) / config.select_area_height)

            image = image.crop(data['box'])
            image = image.resize((config.width, config.height), Image.ANTIALIAS)

            content = StringIO()
            image.save(content, config.save_format, quality=config.quality)

            # new_data = SimpleUploadedFile(file.name, content.getvalue(), content_type='image/' + config.save_format)
            new_data = InMemoryUploadedFile(content, None, file_.name, 'image/' + config.save_format, len(content.getvalue()), None)
            super(AvatarField, self).save_form_data(instance, new_data)
