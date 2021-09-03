from django.db import models

# Create your models here.
class SiteInfo( models.Model):
    quote = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to="banner")
    logo = models.ImageField(upload_to="logo")


    def __str__(self):
        return str(self.logo)


    def imgLogoURL(self):
        try:
            url = self.logo.url
        except:
            url = ""

        return url 


    def imgBannerURL(self):
        try:
            url = self.banner.url
        except:
            url = ""

        return url               