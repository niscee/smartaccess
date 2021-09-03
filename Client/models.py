from django.db import models

# Create your models here.
class Client( models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    link = models.URLField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="clients")


    def __str__(self):
        return str(self.title)


    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ""

        return url            