from django import forms
from awesome_avatar.widgets import AvatarWidget


class AvatarField(forms.ImageField):
    widget = AvatarWidget

    def to_python(self, data):
        super(AvatarField, self).to_python(data['file'])
        return data
