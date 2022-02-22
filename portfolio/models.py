from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=200)
    greeting = models.CharField(max_length=50)
    sub_greeting = models.CharField(max_length=50, default='')
    text = models.TextField(max_length=255, blank=True)
    picture_home = models.ImageField(upload_to='picture_web/', blank=True)

    # variable para que muestre la ultima informacion guardada.
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    picture_profile = models.ImageField(upload_to='pictures_web/', blank=True)
    personal_email = models.EmailField(max_length=255, blank=True)
    ubication = models.CharField(max_length=255, blank=True)

    # variable para que muestre la ultima informacion guardada.
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class CvDownload(models.Model):
    cv_portfolio = models.FileField(upload_to='profile_documents/')


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=255, blank=True)
    project_img = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(null=True, blank=True)
    exe = models.FileField(upload_to='executable_apps/', blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)
    icon_name = models.CharField(max_length=50, null=True, blank=True)
    icon_img = models.FileField(upload_to='icon_img/', null=True, blank=True, validators=[FileExtensionValidator(['png', 'svg', 'jpg'])])

class Company_certificates(models.Model):
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Certificates(models.Model):
    name = models.CharField(max_length=250)
    company_name = models.ForeignKey(Company_certificates, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    id_credencial = models.CharField(max_length=250)
    url_credencial = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Social(models.Model):
    social_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    icon = models.ImageField(upload_to='social/', null=True)

    def __str__(self):
        return self.social_name
    
class Flag(models.Model):
    flag_img = models.FileField(upload_to='flags_img/', null=True, blank=True, validators=[FileExtensionValidator(['png', 'svg', 'jpg'])])
    data_language = models.CharField(max_length=25)

    def __str__(self):
        return self.data_language
