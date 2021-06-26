from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files import File
from ComparePhones.helpers import upload_file_name
from django.conf import settings
import os


class User(AbstractUser):
    photo = models.ImageField(upload_to=upload_file_name)

    def save(self, *args, **kwargs):
        if not self.photo.closed:
            img = Image.open(self.photo)
            img.thumbnail((1024, 1024), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')

            self.photo = File(tmp, 't.png')

        super().save(*args, **kwargs)


    @property
    def image_url(self):
        if self.image:
            return os.path.join(settings.MEDIA_URL, str(self.image))

        return os.path.join( 'assets/img/nophoto.png')
