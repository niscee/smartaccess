from django.db import models

# Create your models here.
class Gallery( models.Model):
    image = models.ImageField(upload_to="gallery")


    def __str__(self):
        return str(self.image)


    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url            