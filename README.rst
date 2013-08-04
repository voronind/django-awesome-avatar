=====================
django-awesome-avatar
=====================

Django-awesome-avatar is a reusable application providing Avatar model field.
It allows crop selected area before saving image.

Purpose
=======

| Unlike django-avatar_ and django-upload-avatar_  
| django-awesome-avatar_ uses:

- field in profile model instead creating model for saving images
- HTML FileAPI instead hidden iframe ajax for image preview
- easy customizable presence (any view and widget templates)


Usage
=====

To integrate `django-awesome-avatar` with your site, there are few things
that are required:

#. ``pip install django-awesome-avatar``

#. List this application in the ``INSTALLED_APPS`` portion of your settings file.
Your settings file will look something like::

        INSTALLED_APPS = (
            ...
            'awesome_avatar',
        )

#.  Add the ``AvatarField`` to your profile model::
        
        from awesome_avatar.fields import AvatarField
        
        class Profile(Model):
            ...
            avatar = AvatarField(upload_to='avatars', width=100, height=100)

#.  And for example, use in ModelForm::
    
        class AvatarChangeForm(ModelForm):
            class Meta:
                model = Profile
                fields = ['avatar']
        
        ...
        return render(request, template, {'form': AvatarChangeForm})
        
Global Settings
===============

``settings.py``::
     
    AWESOME_AVATAR = {
        'width': 100,
        'height': 100,
        
        'select_area_width': 400,
        'select_area_height': 300,
        
        'save_quality': 90,
        'save_format': 'png',
        ...
    }
     
.. _django-avatar: https://github.com/jezdez/django-avatar
.. _django-upload-avatar: https://github.com/yueyoum/django-upload-avatar
.. _django-awesome-avatar: https://github.com/dimka665/django-awesome-avatar
